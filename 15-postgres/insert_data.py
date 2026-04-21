from urllib.parse import urlparse
from config import URL
import psycopg2

result = urlparse(URL)

username = result.username
password = result.password
database = "nikita_db"
hostname = result.hostname
port = result.port


user_data = [["кукуруза", 40, 30], ["банан", 30, 50], ["груша", 100, 100]]

with psycopg2.connect(
    database=database, user=username, password=password, host=hostname, port=port
) as connection:
    cursor = connection.cursor()
    for product in user_data:
        cursor.execute(f"""
            INSERT INTO goods (product, value, price) VALUES
            ('{product[0]}', {product[1]}, {product[2]})
            """)
    connection.commit()
