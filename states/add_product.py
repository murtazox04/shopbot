from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductState(StatesGroup):
    category_code = State()
    category_name = State()
    subcategory_code = State()
    subcategory_name = State()
    productname = State()
    photo = State()
    price = State()
    description = State()
