from flask import Flask, request
import requests
import json
import threading
import time

app = Flask(__name__)

TOKEN = "8645932660:AAEe_6AKn74W9gJioEo9tHA_WQ3d3mLObm8"
GAME_URL = "https://zaidplt22.github.io/palestine-token/"

# خدمة ngrok المجانية لإنشاء رابط عام يعمل بدون VPN
def run_ngrok():
    try:
        import subprocess
        import sys
        subprocess.Popen([sys.executable, "-m", "pyngrok", "ngrok", "http", "8080", "--log=stdout"])
        time.sleep(3)
        response = requests.get("http://localhost:4040/api/tunnels")
        tunnels = response.json()["tunnels"]
        public_url = tunnels[0]["public_url"]
        print(f"✅ الرابط العام (يعمل بدون VPN): {public_url}")
        
        # تعيين الويبهوك على الرابط العام
        webhook_url = f"{public_url}/webhook/{TOKEN}"
        requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook", 
                      json={"url": webhook_url})
        print(f"✅ تم تعيين الويبهوك على: {webhook_url}")
    except Exception as e:
        print(f"⚠️ لم نتمكن من تشغيل ngrok تلقائياً: {e}")
        print("البوت سيعمل بالطريقة العادية على الرابط المحلي")

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
    # تشغيل ngrok في خلفية (ينشئ رابطاً عاماً)
    threading.Thread(target=run_ngrok, daemon=True).start()
    
    print("✅ البوت يعمل على Render!")
    app.run(host='0.0.0.0', port=8080)
