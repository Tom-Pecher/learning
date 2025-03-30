
-- SQL: W3Schools - Main Tutorial
-- Section 23: Aliases

-- Use the as keyword to give a table or column an alias:
SELECT CustomerID AS ID
FROM Customers;

-- SELECT column_name AS alias_name
-- FROM table_name;

-- SELECT column_name(s)
-- FROM table_name AS alias_name;

-- Use as to concatenate columns:
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;
