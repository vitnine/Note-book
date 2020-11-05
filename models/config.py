from typing import Optional, List, Dict, TypedDict
from pydantic import BaseModel, validator


class BotConfig(BaseModel):
    admins: List[str]
    token: str
    parse_mode: str


class MongoConfig(BaseModel):
    uri: str
    dbname: str
    collections: List[str]


class BaseConfig(BaseModel):
    bot: BotConfig
    mongo: MongoConfig
