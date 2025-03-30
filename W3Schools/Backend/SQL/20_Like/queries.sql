
-- SQL: W3Schools - Main Tutorial
-- Section 20: Like

-- The like keyword is used for pattern matching:
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';

-- The like keyword is case insensitive:
SELECT * FROM Customers
WHERE CustomerName LIKE 'A%';

-- The _ character can be used to match any single character:
SELECT * FROM Customers
WHERE city LIKE 'L_nd__';
