import requests
from loader import dp
from aiogram import types
from states.main import Product
from aiogram.dispatcher import FSMContext
from data.info import brand_names
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



@dp.message_handler(state=Product.brand)
async def get_choose_brand(message: types.Message, state: FSMContext):
  brend = message.text
  await state.update_data(
    {'brend': brend}
  )
  # await message.answer(brend)
  for brand in brand_names:
    if brand['brand_name'] == brend:
      url2 = brand['detail']
      await state.update_data(
        {'url_model': url2}
      )
      response2 = requests.get(url2).json()
      data2 = response2['data']['phones']
      models = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      for model in data2:
        models.insert(KeyboardButton(text=model["phone_name"]))
      models.row("🔙 Ortga")
      await message.answer(f"{brend} telefonlarini modellari 🔽", reply_markup=models)
      await Product.next()
