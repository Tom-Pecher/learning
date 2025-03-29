
-- SQL: W3Schools - Main Tutorial
-- Section 12: Update

-- The update keyword is used to update existing records in a table:
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;

SELECT * FROM Customers;

-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition; 
