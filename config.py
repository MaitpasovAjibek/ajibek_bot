from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
DESTINATION = config('DESTINATION')
storage = MemoryStorage
ADMIN_ID = config('ADMIN_ID')