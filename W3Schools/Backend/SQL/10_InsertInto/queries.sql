
-- SQL: W3Schools - Main Tutorial
-- Section 10: Insert Into

-- The insert into keyword is used to insert new records in a table:
-- INSERT INTO table_name (column1, column2, column3, ...)
-- VALUES (value1, value2, value3, ...);

-- When inserting new values into all columns, we do not need to specify the column names:
-- INSERT INTO table_name
-- VALUES (value1, value2, value3, ...);

INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (6, 'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

SELECT * FROM Customers;
