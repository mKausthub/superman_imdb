import configparser
import json
import pickle

import redis

cfg = configparser.ConfigParser()
cfg.read("config.ini")

"""This class provides the utilty functions to perform crud operations on the Redis database"""


class Crud:
    def __init__(self):
        self.r = redis.Redis(
            host=cfg["redis_db"]["host"],
            port=cfg["redis_db"]["port"],
            db=cfg["redis_db"]["db"],
        )

    def write_db(self, data: dict):
        """@param data: response data from the OMDb_API"""
        for movie in data["Search"]:
            self.r.set(movie["imdbID"], pickle.dumps(movie))

    def read_db(self, key: str):
        """@param key: imdbID"""
        return pickle.loads(self.r.get(key))

    def get_all(self):
        for key in self.all_keys():
            yield self.read_db(key)

    def all_keys(self):
        return self.r.keys()
