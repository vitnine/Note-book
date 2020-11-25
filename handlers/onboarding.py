from aiogram.dispatcher import filters
from aiogram.types import Message

from content import keyboards
from keyboards.reply import menu, back_keyboard
from preparations import (
    dispatcher as dp,
    bot, db, ANY_STATE, config
)
from models.filters import State
from content.onboarding import Onboarding
from utils.auxiliary import States


@dp.message_handler(filters.Text(equals=(keyboards.Choosing.back, keyboards.Choosing.confirm)),
                    State(state=ANY_STATE)
                    )
@dp.message_handler(filters.CommandStart(),
                    State(state=ANY_STATE))
async def start(message: Message):
    if await db.is_user_exist():
        if await db.check_changing_status():
            await db.confirm_changed_contact()
        else:
            if message.text == keyboards.Choosing.confirm:
                added_contact_id = await db.get_contact_id()
                await message.answer(f"id добавленного вами контакта:\n"
                                     f"{added_contact_id}")
                await db.confirm_new_contact()
            else:
                await db.delete_not_finished_note()
        await message.answer(text=Onboarding.second_push, reply_markup=menu)
        await db.set_user_state(state=States.Users.START_PRESSED)
    else:
        await message.answer(Onboarding.weclome_text, reply_markup=menu)
        await db.new_user(state=States.Users.START_PRESSED)
        if str(message.from_user.id) in config.bot.admins:
            await db.set_user_role(role='admin', user_id=message.from_user.id)


@dp.message_handler(filters.Text(equals=keyboards.Menu.ask_rights),
                    State(state=ANY_STATE))
async def rights_order(message: Message):
    admin_ids = await db.get_all_admins()
    if message.from_user.id not in admin_ids:
        await message.answer('Запрос отправлен')
    for admin in admin_ids:
        await bot.send_message(chat_id=admin, text=f"Пользователь {message.from_user.first_name} "
                                                   f"{message.from_user.last_name} "
                                                   f"{message.from_user.username} "
                                                   f"с id {message.from_user.id} просит "
                                                   f"дополнительные права, для этого пропишите команду /set_right "
                                                   f"в начальном меню", reply_markup=back_keyboard)


@dp.message_handler(filters.Command('set_right'),
                    State(state=States.Users.START_PRESSED))
async def rights_order(message: Message):
    if await db.get_user_role() == 'admin':
        await message.answer('Введите id юзера которому хотиете присвоить права')
        await db.set_user_state(States.Users.ADDING_NEW_ROLE)
    else:
        await message.answer('У вас недостаточно прав')


@dp.message_handler(State(state=States.Users.ADDING_NEW_ROLE))
async def id_entering(message: Message):
    try:
        await db.set_user_role(user_id=int(message.text), role='VIP')
        await message.answer(f"Пользователю с id {message.text} успешно изменнены права", reply_markup=menu)
    except ValueError:
        await message.answer('Некорректный id')
