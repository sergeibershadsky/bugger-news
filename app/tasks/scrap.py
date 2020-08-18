from typing import List

import httpx
from loguru import logger
from lxml import html

from app.models import Article, ArticleIn_Pydantic


async def fetch_page() -> str:
    url = "https://news.ycombinator.com/"
    async with httpx.AsyncClient() as client:
        request = await client.get(url)
    request.raise_for_status()
    return request.text


def extract_articles(html_str: str) -> List[ArticleIn_Pydantic]:
    root = html.fromstring(html_str)
    articles = root.xpath("//a[@class='storylink']")
    return [
        ArticleIn_Pydantic(title=article.text, url=article.attrib['href'])
        for article in articles
    ]


async def scrap_hackernews(ctx) -> None:
    logger.info(f'Start scrap job')
    page = await fetch_page()
    articles = extract_articles(page)
    await Article.all().delete()
    await Article.bulk_create([
        Article(**article.dict())
        for article in articles
    ])
    logger.success('Job done')
