Sistema de Divisão de PDF - Instruções de Uso

1. INSTALAÇÃO
   - Certifique-se de ter Python 3 instalado no seu computador
   - Instale as dependências necessárias usando um dos comandos:
     python3 -m pip install -r requirements.txt
     ou
     pip3 install -r requirements.txt

2. INICIANDO A APLICAÇÃO WEB
   - Execute o programa usando um dos métodos:
     a) Clique duas vezes no arquivo 'launch_web_app.command'
     ou
     b) Execute no terminal:
        python3 app.py
   
   - O navegador web será aberto automaticamente com a interface do sistema
   - Se não abrir automaticamente, acesse: http://127.0.0.1:5000

3. USANDO A APLICAÇÃO
   - Na interface web:
     a) Clique em "Choose File" para selecionar o arquivo PDF
     b) Clique em "Upload & Split" para iniciar a divisão
     c) Aguarde o processamento
     d) Faça o download dos arquivos individuais ou use "Download All"

4. RESULTADOS
   - O sistema criará um arquivo PDF separado para cada página
   - Os arquivos serão nomeados seguindo o padrão:
     nome_original_page_1.pdf, nome_original_page_2.pdf, etc.
   - Você pode baixar cada arquivo individualmente ou todos de uma vez

5. SOLUÇÃO DE PROBLEMAS
   Se encontrar problemas:
   - Verifique se todas as dependências foram instaladas
   - Certifique-se de que o arquivo PDF existe e não está corrompido
   - Verifique se o tamanho do arquivo não excede 16MB
   - Certifique-se de que está usando um navegador web moderno e atualizado

Para suporte adicional, consulte a documentação do código fonte.
