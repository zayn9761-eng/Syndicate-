from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to Paki Syndicate\n\n"
        "Premium - Rs 3,000\n"
        "Premium Plus - Rs 5,000\n"
        "Exclusive - Rs 7,000\n"
        "Rare - Rs 18,000"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
