from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="soft")
async def soft(call: types.CallbackQuery):
    await call.message.edit_text("<b>🚀 Софт 🚀</b>", reply_markup=kb.soft_markup)

@dp.callback_query_handler(text="open_vpn_pro")
async def open_vpn_pro(call: types.CallbackQuery):
    text = "🚀 Проверенный впн , меняет айпи , мак-адресс, модель и марку устройства - <b>бесконечно</b>, " \
           "каждые 20 минут. Полная прошивка устройства! 🚀 \n\nЦена: <b>1000 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)


@dp.callback_query_handler(text="mac_changer_pro")
async def mac_changer_pro(call: types.CallbackQuery):
    text = "🚀 Проверенный сервис для смены Мак-адресса, хорошо подходит новичкам (в сфере скама). 🚀\n\n Цена: <b>750 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
