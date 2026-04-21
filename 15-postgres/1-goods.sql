-- Active: 1776353800541@@dpg-d7gd4fho3t8c73c6167g-a.oregon-postgres.render.com@5432@postgres
-- Створення таблиці товарів
CREATE TABLE goods (
    id SERIAL PRIMARY KEY,
    product VARCHAR(255),
    value INT,
    price DECIMAL(10, 2)
);

