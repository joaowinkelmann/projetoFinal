import psycopg2
from urllib.parse import urlparse

def connect():
    database_url = 'DATABASE_URL'

    url_parts = urlparse(database_url)
    connection = psycopg2.connect(
        host=url_parts.hostname,
        port=url_parts.port,
        database=url_parts.path[1:],
        user=url_parts.username,
        password=url_parts.password
    )
    return connection