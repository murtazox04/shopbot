from aiogram.dispatcher.filters.state import StatesGroup, State


class LanguageState(StatesGroup):
    get_lang = State()
    get_con = State()
