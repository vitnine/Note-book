from typing import List

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


from preparations import db, ANY_STATE
import re


class State(BoundFilter):
    def __init__(self, state: List[str], exception: List[str] = None) -> None:
        self.state = state
        self.exception = exception

    async def check(self, event: Message) -> bool:
        if not await db.is_user_exist():
            return True

        current_state = await db.get_user_state()
        if ((current_state in self.state or self.state == ANY_STATE)
                and (self.exception is None or current_state not in self.exception)):
            return True


        else:
            return False


def format_round(value: float, precision: int = 2) -> str:
    if isinstance(value, int):
        return '{:,}'.format(value)
    elif isinstance(value, float):
        pattern = '{:,.%df}' % precision
        return pattern.format(value)
    else:
        raise TypeError('incorrect type of value')


async def detect_numbers(text):
    phone_regex = re.compile(r"\b(\+?[7,8]\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b")
    phone = (phone_regex.findall(text)[0].replace(' ', ''))
    return phone


async def correct_interaction_form(diction):
    result = ''
    print(diction)
    if isinstance(diction, list):
        for dic in diction:
            result += '\n'
            for key in dic:
                result += f'\n{key}:  {dic[key]}'
    elif isinstance(diction, dict):
        for key in diction:
            result += f'\n{key}:  {diction[key]}'
    return result

