from loader import dp
from aiogram import types
from keyboards.default.brands import brendlar
from states.main import Product


@dp.message_handler(text="📱 Telefon Brendlari", state="*")
async def get_brands(message: types.Message):
  await message.answer("Telefon Brandlaridan birini tanlang 🔽", reply_markup=brendlar)
  await Product.brand.set()