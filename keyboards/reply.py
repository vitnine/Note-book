from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from content import keyboards


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text=keyboards.Menu.add_new_contact),
          KeyboardButton(text=keyboards.Menu.get_contact)
        ],
        [
          KeyboardButton(text=keyboards.Menu.correct_inf),
          KeyboardButton(text=keyboards.Menu.delete_contact)
        ],
        [
            KeyboardButton(text=keyboards.Menu.ask_rights)
        ]
    ],
    resize_keyboard=True
)


change_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=keyboards.Choosing.Numbers.SELF_PHONE),
                KeyboardButton(text=keyboards.Choosing.Numbers.HOME_PHONE),
                KeyboardButton(text=keyboards.Choosing.Numbers.WORK_PHONE)

            ],
            [
                KeyboardButton(text=keyboards.Choosing.Person.NAME),
                KeyboardButton(text=keyboards.Choosing.Person.SURNAME),
                KeyboardButton(text=keyboards.Choosing.Person.MIDDLE_NAME)

            ],
            [
                KeyboardButton(text=keyboards.Choosing.Address.INDEX),
                KeyboardButton(text=keyboards.Choosing.Address.AREA),
                KeyboardButton(text=keyboards.Choosing.Address.SETTLEMENT)
            ],
            [
                KeyboardButton(text=keyboards.Choosing.Address.STREET),
                KeyboardButton(text=keyboards.Choosing.Address.HOUSE),
                KeyboardButton(text=keyboards.Choosing.Address.CORPUS),
                KeyboardButton(text=keyboards.Choosing.Address.FLAT)

            ],
            [
                KeyboardButton(text=keyboards.Choosing.confirm)
            ],

        ],
        resize_keyboard=True
    )


choose_number = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=keyboards.Choosing.Numbers.SELF_PHONE),
                KeyboardButton(text=keyboards.Choosing.Numbers.HOME_PHONE),
                KeyboardButton(text=keyboards.Choosing.Numbers.WORK_PHONE)

            ],
            [
                KeyboardButton(text=keyboards.Choosing.Person.NAME),
                KeyboardButton(text=keyboards.Choosing.Person.SURNAME),
                KeyboardButton(text=keyboards.Choosing.Person.MIDDLE_NAME)

            ],
            [
                KeyboardButton(text=keyboards.Choosing.Address.INDEX),
                KeyboardButton(text=keyboards.Choosing.Address.AREA),
                KeyboardButton(text=keyboards.Choosing.Address.SETTLEMENT)
            ],
            [
                KeyboardButton(text=keyboards.Choosing.Address.STREET),
                KeyboardButton(text=keyboards.Choosing.Address.HOUSE),
                KeyboardButton(text=keyboards.Choosing.Address.CORPUS),
                KeyboardButton(text=keyboards.Choosing.Address.FLAT)

            ],
            [
                KeyboardButton(text=keyboards.Choosing.back)
            ],
            [
                KeyboardButton(text=keyboards.Choosing.confirm)
            ],

        ],
        resize_keyboard=True
    )

back_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=keyboards.Choosing.back)
            ],
        ],
        resize_keyboard=True
)


