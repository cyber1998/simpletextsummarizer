from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

from transformers import pipeline
pipe = pipeline("summarization", model="facebook/bart-large-cnn")

app = FastAPI()


class Article(BaseModel):
    article: str
    max_length: int
    min_length: int


class ArticleSummary(BaseModel):
    summary: str


@app.post("/summary/")
async def get_summary(body: Article):
    summary = pipe(body.article, max_length=body.max_length, min_length=body.min_length, do_sample=False)
    returned_summary = summary[0]['summary_text']
    return ArticleSummary(summary=returned_summary)



