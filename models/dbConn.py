import psycopg2
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

def connect():
    load_dotenv()
    
    # database_url = 'DATABASE_URL'
    database_url = os.getenv("DB_URL")

    url_parts = urlparse(database_url)
    connection = psycopg2.connect(
        host=url_parts.hostname,
        port=url_parts.port,
        database=url_parts.path[1:],
        user=url_parts.username,
        password=url_parts.password
    )
    return connection