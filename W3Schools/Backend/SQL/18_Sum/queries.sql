
-- SQL: W3Schools - Main Tutorial
-- Section 18: Sum

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(100),
    Price DECIMAL
);

INSERT INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price) VALUES
    (1, 'Chais', 1, 1, '10 boxes x 20 bags', '18'),
    (2, 'Chang', 1, 1, '24 - 12 oz bottles', '19'),
    (3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', '10'),
    (4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', '22'),
    (5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', '21.35');


-- Use sum to get the total of a numeric column, possibly based on a condition:
SELECT SUM(Quantity)
FROM OrderDetails; 

-- SELECT SUM(column_name)
-- FROM table_name
-- WHERE condition;

-- Sum over an expression:
SELECT SUM(Quantity * 10)
FROM OrderDetails; 

-- We can also join the OrderDetails table to the Products table to find the actual amount:
SELECT SUM(Price * Quantity)
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID; 
