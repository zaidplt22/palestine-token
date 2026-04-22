from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "8645932660:AAEe_6AKn74W9gJioEo9tHA_WQ3d3mLObm8"
GAME_URL = "https://zaidplt22.github.io/palestine-token/"

# رابط البوت على Render
BASE_URL = "https://palestine-token.onrender.com"

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f'/webhook/{TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()
    if update and 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')
        
        if text == '/start':
            send_message(chat_id)
    return 'ok'

def send_message(chat_id):
    keyboard = {
        "inline_keyboard": [[{
            "text": "🎮 افتح اللعبة",
            "web_app": {"url": GAME_URL}
        }]]
    }
    
    reply_markup = json.dumps(keyboard)
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": "مرحباً بك في Palestine Token2!\nاضغط الزر أدناه لبدء اللعب.",
        "reply_markup": reply_markup
    }
    requests.post(url, json=data)

if __name__ == "__main__":
    # تعيين الويبهوك
    requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook", 
                  json={"url": f"{BASE_URL}/webhook/{TOKEN}"})
    print("✅ البوت يعمل على Render!")
    app.run(host='0.0.0.0', port=8080)
