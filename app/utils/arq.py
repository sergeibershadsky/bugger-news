from tortoise import Tortoise
import logging

from app.config.db import tortoise_settings


async def on_startup(ctx) -> None:
    await Tortoise.init(db_url=tortoise_settings.db_url, modules=tortoise_settings.modules)
    logging.info("Tortoise-ORM started, %s, %s", Tortoise._connections, Tortoise.apps)


async def on_shutdown(ctx) -> None:
    await Tortoise.close_connections()
    logging.info("Tortoise-ORM shutdown")
