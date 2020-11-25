from aiogram.utils import executor
import handlers
from preparations import dispatcher


async def on_startup(dispatcher_):
    print('ЗАПУЩЕН')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, on_startup=on_startup)
