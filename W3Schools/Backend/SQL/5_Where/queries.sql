
-- SQL: W3Schools - Main Tutorial
-- Section 5: Where

-- The where keyword is used to specify conditions for rows in a SELECT statement:
SELECT * FROM Customers
WHERE Country='Mexico';

-- SELECT column1, column2, ...
-- FROM table_name
-- WHERE condition;

-- We can use operators in our where clause to specify more conditions:
SELECT * FROM Customers
WHERE CustomerID > 2;
