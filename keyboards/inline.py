from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from content import keyboards


class Choose:
    class Callbacks:
        self_numb = "self_phone"
        home_numb = "home_numb"
        work_numb = "work_numb"
        back = "back"

    choose_number = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(text=keyboards.Choosing.Numbers.SELF_PHONE,
                                     callback_data=Callbacks.self_numb
                                     ),

                InlineKeyboardButton(text=keyboards.Choosing.Numbers.HOME_PHONE,
                                     callback_data=Callbacks.home_numb
                                     ),

                InlineKeyboardButton(text=keyboards.Choosing.Numbers.WORK_PHONE,
                                     callback_data=Callbacks.work_numb
                                     ),

                InlineKeyboardButton(text=keyboards.Choosing.back,
                                     callback_data=Callbacks.back
                                     ),
            ],
        ],
        resize_keyboard=True
    )
