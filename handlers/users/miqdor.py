from loader import dp, db
from aiogram import types
from states.main import Product
from aiogram.dispatcher import FSMContext
from keyboards.default.miqdor import miqdorlar
from keyboards.default.brands import menu


@dp.message_handler(state=Product.amount)
async def get_count(message: types.Message, state: FSMContext):
  amount = message.text
  if int(amount) >= 1:
    await state.update_data(
      {'amount': amount}
    )
    data = await state.get_data()
    model = data.get('model')
    old_amount = db.check_product(tg_id=message.from_user.id, Product=model)
    if old_amount:
      db.update_product(tg_id=message.from_user.id, Product=model, quantity=int(amount) + int(old_amount[2]))
    else:
      db.add_product(message.from_user.id, model, amount)
    await message.answer(f"{amount} ta {model} savatchaga qo'shildi", reply_markup=menu)
    await state.finish()
  else:
    await message.answer("Miqdorni to'g'ri kiriting", reply_markup=miqdorlar)
    await Product.amount.set()