from aiogram import Dispatcher

from loader import dp
from .is_user import IsUser

if __name__ == "filters":
    dp.filters_factory.bind(IsUser)
