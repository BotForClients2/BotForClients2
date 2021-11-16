from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="steam")
async def steam(call: types.CallbackQuery):
    await call.message.edit_text("<b>🎮 Steam 🎮</b>", reply_markup=kb.steam_markup)

@dp.callback_query_handler(text="account_10lvl")
async def account_10lvl(call: types.CallbackQuery):
    text = "🎮 Аккаунт 10 lvl стима 🎮" \
           "\n\nЦена: <b>100 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)

@dp.callback_query_handler(text="account_20lvl")
async def account_20lvl(call: types.CallbackQuery):
    text = "🎮 Аккаунт 20 lvl стима 🎮\n\n" \
           "<b>150 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)

@dp.callback_query_handler(text="account_40lvl")
async def account_40lvl(call: types.CallbackQuery):
    text = "🎮 Аккаунт 40 lvl стима 🎮" \
           "\n\nЦена: <b>200 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)

@dp.callback_query_handler(text="account_csgo")
async def account_csgo(call: types.CallbackQuery):
    text = "🎮 Аккаунт с CsGo (Prime) 🎮\n\n" \
           "🎖 Звания 🎖: \n\n  MM: Global. \n  Напарники: Global. \n  Запретная зона: без звания. \n\nЦена: <b>250 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)

@dp.callback_query_handler(text="account_pubg")
async def account_pubg(call: types.CallbackQuery):
    text = "🎮 Аккаунт с Pubg 🎮\n\n" \
           "Несколько красивых шмоток 🤷‍♂️ \nЗвание неизвестно.  \n\nЦена: <b>250 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
