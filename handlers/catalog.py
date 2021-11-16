from aiogram import types
from config import dp, bot
from . import keyboards as kb

@dp.callback_query_handler(text="catalog")
async def catalog(call: types.CallbackQuery):
    await call.message.edit_text("<b>Каталог:</b>", reply_markup=kb.catalog)
