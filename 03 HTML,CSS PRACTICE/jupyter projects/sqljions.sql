CREATE DATABASE JOINS_DB;
USE JOINS_DB;
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Country VARCHAR(50)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    Amount INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Customers 
(CustomerID, Name, Country)
 VALUES
(1, 'John', 'USA'),
(2, 'Alice', 'UK'),
(3, 'Bob', 'India'),
(4, 'Mike', 'Canada'),
(5, 'Sara', 'USA');
DROP DATABASE joins_db;

INSERT INTO Orders 
(OrderID, CustomerID, Amount)
VALUES
(101, 1, 500),
(102, 3, 300),
(103, 1, 700),
(104, 2, 100),
(105, 4, 400),
(106, NULL, 250); 

SELECT * FROM CUSTOMERS;
SELECT * FROM orders;

SELECT *
FROM Customers AS C
INNER JOIN Orders as O
ON C.CustomerID=O.CustomerID;

SELECT *
FROM Customers as c
LEFT JOIN orders as o
ON c.customerID=o.customerid;

SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
ON C.customerID=o.customerID;
 
SELECT *
FROM customers AS c
LEFT JOIN orders AS o
ON C.customerID=o.customerID
UNION
SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
ON C.customerID=o.customerID;

SELECT * 
FROM customers AS c
LEFT JOIN Orders as o
ON c.customerID=o.customerID
WHERE o.orderID IS NULL;
 

SELECT * 
FROM customers AS c
RIGHT JOIN Orders as o
ON c.customerID=o.customerID
WHERE c.customerID IS NULL;
 
SELECT * 
FROM customers AS c
RIGHT JOIN Orders as o
ON c.customerID=o.customerID
WHERE c.customerID IS NULL;
 
SELECT * 
FROM customers 
INNER JOIN Orders as o
ON c.customerID=o.customerID
WHERE c.customerID IS NULL;
 
SELECT CUSTOMERS.NAME ,SUM(orders.amount) AS TotalAmount
FROM customers 
RIGHT JOIN Orders
ON customers.customerID=Orders.customerID
GROUP BY Customers.name;

SELECT *
FROM Customers
RIGHT JOIN Orders
ON Orders.customerID=Customers.customerID;

SELECT *
FROM Orders
LEFT JOIN Customers
ON Orders.customerID=Customers.customerID;

SELECT DISTINCT  Customers.name
FROM Customers
INNER JOIN Orders
ON Customers.customerID=Orders.customerID
;
 
SELECT Customers.Customerid, Customers.name 
FROM  Customers
INNER JOIN Orders
ON Customers.customerID=orders.customerID
GROUP BY  Customers.customerid, Customers.name
HAVING COUNT(orders.orderid) > 1;

SELECT DISTINCT Customers.name 
FROM  Customers
INNER JOIN Orders
ON Customers.customerID=orders.customerID
GROUP BY   Customers.name
HAVING COUNT(orders.orderid) > 0;

SELECT Customers.Customerid, Customers.name 
FROM  Customers
INNER JOIN Orders
ON Customers.customerID=orders.customerID
GROUP BY  Customers.customerid, Customers.name
HAVING SUM(orders.Amount) > 1000;

SELECT * FROM customers;

SELECT DISTINCT Customers.customerID, customers.name 
FROM customers
INNER JOIN Orders
ON Customers.customerID=Orders.customerID
WHERE customers.country='USA' ;

SELECT DISTINCT Customers.customerID, customers.name, COUNT(orders.orderID) AS total_orders
FROM CUSTOMERS
LEFT JOIN Orders
ON Customers.customerID=Orders.customerID
GROUP BY Customers.customerID, customers.name;

SELECT DISTINCT Customers.customerID, customers.name, COUNT(orders.orderID) AS total_orders
FROM CUSTOMERS
LEFT JOIN Orders
ON Customers.customerID=Orders.customerID
GROUP BY Customers.customerID, customers.name;

SELECT  Customers.customerID, customers.name, SUM(Orders.Amount) AS Total_Amount
FROM CUSTOMERS
LEFT JOIN Orders
ON Customers.customerID=Orders.customerID
GROUP BY Customers.customerID, customers.name;

SELECT * FROM orders;
SELECT * FROM customers;

SELECT Customers.customerID, customers.name ,COUNT(Orders.orderID) AS TOTAL_ORDERS
FROM  Customers
LEFT JOIN Orders 
ON Customers.customerID=Orders.customerID
GROUP BY Customers.customerID, customers.name;

SELECT Customers.customerID, customers.name ,AVG(Orders.Amount) AS AVG_Amount
FROM  Customers
LEFT JOIN Orders 
ON Customers.customerID=Orders.customerID
GROUP BY Customers.customerID, customers.name;

SELECT Customers.customerID, customers.name 
FROM  Customers
INNER JOIN Orders 
ON Customers.customerID=Orders.customerID
GROUP BY Customers.customerID, customers.name
HAVING COUNT(Orders.orderID) > 1;


SELECT Customers.CustomerID, Customers.name, MIN(Orders.Amount) AS Min_Amount , MAX(Orders.Amount) AS Max_Amount, COUNT(ORDERS.orderID),AVG(Orders.Amount)
FROM CUSTOMERS 
LEFT JOIN ORDERS
ON  Customers.CustomerID= ORDERS.CustomerID
GROUP BY Customers.CustomerID, Customers.name;

SELECT  Customers.country , COUNT(orders.customerid)
FROM  customers
LEFT JOIN orders
ON Customers.CustomerID=orders.CustomerID
GROUP BY customers.COUNTRY;

SELECT COUNTRY , COUNT(customerID) AS CustomerCount
FROM customers
GROUP BY country;

SELECT  Customers.country , SUM(orders.AMOUNT) AS TotalAmount
FROM  customers
LEFT JOIN orders
ON Customers.CustomerID=orders.CustomerID
GROUP BY customers.COUNTRY;

select * from customers;





