from aiogram.dispatcher import FSMContext

from filters import IsUser
from keyboards.inline import set_lang
from loader import db_user

import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu

from loader import dp
from states.set_lang import LanguageState


@dp.message_handler(IsUser(), CommandStart(), state=None)
async def bot_get_lang(message: types.Message):

    await message.answer(text='Please select a language.', reply_markup=set_lang.lang_button)
    await LanguageState.get_lang.set()


@dp.callback_query_handler(state=LanguageState.get_lang)
async def get_lang(call: types.CallbackQuery, state=FSMContext):
    lang = call.data
    await state.update_data(
        {'language': lang}
    )

    await call.answer(text=f'Your language {lang}')
    await call.message.answer(text='Raqamingizni 998911234567 kabi kiriting')
    await LanguageState.get_con.set()


@dp.message_handler(IsUser(), state=LanguageState.get_con)
async def bot_start(message: types.Message, state: FSMContext):
    con = message.text
    await state.update_data(
        {'contact': con}
    )

    st = await state.get_data()
    lang = st['language']
    contact = st['contact']

    try:
        db_user.telegram_id = message.from_user.id
        db_user.full_name = message.from_user.full_name
        db_user.username = message.from_user.username
        db_user.lang = lang
        db_user.contact = contact

        await db_user.add_user()
        await state.finish()
    except asyncpg.exceptions.UniqueViolationError:
        await db_user.select_user(telegram_id=message.from_user.id)

    await message.answer(
        "Xush kelibsiz! Do'konimizdagi mahsulotlarni ko'rish uchun quyidagi Menu tugmasini bosing",
        reply_markup=menu,
    )
