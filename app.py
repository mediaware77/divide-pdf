from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
from pdf_splitter import split_pdf
import tempfile
import shutil

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'File must be a PDF'}), 400
    
    try:
        # Create a temporary directory for this upload
        output_dir = tempfile.mkdtemp(dir=app.config['UPLOAD_FOLDER'])
        
        # Save the uploaded file
        filename = secure_filename(file.filename)
        input_path = os.path.join(output_dir, filename)
        file.save(input_path)
        
        # Split the PDF
        success = split_pdf(input_path, output_dir)
        
        if success:
            # Get list of split files
            split_files = [f for f in os.listdir(output_dir) if f.endswith('.pdf') and f != filename]
            split_files.sort()
            
            return jsonify({
                'success': True,
                'message': f'Successfully split into {len(split_files)} pages',
                'files': split_files,
                'directory': os.path.basename(output_dir)
            })
        else:
            return jsonify({'error': 'Failed to split PDF'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<directory>/<filename>')
def download_file(directory, filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], directory, filename)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/cleanup/<directory>')
def cleanup(directory):
    try:
        dir_path = os.path.join(app.config['UPLOAD_FOLDER'], directory)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)