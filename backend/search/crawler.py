import configparser
import urllib.parse

import requests

from search.crud import Crud

cfg = configparser.ConfigParser()
cfg.read("config.ini")

# This class provides the utility functions to query the OMDb API database
# On intitialization, it queries the api and caches responses in the database
class Crawler:
    def __init__(self):
        self.db = Crud()
        start, stop = self.get_range_from_configs()
        for page in range(start, stop):
            data = self.get_page_data(page)
            print(data)
            if not data:
                break
            self.db.write_db(data)

    def get_range_from_configs(self):

        return (
            eval(cfg["OMDb_API"]["page_range"])["start"],
            eval(cfg["OMDb_API"]["page_range"])["stop"],
        )

    def get_page_data(self, page):
        url = self.generate_omdb_api_url_by(page)
        valid_request, req = self.is_valid_request(url)
        if not valid_request:
            return False
        data = req.json()

        return data

    def generate_omdb_api_url_by(self, page):
        query_params = eval(cfg["OMDb_API"]["query_param"])
        query_params["page"] = page
        return cfg["OMDb_API"]["root"] + urllib.parse.urlencode(query_params)

    def is_valid_request(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return (False, r)

        status = eval(r.json()["Response"])
        return (status, r)
