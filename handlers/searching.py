from aiogram.dispatcher import filters
from aiogram.types import Message

from content import keyboards
from keyboards.reply import back_keyboard
from models.filters import State, correct_interaction_form
from preparations import (
    dispatcher as dp,
    db
)
from utils.auxiliary import States


@dp.message_handler(filters.Text(equals=keyboards.Menu.get_contact),
                    State(state=States.Users.START_PRESSED))
async def new_contact(message: Message):
    await message.answer('Вы вошли в режим поиска контакта')
    await message.answer('Введите информацию которую вы знаете о контакте через пробел', reply_markup=back_keyboard)
    await db.set_user_state(States.Users.SEARCHING_CONTACT)


@dp.message_handler(State(state=States.Users.SEARCHING_CONTACT))
async def address_adding(message: Message):
    intersection = await db.find_contact(inf=message.text)
    if len(intersection) > 0:
        contacts = await correct_interaction_form(intersection)
        await message.answer(contacts)
    else:
        await message.answer('Совпадения не найдены')


