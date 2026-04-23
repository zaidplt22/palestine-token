from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "8645932660:AAEe_6AKn74W9gJioEo9tHA_WQ3d3mLObm8"
GAME_URL = "https://zaidplt22.github.io/palestine-token/app.html"

@app.route('/')
def home():
    return "Bot is alive!"

@app.route(f'/webhook/{TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()
    if update and 'message' in update:
        chat_id = update['message']['chat']['id']
        if update['message'].get('text') == '/start':
            send_message(chat_id)
    return 'ok'

def send_message(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    keyboard = {
        "inline_keyboard": [[{
            "text": "🎮 افتح اللعبة",
            "web_app": {"url": GAME_URL}
        }]]
    }
    data = {
        "chat_id": chat_id,
        "text": "مرحباً بك في Palestine Token2!",
        "reply_markup": json.dumps(keyboard)
    }
    requests.post(url, json=data)

if __name__ == "__main__":
    # تعيين الويبهوك
    webhook_url = f"https://zaidplt22-palestine-token.onrender.com/webhook/{TOKEN}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook", json={"url": webhook_url})
    print("✅ البوت يعمل...")
    app.run(host='0.0.0.0', port=8080)
