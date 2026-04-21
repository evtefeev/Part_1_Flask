SELECT * FROM goods WHERE product = 'milk';


SELECT * FROM goods WHERE value > 50;


SELECT product, COUNT(*) as кількість FROM goods GROUP BY product;


CREATE INDEX idx_product ON goods (product);
CREATE INDEX idx_value ON goods (value);


SELECT * FROM goods WHERE product = 'milk';


SELECT * FROM goods WHERE value > 50;



SELECT product, COUNT(*) as кількість FROM goods GROUP BY product;


