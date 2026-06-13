from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os

TOKEN = os.getenv("BOT_TOKEN")

# START MENU
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🔥 Premium", callback_data="premium")],
        [InlineKeyboardButton("💎 Premium Plus", callback_data="premiumplus")],
        [InlineKeyboardButton("👑 Exclusive", callback_data="exclusive")],
        [InlineKeyboardButton("🚀 Rare", callback_data="rare")],
        [InlineKeyboardButton("💰 Payment Methods", callback_data="payment")],
        [InlineKeyboardButton("📞 Contact Admin", callback_data="contact")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to Paki Syndicate\n\n"
        "Choose your membership tier:",
        reply_markup=reply_markup
    )


# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "premium":
        text = (
            "🔥 PREMIUM MEMBERSHIP\n\n"
            "Price: Rs 3,000\n\n"
            "Includes:\n"
            "• Access to Premium Telegram Server\n"
            "• Daily market insights\n"
            "• Community support\n\n"
            "To purchase, contact admin."
        )

    elif query.data == "premiumplus":
        text = (
            "💎 PREMIUM PLUS MEMBERSHIP\n\n"
            "Price: Rs 5,000\n\n"
            "Includes:\n"
            "• Premium Telegram Server\n"
            "• Discord Server Access\n"
            "• Priority Support\n\n"
            "To purchase, contact admin."
        )

    elif query.data == "exclusive":
        text = (
            "👑 EXCLUSIVE MEMBERSHIP\n\n"
            "Price: Rs 7,000\n\n"
            "Includes:\n"
            "• 3 Telegram Servers\n"
            "• 2 Discord Servers\n"
            "• VIP Support\n\n"
            "To purchase, contact admin."
        )

    elif query.data == "rare":
        text = (
            "🚀 RARE MEMBERSHIP\n\n"
            "Price: Rs 18,000\n\n"
            "Includes:\n"
            "• 5 Telegram Servers\n"
            "• 3 Discord Servers\n"
            "• Highest Priority Access\n\n"
            "To purchase, contact admin."
        )

    elif query.data == "payment":
        text = (
            "💰 PAYMENT METHODS\n\n"
            "• USDT\n"
            "• Bank Transfer\n"
            "• Easypaisa\n"
            "• JazzCash\n\n"
            "After payment, send screenshot to admin."
        )

    elif query.data == "contact":
        text = (
            "📞 CONTACT ADMIN\n\n"
            "Telegram: @Ganjalordx\n\n"
            "Send payment screenshot after purchase."
        )

    await query.edit_message_text(text)


# BOT SETUP
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

if __name__ == "__main__":
    app.run_polling()