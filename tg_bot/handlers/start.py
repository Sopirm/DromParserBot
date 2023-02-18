from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link
from tg_bot.filters.private_chat import IsPrivate

dp_lnk = "577865974"


async def bot_start_with_deep_link(message: types.Message):
    # user_name = await bot.get_chat(dp_lnk)
    # РАЗОБРАТЬСЯ С ДОСТУПОМ ПО ID К USERNAME
    await message.answer(text=f"Привет , {message.from_user.full_name}, я бот парсер объявлений сайта <b>Дром</b>!\n"
                              f"Тебя пригласил пользователь с id: <b>{dp_lnk}</b>")


async def bot_start(message: types.Message):
    bot_user = await get_start_link(payload=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_menu = types.KeyboardButton(text="Меню")
    keyboard.add(button_menu)
    await message.answer(f"Привет , {message.from_user.full_name}, я бот парсер объявлений сайта <b>Дром</b>!\n\n"
                             f"Не ленись и поделись с друзьями данным ботом!\nВот твоя реферальная ссылка:\n{bot_user}", reply_markup=keyboard)

def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start_with_deep_link, CommandStart(deep_link=dp_lnk), IsPrivate())
    dp.register_message_handler(bot_start, CommandStart(), IsPrivate())