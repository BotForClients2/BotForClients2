from aiogram import types
from config import dp, bot


@dp.callback_query_handler(text="pay")
async def pay(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,
    "Реквизиты для оплаты👇\n\n 📄 <b>Перевод по никнейму: </b> TEAMALFA26 📄 \n\n"
    "<em>В комментарии к платежу указать свой айди в тг! \nПосле оплаты сделать "
     "скрин и написать админу для получения товара👇</em> \n\n 🖥  @San4ezko26  🖥  \n\n Предоставить скрин"
      " - <b>обязательно!</b>")
