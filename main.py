import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from core.handler.handler import *

async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s")
    bot = Bot(token="6856429419:AAEDFkJIwtKq4AQdq7I68mqgiR8uAN8WXFw", parse_mode='HTML')
    dp = Dispatcher()
    
    dp.message.register(start_command, Command(commands=["start"]))
    # dp.message.register(start_command1, CommandStart(deep_link=True))
    dp.message.register(get_ref, Command(commands=["reff"]))
    dp.callback_query.register(aboutus, F.data.startswith("aboutus"))
    dp.callback_query.register(start_command, F.data.startswith("back"))
    dp.callback_query.register(uslugi, F.data.startswith("uslugi"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())