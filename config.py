from aiogram import Bot, Dispatcher
import logging

bot = Bot(token="2050222752:AAHePfMjcAomZJ7lpEhL-dvnBb2_kf1epZY", parse_mode="html")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
