from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.Config import ADMINS
from loader import dp, db_prod
from states.add_product import ProductState


@dp.message_handler(commands='add_products', user_id=ADMINS)
async def add_prod(message: types.Message):
    await message.answer(text="Product categoriya-sini qo'shing qo'shing")
    await ProductState.category_code.set()


@dp.message_handler(state=ProductState.category_code)
async def category_code(message: types.Message, state: FSMContext):
    category_code = message.text

    await state.update_data(
        {'category_code': category_code,
         'category_name': category_code}
    )

    await message.answer(text='Kiyim turini kiriting')

    await ProductState.subcategory_code.set()


@dp.message_handler(state=ProductState.subcategory_code)
async def subcategory_code(message: types.Message, state: FSMContext):
    subcategory_code = message.text

    await state.update_data(
        {'subcategory_code': subcategory_code,
         'subcategory_name': subcategory_code}
    )

    await message.answer(text='Product nomini kiriting')

    await ProductState.productname.set()


@dp.message_handler(state=ProductState.productname)
async def productname(message: types.Message, state: FSMContext):
    productname = message.text

    await state.update_data(
        {'productname': productname}
    )

    await message.answer(text='Pruduct-ga rasm yuboring havola shaklida')

    await ProductState.photo.set()


@dp.message_handler(state=ProductState.photo)
async def photo(message: types.Message, state: FSMContext):
    photo = message.text

    await state.update_data(
        {'photo': photo}
    )

    await message.answer(text='Narx kiriting')

    await ProductState.price.set()


@dp.message_handler(state=ProductState.price)
async def price(message: types.Message, state: FSMContext):
    price = message.text

    await state.update_data(
        {'price': price}
    )

    await message.answer(text='Mahsulotingizga tavsif bering')

    await ProductState.description.set()


@dp.message_handler(state=ProductState.description)
async def description(message: types.Message, state: FSMContext):
    description = message.text

    await state.update_data(
        {'description': description}
    )

    st = await state.get_data()

    category_name = st['category_name']
    category_code = st['category_code']
    subcategory_code = st['subcategory_code']
    subcategory_name = st['subcategory_code']
    productname = st['productname']
    photo = st['photo']
    price = st['price']
    description = st['description']

    try:
        db_prod.category_code = category_code
        db_prod.category_name = category_name
        db_prod.subcategory_code = subcategory_code
        db_prod.subcategory_name = subcategory_name
        db_prod.productname = productname
        db_prod.photo = photo
        db_prod.price = float(price)
        db_prod.description = description
        await db_prod.add_product()

        await message.answer(text='Ma\'lumotlaringiz muvaffaqiyatli saqlandi')
    except Exception as err:
        await message.answer(text=f'{err}\nSiz xato ma\'lumot kiritdingiz')

    await state.finish()
