from aiogram import types
from config import dp, bot


@dp.callback_query_handler(text="fake_qiwi")
async def reply_for_callback(call: types.CallbackQuery):
    if call.message.text == "fake_qiwi":
        await bot.send_message(call.message.chat.id, "Hi")
