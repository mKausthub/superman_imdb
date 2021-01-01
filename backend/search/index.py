import configparser
import os
import os.path

from whoosh import index
from whoosh.qparser import QueryParser

from search.crud import Crud
from search.models.search_schema import schema

cfg = configparser.ConfigParser()
cfg.read("config.ini")


"""This class provides utility functions to create an index and add documents to it
_create(): queries the database to create an index"""


class Index:
    def __init__(self):
        if not os.path.exists(cfg["index"]["dir"]):
            os.mkdir(cfg["index"]["dir"])
        self.ix = index.create_in(cfg["index"]["dir"], schema)
        self.writer = self.ix.writer()
        self.db = Crud()

    def _create(self):
        for movie in self.db.get_all():
            self.writer.add_document(
                title=movie["Title"],
                year=movie["Year"],
                imdbID=movie["imdbID"],
                format_type=movie["Type"],
                poster_link=movie["Poster"],
            )
        self.writer.commit()

    def parse_query(self, raw_q):
        return self.parser.parse(raw_q)

    def search_query(self, q, page, page_len=cfg["search"]["page_len"]):
        searcher = self.ix.searcher()
        parser = QueryParser("title", schema=self.ix.schema)
        p_q = parser.parse(q)

        return searcher.search_page(p_q, page, page_len)

    def test_search_query(self, q, page, page_len=cfg["search"]["page_len"]):
        search_results = self.search_query(q, page, page_len)
        for i, result in enumerate(search_results):
            print("{}. {}".format(i + 1, result["title"]))

    # def clear_index(self):
    #     #TODO
    #     pass
