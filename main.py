import asyncio
import os
import json
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Загружаем карты
with open("cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

# Кнопки
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🔮 Карта дня"))

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я TaroWhisper. Нажми кнопку ниже, чтобы получить свою карту дня ✨",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == "🔮 Карта дня")
async def card_of_the_day(message: types.Message):
    card = random.choice(cards)
    await message.answer_photo(
        card["image"],
        caption=f"**{card['name']}**\n\n{card['meaning']}",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
