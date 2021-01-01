import asyncio
import configparser
from enum import Enum
from typing import Optional

import aiocron
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from search.crawler import Crawler
from search.index import Index
from search.search import Search

app = FastAPI()

cfg = configparser.ConfigParser()
cfg.read("config.ini")


app.add_middleware(
    CORSMiddleware,
    allow_origins=(eval(cfg["middleware"]["ALLOWED_HOSTS"]),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# search interface
@app.get("/search/")
async def search(
    q: str = Query(None, max_length=280),
    page: Optional[int] = Query(
        None,
        ge=eval(cfg["search"]["pg_range"])["ge"],
        le=eval(cfg["search"]["pg_range"])["le"],
    ),
):

    return Search()._query(q, page)


# Re-queries and populates database at scheduled time
# Use cron expression to set refresh rate
@aiocron.crontab(cfg["CRAWLER"]["refresh_rate"])
async def background_process():
    start_crawl = Crawler()
    index = Index()._create()
