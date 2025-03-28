
-- SQL: W3Schools - Main Tutorial
-- Section 4: Select Distinct

-- The select distinct keyword is used to return only distinct (different) rows:
SELECT DISTINCT city FROM Customers;

-- SELECT DISTINCT column1, column2, ...
-- FROM table_name;

-- We can use this to count the number of distinct values in a column:
SELECT COUNT(DISTINCT city) FROM Customers;

-- However this approach is incompatible with Microsoft Access databased (they do not support DISTINCT).
-- Instead, we can use a subquery:
SELECT Count(*) FROM (SELECT DISTINCT city FROM Customers) AS DistinctCities;
