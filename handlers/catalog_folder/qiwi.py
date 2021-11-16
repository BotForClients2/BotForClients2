from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="qiwi")
async def qiwi(call: types.CallbackQuery):
    await call.message.edit_text("<b>🥝 QIWI 🥝</b>", reply_markup=kb.qiwi_markup)


@dp.callback_query_handler(text="fake_qiwi")
async def qiwi(call: types.CallbackQuery):
    text = "🥝 Фейковый киви со статусом( основной ) 🥝 \n\n Цена: <b>300 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)


@dp.callback_query_handler(text="fake_qiwi_number")
async def qiwi(call: types.CallbackQuery):
    text = "🥝 Фейк номера для создания Qiwi 🥝 \n\n В наличии: <em>(3 шт.)</em> \n Цена: <b>150 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
