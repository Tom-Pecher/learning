
-- Setup

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);

INSERT INTO customers (name, age, city) VALUES 
    ('Alice', 30, 'New York'),
    ('Bob', 25, 'Los Angeles'),
    ('Charlie', 35, 'Chicago');
    