from aiogram.dispatcher import filters
from aiogram.types import Message
from preparations import (
    dispatcher as dp,
    bot
)


@dp.message_handler(filters.CommandStart())
async def start(message: Message):
    await message.answer('ты пидор')
