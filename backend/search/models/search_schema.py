from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer

schema = Schema(
    imdbID=TEXT(stored=True),
    title=TEXT(stored=True),
    poster_link=TEXT(stored=True),
    year=TEXT,
    format_type=TEXT,
)
