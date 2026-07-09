import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
from aiogram.utils import executor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv(8213646962:AAF3EqZQuk_Ml6zA99on5q6kLzRKjr-Ntug)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in .env file")

bot = Bot(token=8213646962:AAF3EqZQuk_Ml6zA99on5q6kLzRKjr-Ntug)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# ==================== TIER DATA ====================
TIERS = {
    "premium": {
        "name": "Premium",
        "stars": 250,
        "description": "Access trending and high-demand model features and casting opportunities. "
                       "Receive reliable updates, regular portfolio guidance, and consistent industry opportunities."
    },
    "premium_plus": {
        "name": "Premium Plus",
        "stars": 500,
        "description": "Enjoy complete curated access to exclusive modelling networks and opportunities. "
                       "Stay ahead with up-to-date premium material, industry insights, and balanced exclusivity."
    },
    "exclusive": {
        "name": "Exclusive",
        "stars": 1000,
        "description": "Experience true VIP status in Pakistani modelling. "
                       "Gain rare and unseen top-tier model portfolios, campaign access, "
                       "priority casting drops, and personalised opportunities."
    },
    "rare": {
        "name": "Rare",
        "stars": 2500,
        "description": "The highest level of access. Unlock ultra-rare and completely unseen content "
                       "from top campaigns, hidden archives, insider industry material, "
                       "and exclusive personalised opportunities. For those who want what others cannot obtain."
    }
}


# ==================== HANDLERS ====================
@dp.message_handler(commands=['start', 'tiers'])
async def show_tiers(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("Premium — 250 Stars", callback_data="buy_premium"),
        types.InlineKeyboardButton("Premium Plus — 500 Stars", callback_data="buy_premium_plus"),
        types.InlineKeyboardButton("Exclusive — 1000 Stars", callback_data="buy_exclusive"),
        types.InlineKeyboardButton("Rare — 2500 Stars", callback_data="buy_rare"),
    )

    await message.answer(
        "✨ <b>PAKI SYNDICATE</b> ✨\n\n"
        "<i>Where Talent Defines Status</i>\n\n"
        "Choose a tier below to unlock exclusive opportunities in the Pakistani modelling industry:",
        parse_mode="HTML",
        reply_markup=keyboard
    )


@dp.callback_query_handler(lambda c: c.data.startswith("buy_"))
async def process_buy(callback: types.CallbackQuery):
    tier_key = callback.data.replace("buy_", "")
    tier = TIERS.get(tier_key)

    if not tier:
        await callback.answer("Invalid tier selected.", show_alert=True)
        return

    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title=f"Paki Syndicate — {tier['name']}",
        description=tier['description'],
        payload=f"{tier_key}_access",
        currency="XTR",                    # Telegram Stars
        prices=[LabeledPrice(label=tier['name'], amount=tier['stars'])],
        start_parameter="paki_syndicate",
        provider_token=""
    )
    await callback.answer()


@dp.pre_checkout_query_handler(lambda q: True)
async def pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    payload = message.successful_payment.invoice_payload
    tier_key = payload.replace("_access", "")
    tier = TIERS.get(tier_key, {"name": "Selected Tier"})

    await message.answer_photo(
        photo="YOUR_FLYER_FILE_ID_HERE",   # ← Replace with your actual Paki Syndicate flyer file_id
        caption=(
            f"🎉 <b>Welcome to the {tier['name']} Tier</b>\n\n"
            f"{tier['description']}\n\n"
            "You now have access to exclusive opportunities within <b>Paki Syndicate</b>.\n\n"
            "📌 <b>Next Steps:</b>\n"
            "• Check the pinned messages in the main group\n"
            "• Contact @GANJALORDX for personalised onboarding\n\n"
            "Thank you for choosing excellence."
        ),
        parse_mode="HTML"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)