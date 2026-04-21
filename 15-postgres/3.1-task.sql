CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES departments (id)
);

-- HR
-- Finance
-- IT

INSERT INTO departments (name) VALUES 
    ('HR'), 
    ('Finance'), 
    ('IT ')
    
INSERT INTO employees (name, department_id) VALUES 
    ('Anton', (SELECT id FROM departments WHERE name = 'HR')), 
    ('Vlad', (SELECT id FROM departments WHERE name = 'Finance')), 
    ('Andrii', (SELECT id FROM departments WHERE name = 'IT')) 



-- Вам потрібно оновити всіх співробітників, які працюють у відділі "HR",
-- перевівши їх у відділ "Finance".

-- Очікуваний результат: Усі працівники, які працювали у відділі HR,
-- тепер будуть у відділі Finance.

UPDATE employees
SET
    department_id = (
        SELECT id
        FROM departments
        WHERE
            name = 'Finance'
    )
WHERE
    department_id = (
        SELECT id
        FROM departments
        WHERE
            name = 'HR'
    );