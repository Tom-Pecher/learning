
-- SQL: W3Schools - Main Tutorial
-- Section 6: Order By

-- The order by keyword is used to sort the result-set in ascending or descending order:
SELECT * FROM products
ORDER BY Price;

-- SELECT column1, column2, ...
-- FROM table_name
-- ORDER BY column1, column2, ... ASC|DESC;

-- We can also order by multiple columns (first order by column1, then order by column2):
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
