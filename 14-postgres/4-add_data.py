from urllib.parse import urlparse
from config import URL
import psycopg2

result = urlparse(URL)

username = result.username
password = result.password
database = "nikita"
hostname = result.hostname
port = result.port



user_data = ["John", "john@gamil.com"]

with psycopg2.connect(
    database=database, user=username, password=password, host=hostname, port=port
) as connection:
    cursor = connection.cursor()

    cursor.execute(f"""
        INSERT INTO users (name, email) VALUES
        ('{user_data[0]}', '{user_data[1]}')
        """, user_data)
    connection.commit()


"""
INSERT INTO users (name, email) VALUES
('Ivan', 'ivan@gmail.com'),
('Anna', 'anna@gmail.com');

INSERT INTO courses (title) VALUES
('Python'),
('SQL');

INSERT INTO enrollments (user_id, course_id) VALUES
(1, 1),
(1, 2),
(2, 2);
"""
