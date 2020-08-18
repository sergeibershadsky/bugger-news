import sys

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.config.db import tortoise_settings

sys.path.extend(["./"])

app = FastAPI()

register_tortoise(
    app,
    add_exception_handlers=True,
    **tortoise_settings.dict()
)






