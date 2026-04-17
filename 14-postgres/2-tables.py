from tool import exec_sql


exec_sql("""
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    user_id INT,
    course_id INT
);
""")

