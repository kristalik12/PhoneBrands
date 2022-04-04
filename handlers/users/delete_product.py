from loader import dp, db
from aiogram import types
from keyboards.default.brands import menu

@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
  product = message.text
  product = product.replace("❌", "")
  if db.check_product(tg_id=message.from_user.id, Product=product.strip()):
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())
    await message.answer(f"{product} savatchadan o'chirildi", reply_markup=menu)
  else:
    await message.answer("Bu mahsulot savatingizda mavjud emas")