from aiogram import types

from filters import IsUser
from loader import dp


@dp.message_handler(IsUser(), commands='location')
async def location(message: types.Message):
    location = f'Chilonzor tumani Farxod bozor qarshisida OAZIS savdo markazi 2-qavatida joylashgan' \
               f'Telefon: +998 99 956 35 80\n' \
               f'Kartadan ko\'rish👇👇👇' \
               f'----- None -----'
    await message.answer(text=location)
