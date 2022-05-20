from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Eng🇺🇸', callback_data='en'),
            InlineKeyboardButton(text='Ru🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='Uz🇺🇿', callback_data='uz'),
        ]
    ]
)
