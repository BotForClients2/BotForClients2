from aiogram import types
from config import dp, bot
from . import keyboards as kb
@dp.callback_query_handler(text='social')
async def social(call: types.CallbackQuery):
    await call.message.edit_text("Связь с нами: \n\n @San4ezko26", reply_markup=kb.cancel_on_menu_markup)
