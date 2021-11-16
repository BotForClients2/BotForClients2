from aiogram import types
from config import dp, bot
from .. import keyboards as kb

@dp.callback_query_handler(text="social_accounts")
async def social_accounts(call: types.CallbackQuery):
    await call.message.edit_text("<b>📬 Аккаунты в мессенджерах 📬</b>", reply_markup=kb.social_accounts_markup)


@dp.callback_query_handler(text="social_tg")
async def social_tg(call: types.CallbackQuery):
    text = "📬 Новый аккаунт TG 📬 \n\n" \
           "Заполненный фейк акк в Телеге! \n\nЦена: <b>50 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)


@dp.callback_query_handler(text="social_inst")
async def social_inst(call: types.CallbackQuery):
    text = "📬 Новый аккаунт Inst 📬 \n\n" \
           "Заполненный фейк акк в Инсте! \n\nЦена: <b>50 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)


@dp.callback_query_handler(text="social_vk")
async def social_vk(call: types.CallbackQuery):
    text = "📬 Новый аккаунт VK 📬 \n\n" \
           "Заполненный фейк в ВК! \n\nЦена: <b>50 рублей</b>"
    await bot.send_message(call.message.chat.id, text=text, reply_markup=kb.pay)
