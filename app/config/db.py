from os import environ
from typing import Union

from pydantic import BaseSettings
from pydantic.networks import PostgresDsn

DB_MODELS = {"models": ["app.models"]}


class TortoiseSettings(BaseSettings):
    db_url: Union[PostgresDsn, str]
    modules: dict = DB_MODELS
    generate_schemas: bool = True


tortoise_settings = TortoiseSettings()
