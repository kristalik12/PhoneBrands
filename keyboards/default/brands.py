from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.info import brand_names

menu = ReplyKeyboardMarkup(
  keyboard=[
    [KeyboardButton(text="📱 Telefon Brendlari")],
    [KeyboardButton(text="🛒 Savatcha")]
  ],
  resize_keyboard=True
)


brendlar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

for brand in brand_names:
  brendlar.insert(KeyboardButton(text=brand['brand_name']))
brendlar.row("🔙 Ortga")