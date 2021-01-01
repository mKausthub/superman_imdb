import configparser

import whoosh.index as index
from fastapi.responses import JSONResponse
from whoosh.qparser import QueryParser

from search.models.search_schema import schema

cfg = configparser.ConfigParser()
cfg.read("./config.ini")

""" This class provides the utility to search indexed documents
 _query(q, page, page_len)
    @param q: query to search
    @param page: retrieve results on a given page
    @pagelen: to set a different page length. The default is 10
"""


class Search:
    def __init__(self):
        self.ix = index.open_dir(cfg["index"]["dir"])
        self.searcher = self.ix.searcher()
        self.parser = QueryParser("title", schema=self.ix.schema)

    def parse_query(self, raw_q):
        return self.parser.parse(raw_q)

    def _query(self, q: str, page: int, page_len=int(cfg["search"]["page_len"])):
        p_q = self.parse_query(q)
        results = self.searcher.search_page(p_q, page, page_len)
        return self.convert_to_JSONResponse(results)

    def convert_to_JSONResponse(self, results):
        return JSONResponse(
            {
                "total": results.total,
                "curr_page": results.pagenum,
                "page_count": results.pagecount,
                "is_last_page": results.is_last_page(),
                "runtime": results.results.runtime,
                "Search": [dict(hit) for hit in results],
            }
        )

    def test_search_query(self, q, page, page_len=cfg["search"]["page_len"]):
        search_results = self.search_query(q, page, page_len)
        for i, result in enumerate(search_results):
            print("{}. {}".format(i + 1, result["title"]))
