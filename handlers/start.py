from aiogram import types
from config import dp, bot
from . import keyboards as kb

@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    await bot.send_photo(
        message.chat.id,
        photo="AgACAgIAAxkDAAN0YY6p_IY4CPJkhjuXv4WtuKDbCz0AAsa3MRugsXhITUwo2hZfmYsBAAMCAANzAAMiBA",
        caption="<em>Приветствую вас, на нашем Dark Store Bot</em> \nНачните выбирать товар снизу👇 \nЕсли вам нужен меню напишите /menu!",
    )

    await bot.send_message(
    message.chat.id,
    text="<b> Главное меню: </b>",
    reply_markup=kb.menu
    )

@dp.message_handler(commands=['menu'])
async def menu_command(message: types.message):
    await bot.send_message(chat_id=message.chat.id, text="<b> Главное меню: </b>", reply_markup=kb.menu)
