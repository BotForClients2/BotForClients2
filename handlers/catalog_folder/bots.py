from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="bots")
async def bots(call: types.CallbackQuery):
    await call.message.edit_text("<b>🤖 Боты 🤖</b>", reply_markup=kb.bots_markup)

@dp.callback_query_handler(text="bot_shop")
async def bot_shop(call: types.CallbackQuery):
    text = "🤖 Бот-магазин 🤖\n\n" \
           "Бот схожий с нашим, просьба высказать свои пожелания одному из наших админов👇 \n\n@San4ezko26 \n\nЦена: <b>2000 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)

@dp.callback_query_handler(text="bot_info")
async def bot_info(call: types.CallbackQuery):
    text = "🤖 Бот-магазин 🤖\n\n" \
           "Бот, показывающий информацию о вашем проекте или работе. \nКол-во вкладок не ограничено. \n\nЦена: <b>2000 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
