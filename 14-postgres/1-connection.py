from urllib.parse import urlparse

import psycopg2
from config import URL

result = urlparse(URL)

username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
# print(f"""
# user: {username}
# pass: {password}
# host: {hostname}
# port: {port}
# """)

connection = psycopg2.connect(
    database=database, user=username, password=password, host=hostname, port=port
)


cursor = connection.cursor()

cursor.execute("SELECT version()")

print(cursor.fetchone())

connection.close()
