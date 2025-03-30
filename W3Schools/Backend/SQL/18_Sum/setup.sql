
-- Setup

DROP TABLE IF EXISTS orderdetails;

CREATE TABLE orderdetails (
    OrderDetailID SERIAL PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);

INSERT INTO orderdetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
    (1,	10248, 11, 12),
    (2, 10248, 42, 10),
    (3, 10248, 72, 5),
    (4, 10249, 14, 9),
    (5, 10249, 51, 40);
