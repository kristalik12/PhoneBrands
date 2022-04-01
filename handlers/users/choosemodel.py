import requests
from loader import dp
from aiogram import types
from states.main import Product
from aiogram.dispatcher import FSMContext
from random import choice



@dp.message_handler(state=Product.model)
async def get_choose_model(message: types.Message, state: FSMContext):
  model1 = message.text
  await state.update_data(
    {'model': model1}
  )
  data = await state.get_data()
  url_model = data.get('url_model')
  # await message.answer(url_model)
  response_models = requests.get(url_model).json()['data']['phones']
  for model in response_models:
    if model['phone_name'] == model1:
      url2 = model['detail']
      await state.update_data(
        {'url_phone': url2}
      )
      response2 = requests.get(url2).json()
      photos = response2['data']['phone_images']
      release = response2['data']['release_date']
      dimension = response2['data']['dimension']
      os = response2['data']['os']
      storage = response2['data']['os']
      # await message.answer_photo(photo=model['image'], caption=f"{model1} haqida {url2}")
      photo = choice(photos)
      await message.answer_photo(photo=photo, caption=f"<b>{model1}</b>\n\nRelease Date: {release}\nDimension: {dimension}\nOS: {os}\nStorage: {storage}")
      await Product.model.set()
