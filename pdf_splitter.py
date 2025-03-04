import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_directory=None):
    """
    Split a PDF into individual pages.
    
    Args:
        input_path (str): Path to the input PDF file
        output_directory (str, optional): Directory to save the output files.
                                         If None, uses the same directory as the input file.
    """
    # Validate input file
    if not os.path.exists(input_path):
        print(f"Error: The file {input_path} does not exist.")
        return False
    
    # Validate file size
    if os.path.getsize(input_path) == 0:
        print("Error: The PDF file is empty.")
        return False
    
    # Determine output directory
    if output_directory is None:
        output_directory = os.path.dirname(input_path)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_path))[0]
    
    try:
        # Open and validate the PDF file
        with open(input_path, 'rb') as file:
            try:
                pdf = PdfReader(file)
                if not pdf.pages:
                    print("Error: Invalid or corrupted PDF file.")
                    return False
                
                total_pages = len(pdf.pages)
                if total_pages < 1:
                    print("Error: The PDF has no pages.")
                    return False
                
                print(f"Processing PDF with {total_pages} pages...")
                
                # Extract each page
                for page_num in range(total_pages):
                    pdf_writer = PdfWriter()
                    pdf_writer.add_page(pdf.pages[page_num])
                    
                    # Define output filename
                    output_filename = f"{base_filename}_page_{page_num + 1}.pdf"
                    output_path = os.path.join(output_directory, output_filename)
                    
                    # Save the page to a new PDF
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                    
                    print(f"Created: {output_filename}")
                
                print(f"Successfully split {total_pages} pages.")
                return True
                
            except Exception as pdf_error:
                print(f"Error processing PDF: {str(pdf_error)}")
                return False
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # Check if input file is provided
    if len(sys.argv) < 2:
        print("Usage: python pdf_splitter.py <input_pdf_path> [output_directory]")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    
    # Check if output directory is provided
    output_dir = None
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    
    # Split the PDF
    success = split_pdf(input_pdf, output_dir)
    
    if success:
        print("PDF splitting completed successfully.")
    else:
        print("PDF splitting failed.")
        sys.exit(1)