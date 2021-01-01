# Superman IMDb

## About
The Ultimate Search Engine to Search for Superman Movies, Series and Episodes. Built using React, FastAPI, Whoosh and Redis

![Superman_IMDb Demo](./app.JPG)


Quickstart
----------

First, install the required dependencies using ``pip install -r requirements``, and set up configurations in ``configs.ini``:

Then run the following command in ``backend/`` folder to start the FastApi-backend web app:

    uvicorn main:app --reload

To run the React front end:

    npm install
    npm start

Project structure
-----------------
    .
    superman_imdb
    ├── backend                         # backend stuff in FastAPI
    │   ├── search                      # search logic
    │   │     ├── db                    # indexed data
    │   │     └──  models               # schema for indexed data
    │   ├── config.ini                  # search configs
    │   ├── requirement.txt             # Python dependencies
    │   └── main.py                     # FastAPI application creation and configuration.
    └── frontend                        # Frontend stuff in React
