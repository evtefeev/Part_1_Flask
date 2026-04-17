from urllib.parse import urlparse

import psycopg2
from config import URL


def exec_sql(sql):
    result = urlparse(URL)

    username = result.username
    password = result.password
    database = "nikita"
    hostname = result.hostname
    port = result.port

    with psycopg2.connect(
        database=database, user=username, password=password, host=hostname, port=port
    ) as connection:
        cursor = connection.cursor()

        cursor.execute(sql)
        connection.commit()
        result = cursor.fetchall()
        return result if len(result) > 1 else result[0]
