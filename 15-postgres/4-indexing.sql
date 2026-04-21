CREATE TABLE goods (
    id SERIAL PRIMARY KEY,
    product VARCHAR(255),
    value INT,
    price DECIMAL(10, 2)
);

INSERT INTO goods (product, value, price)
SELECT
    CASE
        WHEN id % 20 = 0 THEN 'banana'
        WHEN id % 20 = 1 THEN 'milk'
        WHEN id % 20 = 2 THEN 'potato'
        WHEN id % 20 = 3 THEN 'bread'
        ELSE 'other'
    END AS product,
    FLOOR(RANDOM() * 100) + 1 AS value,
    FLOOR(RANDOM() * 50 + 10) AS price
FROM generate_series(1, 2000) AS id;