def create_users_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                avatar TEXT,
            );"""
        )
    except Exception as e:
        print(e)

class Users:
    id: int
    username: str
    email: str
    avatar: str

user = Users(0, "user", "mail@mail.com", "avatar.png")


class Posts:
    #
    #
    #
    user_id: Users


post = Posts(0, "Title", user)


def create_posts_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );"""
        )
    except Exception as e:
        print(e)