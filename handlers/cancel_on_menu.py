from aiogram import types
from config import dp, bot
from . import keyboards as kb

@dp.callback_query_handler(text="cancel_on_menu")
async def cancel_on_menu(call: types.CallbackQuery):
    await call.message.edit_text(text="<b>Главное меню:</b>", reply_markup=kb.menu)
