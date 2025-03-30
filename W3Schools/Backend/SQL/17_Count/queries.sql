
-- SQL: W3Schools - Main Tutorial
-- Section 17: Count

-- Count is used to count the number of rows in a result set that match a condition:
SELECT COUNT(*)
FROM Products;

-- SELECT COUNT(column_name)
-- FROM table_name
-- WHERE condition; 

-- Count unique items by using distinct:
SELECT COUNT(DISTINCT Price)
FROM Products;

-- Use group by to return the number of records for each category:
SELECT COUNT(*) AS [Number of records], CategoryID
FROM Products
GROUP BY CategoryID;
