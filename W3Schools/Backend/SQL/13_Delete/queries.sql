
-- SQL: W3Schools - Main Tutorial
-- Section 13: Delete

-- Delete allows us to delete records from a table:
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

-- DELETE FROM table_name WHERE condition;

SELECT * FROM Customers

-- Delete all records:
-- DELETE FROM Customers;

-- Note, the table still exists, it is just empty.

-- To fully delete a table, use the DROP keyword:
-- DROP TABLE Customers
