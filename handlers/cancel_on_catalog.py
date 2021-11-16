from aiogram import types
from config import dp, bot
from . import keyboards as kb

@dp.callback_query_handler(text="cancel_on_catalog")
async def cancel_on_catalog(call: types.CallbackQuery):
    await call.message.edit_text("<b>Каталог:</b>", reply_markup=kb.catalog)
