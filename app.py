from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = 'MARIA'  # Define tu token de verificación aquí

@app.route('/api/v1/prediction/c835a82f-3e83-4890-b83b-e66136cfeabb', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        return verify_token(token_sent)
    elif request.method == 'POST':
        data = request.json
        # Procesa los datos recibidos del webhook de WhatsApp
        print(data)
        return jsonify({'status': 'Webhook recibido'}), 200

def verify_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return 'Token de verificación inválido', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
