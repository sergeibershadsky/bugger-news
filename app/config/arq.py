from pydantic import BaseSettings, Field
from arq.connections import RedisSettings as ArqRedisSettings


class RedisSettings(BaseSettings):
    host: str = Field("localhost", env="REDIS_IP")
    port: int = Field(6379, env="REDIS_PORT")


redis_settings = ArqRedisSettings(**RedisSettings().dict())
