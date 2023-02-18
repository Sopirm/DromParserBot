
from aiogram import Dispatcher, types


async def bot_help(message: types.Message):
    await message.answer("Список доступных команд:\n/start\n/help\n/paser\n\n"
                         "Для корректного использования команды /parser ,вводите её вместе ссылкой на интересующий бот через пробел.\n"
                         "Пример: /parser **ссылка на Дром**")

def register_help(dp: Dispatcher):
    dp.register_message_handler(callback=bot_help, commands=['help'])