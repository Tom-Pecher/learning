
-- SQL: W3Schools - Main Tutorial
-- Section 9: Not

-- Use not to negate conditions:
SELECT * FROM Customers
WHERE NOT Country = 'Germany';

-- SELECT column1, column2, ...
-- FROM table_name
-- WHERE NOT condition;

-- Use not like to negate pattern matching:
SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'A%'; -- starts with A

-- Use not between to negate ranges:
SELECT * FROM Customers
WHERE CustomerID NOT BETWEEN 2 AND 4;

-- Use not in to negate lists:
SELECT * FROM Customers
WHERE City NOT IN ('Paris', 'London');
