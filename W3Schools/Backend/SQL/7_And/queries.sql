
-- SQL: W3Schools - Main Tutorial
-- Section 7: And

-- Combine coditions using the AND keyword:
SELECT *
FROM Customers
WHERE Country = 'Mexico' AND CustomerName LIKE 'A%'; -- G is the first letter

-- SELECT column1, column2, ...
-- FROM table_name
-- WHERE condition1 AND condition2 AND condition3 ...; 

-- In order for an item to be selected, all conditions must be true.
