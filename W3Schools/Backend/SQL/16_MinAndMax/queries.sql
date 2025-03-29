
-- SQL: W3Schools - Main Tutorial
-- Section 16: Min and Max

-- Min is used to find the smallest value within the selected column:
SELECT MIN(Price)
FROM Products;

-- Max is used to find the largest value within the selected column:
SELECT MAX(Price)
FROM Products;

-- SELECT MIN(column_name)
-- FROM table_name
-- WHERE condition; 

-- SELECT MAX(column_name)
-- FROM table_name
-- WHERE condition;

-- When selecting the new column, we can give it a new, more descriptive name by aliasing it:
SELECT MIN(Price) AS SmallestPrice
FROM Products;

-- Using group by, we can find the smallest price for each category: 
SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;
