from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton


# cancels
cancel_on_menu = InlineKeyboardButton("Назад в главное меню 💥", callback_data='cancel_on_menu')
cancel_on_catalog = InlineKeyboardButton("Назад 💥", callback_data='cancel_on_catalog')


# menu
social = InlineKeyboardButton("👨‍💻 Связь с нами 👨‍💻", callback_data='social')
catalog = InlineKeyboardButton("📚 Каталог 📚", callback_data='catalog')
info_about_bot = InlineKeyboardButton("ℹ️ Инфо о боте ℹ️", callback_data='info_about_bot')

# catalog
qiwi = InlineKeyboardButton("🥝 QIWI 🥝", callback_data='qiwi')
soft = InlineKeyboardButton("🚀 Софт 🚀", callback_data='soft')
fishing = InlineKeyboardButton("⏰ Фишинг ⏰", callback_data='fishing')
manuals = InlineKeyboardButton("📚 Мануалы 📚", callback_data='manuals')
steam = InlineKeyboardButton("🎮 Steam 🎮", callback_data='steam')
bots = InlineKeyboardButton("🤖 Боты 🤖", callback_data='bots')
social_accounts = InlineKeyboardButton("📬 Аккаунты в мессенджерах 📬", callback_data='social_accounts')


# qiwi
fake_qiwi = InlineKeyboardButton("🥝 Fake Qiwi | 300руб | 🥝", callback_data='fake_qiwi')
fake_qiwi_number = InlineKeyboardButton("🥝 Fake номера Qiwi (3шт)| 150руб | 🥝", callback_data='fake_qiwi_number')

# soft
open_vpn_pro = InlineKeyboardButton("🚀 OpenVPN_pro | 1000руб | 🚀", callback_data='open_vpn_pro')
mac_changer_pro = InlineKeyboardButton("🚀 MacChanger_pro | 750руб | 🚀", callback_data='mac_changer_pro')

# fishing
fake_src = InlineKeyboardButton("⏰ Fake ссылка | 1000руб | ⏰", callback_data='fake_src')
fishing_social = InlineKeyboardButton("⏰ Фишинговый inst,vk,telegram | 1500руб | ⏰", callback_data='fishing_social')

# manuals
manual_scan = InlineKeyboardButton("📚 Мануал по скаму (1сп.) | 250руб | 📚", callback_data='manual_scan')
manual_security = InlineKeyboardButton("📚 Мануал по безопасности | 250руб | 📚", callback_data='manual_security')

# steam
account_10lvl = InlineKeyboardButton("🎮 Аккаунт 10lvl стима | 100руб | 🎮", callback_data='account_10lvl')
account_20lvl = InlineKeyboardButton("🎮 Аккаунт 20lvl стима | 150руб | 🎮", callback_data='account_20lvl')
account_40lvl = InlineKeyboardButton("🎮 Аккаунт 40lvl стима | 200руб | 🎮", callback_data='account_40lvl')
account_csgo = InlineKeyboardButton("🎮 Аккаунт с CsGo (Prime) | 250руб | 🎮", callback_data='account_csgo')
account_pubg = InlineKeyboardButton("🎮 Аккаунт с Pubg | 250руб | 🎮", callback_data='account_pubg')


# bots
bot_shop = InlineKeyboardButton("🤖 Бот-магазин 🤖 | 2000руб |", callback_data='bot_shop')
bot_info = InlineKeyboardButton("🤖 Инфо-бот 🤖 | 1000руб |", callback_data='bot_info')

# social accounts
social_tg = InlineKeyboardButton("📬 Новый аккаунт TG 📬: | 50руб |", callback_data='social_tg')
social_inst = InlineKeyboardButton("📬 Новый аккаунт Inst! 📬: | 50руб |", callback_data='social_inst')
social_vk = InlineKeyboardButton("📬 Новый аккаунт VK 📬: | 50руб |", callback_data='social_vk')

# pay
pay = InlineKeyboardButton("💰 Оплатить! 💰", callback_data='pay')

menu = InlineKeyboardMarkup().add(catalog).add(info_about_bot).add(social)
cancel_on_menu_markup = InlineKeyboardMarkup().add(cancel_on_menu)
catalog = InlineKeyboardMarkup().add(qiwi, soft).add(fishing, manuals).add(steam, bots).add(social_accounts).add(cancel_on_menu)
pay = InlineKeyboardMarkup().add(pay)

qiwi_markup = InlineKeyboardMarkup().add(fake_qiwi).add(fake_qiwi_number).add(cancel_on_catalog).add(cancel_on_menu)
soft_markup = InlineKeyboardMarkup().add(open_vpn_pro).add(mac_changer_pro).add(cancel_on_catalog).add(cancel_on_menu)
fishing_markup = InlineKeyboardMarkup().add(fake_src).add(fishing_social).add(cancel_on_catalog).add(cancel_on_menu)
manuals_markup = InlineKeyboardMarkup().add(manual_scan).add(manual_security).add(cancel_on_catalog).add(cancel_on_menu)
steam_markup = InlineKeyboardMarkup().add(account_10lvl).add(account_20lvl).add(account_40lvl).add(account_csgo).add(account_pubg).add(cancel_on_catalog).add(cancel_on_menu)
bots_markup = InlineKeyboardMarkup().add(bot_shop).add(bot_info).add(cancel_on_catalog).add(cancel_on_menu)
social_accounts_markup = InlineKeyboardMarkup().add(social_tg).add(social_inst).add(social_vk).add(cancel_on_catalog).add(cancel_on_menu)
