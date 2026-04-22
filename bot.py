from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
import threading
import time

TOKEN = "8645932660:AAEe_6AKn74W9gJioEo9tHA_WQ3d3mLObm8"
GAME_URL = "https://zaidplt22.github.io/palestine-token/"

# تشغيل Flask لتلبية متطلبات Render
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running!"

# إعداد بوت تلغرام
async def start(update, context):
    keyboard = [[InlineKeyboardButton("🎮 افتح اللعبة", web_app={"url": GAME_URL})]]
    await update.message.reply_text(
        "مرحباً بك في Palestine Token2!\n\nاضغط الزر أدناه لبدء التعدين والألعاب.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ البوت يعمل...")
    app.run_polling()

def run_flask():
    app_flask.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # تشغيل Flask في خيط منفصل
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # تشغيل البوت
    run_bot()
