import yaml
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from motor.motor_asyncio import AsyncIOMotorClient
from models.mongo_database import MongoDB
from utils.yaml_helper import load_yaml_files

from models.config import BaseConfig

CONFIG_PATH = 'content/config.yaml'
YAML_FILES = load_yaml_files(CONFIG_PATH, loader=yaml.SafeLoader)
config = BaseConfig(**YAML_FILES[CONFIG_PATH])


ANY_STATE = "*"
bot = Bot(
    token=config.bot.token,
    parse_mode=config.bot.parse_mode,
)
storage = MemoryStorage()

dispatcher = Dispatcher(bot=bot, storage=storage)

MONGO_CLIENT = AsyncIOMotorClient(config.mongo.uri)
MONGO_DATABASE = MONGO_CLIENT[config.mongo.dbname]

db = MongoDB(
    mongo_client=MONGO_CLIENT,
    mongo_database=MONGO_DATABASE,
    collections=config.mongo.collections
)
