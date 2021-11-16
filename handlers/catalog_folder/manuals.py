from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="manuals")
async def manuals(call: types.CallbackQuery):
    await call.message.edit_text("<b>📚 Мануалы 📚</b>", reply_markup=kb.manuals_markup)


@dp.callback_query_handler(text="manual_scan")
async def manual_scan(call: types.CallbackQuery):
    text = "📚 Основы скама, самый популярный, выгодный и легкий вид скама без вложений! 📚\n\n " \
           "Идеально подходит новичкам в этой сфере! \n\nЦена: <b>250 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)


@dp.callback_query_handler(text="manual_security")
async def manual_security(call: types.CallbackQuery):
    text = "📚 Гайд, как не пресесть в первое же время, очень советуем новичкам!  📚" \
           "\n\nЦена: <b>250 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
