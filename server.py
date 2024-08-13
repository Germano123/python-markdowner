from flask import Flask, request, send_file, jsonify
from markdown2 import markdown
from xhtml2pdf import pisa
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello to Markdowner</h1>"

@app.route('/convert', methods=['POST'])
def convert_markdown_to_pdf():
    # Recebe o conteúdo em markdown do corpo da requisição
    data = request.json
    markdown_text = data.get('markdown', '')
    
    if not markdown_text:
        return jsonify({'error': 'Nenhum texto em Markdown fornecido'}), 400
    
    # Salva o HTML em um arquivo temporário
    html_content = markdown(markdown_text)

    # Converter HTML para PDF
    with open("output.pdf", "wb") as pdf_file:
        pisa.CreatePDF(html_content, dest=pdf_file)

    # Remove o arquivo HTML temporário
    os.remove(temp_html_file)

    # Retorna o PDF como resposta
    return send_file(temp_html_file, as_attachment=True, download_name='output.html')
    
if __name__ == '_main_':
    app.run(debug=True)
