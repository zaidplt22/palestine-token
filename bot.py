import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

TOKEN = "8645932660:AAEe_6AKn74W9gJioEo9tHA_WQ3d3mLObm8"
GAME_URL = "https://zaidplt22.github.io/palestine-token/"

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("🎮 افتح اللعبة", web_app={"url": GAME_URL})]]
    await update.message.reply_text(
        "مرحباً بك في Palestine Token2!\n\n"
        "اضغط الزر أدناه لبدء التعدين والألعاب:\n"
        "يمكنك كسب PT2 عن طريق التعدين اليومي، الألعاب، والمهام.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("✅ البوت يعمل الآن...")
app.run_polling()