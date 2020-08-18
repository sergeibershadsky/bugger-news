from typing import List, Optional

from arq import ArqRedis, create_pool
from fastapi import APIRouter, HTTPException
from tortoise.exceptions import ParamsError, FieldError

from app.models import Article_Pydantic, Article
from app.config.arq import redis_settings

article_router = APIRouter()


@article_router.get('/posts', response_model=List[Article_Pydantic])
async def get_posts(order: Optional[str] = 'id', limit: Optional[int] = 5, offset: Optional[int] = 0):
    try:
        return await Article_Pydantic.from_queryset(
            Article.all().limit(limit).offset(offset).order_by(order)
        )
    except (ParamsError, FieldError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@article_router.get('/force-refresh')
async def force_refresh():
    redis: ArqRedis = await create_pool(settings_=redis_settings)
    await redis.enqueue_job("scrap_hackernews")
