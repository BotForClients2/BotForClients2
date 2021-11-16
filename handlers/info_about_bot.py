from config import bot, dp
from aiogram import types
from . import keyboards as kb

@dp.callback_query_handler(text='info_about_bot')
async def info_about_bot(call: types.CallbackQuery):
    await call.message.edit_text("Данный бот <b>не несет</b> от"
    "ветственности за вред и ущерб, нанесенные пользователям сети с помощью Наших товаров!\n"
    "\n Гарантия возврата товара в течении <b>2 недель</b>, в случае его не исправности! "
    "<u>Исправный товар, мы возвращать не будем!</u> \n \n"
    "<i>Связаться с админом данного бота можно здесь: </i> \n @San4ezko26 \n\n"
    "<i>По вопросам работы или неисправности бота обращаться сюда: </i> \n @San4ezko26", reply_markup=kb.cancel_on_menu_markup)
