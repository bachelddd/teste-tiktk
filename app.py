import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Nome do arquivo baixado
FILENAME = "tiktokdW5OUTN1iagDBP3GH8LZpglxl8Ghs2bT.txt"

# 1. Se você salvou o arquivo baixado na mesma pasta do app.py,
# ele vai ler o conteúdo exato do arquivo.
# 2. Se preferir colar a assinatura direto aqui, substitua a variável SIGNATURE pelo texto dentro do .txt.
SIGNATURE = "" 
if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding='utf-8') as f:
        SIGNATURE = f.read().strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Servir a assinatura exata para o TikTok
@app.route(f'/{FILENAME}', methods=['GET'])
@app.route(f'/tik/{FILENAME}', methods=['GET'])
def serve_tiktok_txt():
    response_text = SIGNATURE if SIGNATURE else FILENAME.replace('.txt', '')
    
    response = app.response_class(
        response=response_text,
        status=200,
        mimetype='text/plain'
    )
    # Cabeçalho para ignorar a tela de aviso do Ngrok
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)