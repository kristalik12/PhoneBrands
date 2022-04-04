from loader import dp, db
from aiogram import types
from keyboards.default.brands import menu

@dp.message_handler(text_contains="Bo'shatish")
async def delete_product(message: types.Message):
  db.clear_cart(tg_id = message.from_user.id)
  await message.answer("Savatchangiz bo'shatildi", reply_markup=menu)