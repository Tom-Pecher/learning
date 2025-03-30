
-- SQL: W3Schools - Main Tutorial
-- Section 22: In

-- The in keyword is used to specify multiple values:
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

-- SELECT column_name(s)
-- FROM table_name
-- WHERE column_name IN (value1, value2, ...);
