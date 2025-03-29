
-- SQL: W3Schools - Main Tutorial
-- Section 8: Or

-- Combine conditions using the OR keyword:
SELECT *
FROM Customers
WHERE Country = 'Mexico' OR CustomerName LIKE 'A%';

-- SELECT column1, column2, ...
-- FROM table_name
-- WHERE condition1 OR condition2 OR condition3 ...; 

-- In order for an item to be selected, at least one of the conditions must be true.
