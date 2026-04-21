SELECT * FROM goods LIMIT 10;

SELECT SUM(value) AS загальні_запаси FROM goods;

SELECT SUM(value) AS загальна_кількість_молока
FROM goods
WHERE
    product = 'кукуруза';

SELECT product, SUM(value) AS загальні_запаси
FROM goods
GROUP BY
    product;

SELECT SUM(value * price) AS загальний_дохід FROM goods;

SELECT product, SUM(value * price) AS дохід_по_категорії
FROM goods
GROUP BY
    product;

SELECT AVG(value) AS середній_запас FROM goods;

SELECT product, AVG(value) AS середній_запас
FROM goods
GROUP BY
    product;

SELECT COUNT(*) AS загальна_кількість_рядків FROM goods;

SELECT product, COUNT(*) AS кількість_записів
FROM goods
GROUP BY
    product;

SELECT COUNT(DISTINCT product) AS унікальні_товари FROM goods;

SELECT MAX(price) AS максимальна_ціна FROM goods;

SELECT product, MAX(price) AS максимальна_ціна
FROM goods
GROUP BY
    product;

SELECT MIN(price) AS мінімальна_ціна FROM goods;

SELECT product, MIN(price) AS мінімальна_ціна
FROM goods
GROUP BY
    product;

SELECT product, price AS максимальна_ціна
FROM goods
WHERE
    price = (
        SELECT MAX(price)
        FROM goods
    );


SELECT AVG(Grade) FROM students;


SELECT Name, AVG(Grade) FROM students GROUP BY Name