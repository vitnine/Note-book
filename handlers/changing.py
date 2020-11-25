from aiogram.dispatcher import filters
from aiogram.types import Message
from bson.errors import InvalidId

from content import keyboards
from keyboards.reply import back_keyboard, choose_number, change_keyboard
from models.filters import State, correct_interaction_form
from preparations import (
    dispatcher as dp,
    db
)
from utils.auxiliary import States


@dp.message_handler(filters.Text(equals=keyboards.Menu.delete_contact),
                    State(state=States.Users.START_PRESSED))
async def delete_contact(message: Message):
    await message.answer('Вы вошли в режим удаления контакта')
    if await db.get_user_role() == 'user':
        await message.answer('У вас недостаточно прав для выполнения этой функции')
    else:
        await message.answer('Введите id контакта которого вы хотите удалить, '
                             'его вы можете найти в меню "Найти контакт"', reply_markup=back_keyboard)
        await db.set_user_state(States.Users.DELETING_CONTACT)


@dp.message_handler(filters.Text(equals=keyboards.Menu.correct_inf),
                    State(state=States.Users.START_PRESSED))
async def change_contact(message: Message):
    await message.answer('Вы вошли в режим корректировки контакта')
    if await db.get_user_role() == 'user':
        await message.answer('У вас недостаточно прав для выполнения этой функции')
    else:
        await db.delete_not_finished_note()
        await message.answer('Введите id контакта которого вы хотите изменить, '
                             'его вы можете найти в меню "Найти контакт"', reply_markup=back_keyboard)
        if message.text != keyboards.Choosing.back:
            await db.set_user_state(States.Users.CHANGING_CONTACT)


@dp.message_handler(State(state=States.Users.CHANGING_CONTACT))
async def id_change_entering(message: Message):
    try:
        if await db.check_id(message.text):
            contact = await db.get_contact_by_id(id_=message.text)
            correct_contact = await correct_interaction_form(contact)
            await message.answer('Выберите что вы хотите изменить у этого контакта\n' + correct_contact,
                                 reply_markup=change_keyboard)
            await db.set_user_id_for_note(id_=message.text)
            await db.set_user_state(States.Users.ADDING_NEW_NOTE)
        else:
            await message.answer('Контакта с таким id не существует')
    except InvalidId:
        await message.answer('Контакта с таким id не существует')


@dp.message_handler(State(state=States.Users.DELETING_CONTACT))
async def id_entering(message: Message):
    try:
        if await db.check_id(message.text):
            await db.delete_contact(id_=message.text)
            await message.answer('Контакт успешно удалён')
        else:
            await message.answer('Контакта с таким id не существует')
    except InvalidId:
        await message.answer('Контакта с таким id не существует')
