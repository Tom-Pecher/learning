
-- SQL: W3Schools - Main Tutorial
-- Section 11: Null

-- Null values represent the absence of a value:
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;
