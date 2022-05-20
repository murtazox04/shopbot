from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import Config as config
from utils.db_api.create_products import CreateProducts
from utils.db_api.create_users import CreateUsers
from utils.db_api.postgresql import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_user = CreateUsers()
db_prod = CreateProducts()
