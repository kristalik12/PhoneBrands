from aiogram.dispatcher.filters.state import StatesGroup, State


class Product(StatesGroup):
  brand = State()
  model = State()
  amount = State()