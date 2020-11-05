from aiogram.utils import executor
import handlers
from preparations import dispatcher

if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher)