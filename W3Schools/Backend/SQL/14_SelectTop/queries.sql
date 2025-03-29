
-- SQL: W3Schools - Main Tutorial
-- Section 14: Select Top

-- The top keyword is used to limit the number of rows returned:
-- SELECT TOP 3 * FROM Customers;

-- NOTE: Not all databases support this keyword. For example, MySQL uses the LIMIT keyword instead of the TOP keyword.
-- Since I am using SQLite, I will use the LIMIT keyword instead of the TOP keyword:
-- SELECT * FROM Customers LIMIT 3;

-- We can include a condition with this:
-- SELECT TOP 3 * FROM Customers
-- WHERE Country='Germany';

-- We can also include an ORDER BY clause:
-- SELECT TOP 3 * FROM Customers
-- ORDER BY CustomerID DESC;
