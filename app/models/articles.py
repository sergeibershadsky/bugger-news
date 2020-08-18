from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Article(models.Model):
    title = fields.TextField()
    url = fields.CharField(unique=True, max_length=200)
    created = fields.DatetimeField(auto_now_add=True)


Article_Pydantic = pydantic_model_creator(Article, name="Article")
ArticleIn_Pydantic = pydantic_model_creator(Article, name="ArticleIn", exclude=("id", "created"))
