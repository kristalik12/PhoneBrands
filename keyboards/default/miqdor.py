from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

miqdorlar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

for i in range(1, 10):
  miqdorlar.insert(KeyboardButton(text=f"{i}"))

miqdorlar.row("🔙 Ortga")