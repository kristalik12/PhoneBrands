from email import message
from email.message import Message
import requests
from loader import dp
from aiogram import types
from states.main import Product
from aiogram.dispatcher import FSMContext
from keyboards.default.brands import menu, brendlar


@dp.message_handler(text="🔙 Ortga", state=Product.brand)
async def go_back(message: types.Message, state: FSMContext):
  await message.answer("Asosiy sahifa", reply_markup=menu)
  await state.finish()

@dp.message_handler(text="🔙 Ortga", state=Product.model)
async def go_back(message: types.Message, state: FSMContext):
  await message.answer("Telefon Brandlaridan birini tanlang 🔽", reply_markup=brendlar)
  await Product.brand.set()