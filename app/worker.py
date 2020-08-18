import sys
from pathlib import Path
from typing import Optional

from arq import cron
from pydantic.utils import import_string
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from app.config.arq import redis_settings
from app.utils import arq
from app.tasks.scrap import scrap_hackernews
from loguru import logger

sys.path.extend(["./"])

p = Path(__file__).parents[2] / ".env"
config = Config(p if p.exists() else None)

ARQ_BACKGROUND_FUNCTIONS: Optional[CommaSeparatedStrings] = config(
    "ARQ_BACKGROUND_FUNCTIONS", cast=CommaSeparatedStrings, default=None
)

FUNCTIONS: list = [
    import_string(background_function)
    for background_function in list(ARQ_BACKGROUND_FUNCTIONS)
] if ARQ_BACKGROUND_FUNCTIONS is not None else list()


class WorkerSettings:
    on_startup = arq.on_startup
    on_shutdown = arq.on_shutdown
    redis_settings = redis_settings
    functions: list = FUNCTIONS
    cron_jobs = [
        cron(scrap_hackernews, second=5)
    ]
