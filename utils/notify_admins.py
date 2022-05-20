import logging

from aiogram import Dispatcher

from data.Config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMINS[0], "Bot ishladi")

    except Exception as err:
        logging.exception(err)
