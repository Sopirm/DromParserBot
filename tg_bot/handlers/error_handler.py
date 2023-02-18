import logging

from aiogram import Dispatcher
from aiogram.utils.exceptions import (TelegramAPIError,
                                      MessageNotModified,
                                      CantParseEntities)

async def errors_handler(update, exception):

    if isinstance(exception, MessageNotModified):
        logging.exception('Сообщение не отредактировано')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logging.exception(f"Update: {update} \n {exception}")

def register_error(dp: Dispatcher):
    dp.register_message_handler(callback=errors_handler)
