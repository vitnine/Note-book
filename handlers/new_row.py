from aiogram.dispatcher import filters
from aiogram.types import Message
from content import keyboards
from keyboards.reply import menu, choose_number
from preparations import (
    dispatcher as dp,
    bot, db, ANY_STATE
)
from models.filters import State, detect_numbers
from content.onboarding import Onboarding
from utils.auxiliary import States, Commands, Types
from content import errors


@dp.message_handler(filters.Text(equals=keyboards.Menu.add_new_contact),
                    State(state=States.Users.START_PRESSED))
async def new_contact(message: Message):
    await message.answer('Вы вошли в режим добавления нового пользователя в бд')
    if await db.get_user_role() == 'user':
        await message.answer('У вас недостаточно прав для выполнения этой функции')
    else:
        await message.answer('Выберите что вы хотите записать в новый контакт', reply_markup=choose_number)
        await db.new_note()
        await db.set_user_state(States.Users.ADDING_NEW_NOTE)


@dp.message_handler(filters.Text(equals=keyboards.Choosing.ALL_CHOOSES),
                    State(state=States.Users.new_contact_states)
                    )
async def choosing_field(message: Message):
    await message.answer('Введите ' + message.text.lower())

    # PHONE
    if message.text == keyboards.Choosing.Numbers.SELF_PHONE:
        await db.set_user_state(States.Users.Phone.SELF_PHONE)

    elif message.text == keyboards.Choosing.Numbers.WORK_PHONE:
        await db.set_user_state(States.Users.Phone.WORK_PHONE)

    elif message.text == keyboards.Choosing.Numbers.HOME_PHONE:
        await db.set_user_state(States.Users.Phone.HOME_PHONE)

    # NAME
    elif message.text == keyboards.Choosing.Person.NAME:
        await db.set_user_state(States.Users.Person.NAME_ENTERING)

    elif message.text == keyboards.Choosing.Person.SURNAME:
        await db.set_user_state(States.Users.Person.SURNAME_ENTERING)

    elif message.text == keyboards.Choosing.Person.MIDDLE_NAME:
        await db.set_user_state(States.Users.Person.MIDDLE_NAME_ENTERING)

    # ADDRESS
    elif message.text == keyboards.Choosing.Address.INDEX:
        await db.set_user_state(States.Users.Address.INDEX)

    elif message.text == keyboards.Choosing.Address.SETTLEMENT:
        await db.set_user_state(States.Users.Address.SETTLEMENT)

    elif message.text == keyboards.Choosing.Address.AREA:
        await db.set_user_state(States.Users.Address.AREA)

    elif message.text == keyboards.Choosing.Address.STREET:
        await db.set_user_state(States.Users.Address.STREET)

    elif message.text == keyboards.Choosing.Address.HOUSE:
        await db.set_user_state(States.Users.Address.HOUSE)

    elif message.text == keyboards.Choosing.Address.CORPUS:
        await db.set_user_state(States.Users.Address.CORPUS)

    elif message.text == keyboards.Choosing.Address.FLAT:
        await db.set_user_state(States.Users.Address.FLAT)


@dp.message_handler(State(state=States.Users.phone_states)
                    )
async def phone_adding(message: Message):
    current_state = await db.get_user_state()
    try:
        phone_number = await detect_numbers(text=message.text)
        await db.set_new_field(name=phone_number, name_type=current_state)
        await message.answer('Данные загружены в БД')
    except IndexError:
        await message.answer(errors.NewContactErr.not_found_or_incorrect)


@dp.message_handler(State(state=States.Users.name_states)
                    )
async def name_adding(message: Message):
    current_state = await db.get_user_state()
    name = message.text.capitalize()
    await db.set_new_field(name=name, name_type=current_state)
    await message.answer('Данные загружены в БД')


@dp.message_handler(State(state=States.Users.address_states)
                    )
async def address_adding(message: Message):
    current_state = await db.get_user_state()
    if current_state in States.Users.numbers_in_address:
        try:
            int(message.text)
            await db.set_new_field(name=message.text, name_type=current_state)
            await message.answer('Данные загружены в БД')
        except ValueError:
            await message.answer(errors.NewContactErr.wrong_type)
    else:
        name = message.text.capitalize()
        await db.set_new_field(name=name, name_type=current_state)
        await message.answer('Данные загружены в БД')


