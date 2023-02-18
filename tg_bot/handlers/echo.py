from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode


async def bot_echo(message: types.Message):
    await message.answer(text="Бот пока работает в тестовом режиме, для проверки парсера используйте команду "
                              "/parser.\nНе забудьте ввести после неё ссылку на интересующие объявления на сайте "
                              "Дром.")


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state=None)
