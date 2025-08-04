import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📢 Telegram Channel", url="https://t.me/FreeCryptoRewardsBotNews"),
        InlineKeyboardButton("▶️ Play", callback_data="play")
    )
    await message.answer_photo(
        photo="https://example.com/bot-image.jpg",  # Мұнда бот суретінің URL-сын қоясың
        caption="🤖 Welcome to FreeCryptoRewards Bot!\n\nEarn free crypto by completing simple tasks! 💰",
        reply_markup=keyboard
    )

@dp.callback_query_handler(lambda call: call.data == "play")
async def play_game(call: types.CallbackQuery):
    await call.message.answer("🎮 Let's start earning crypto! Complete your first task now!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
