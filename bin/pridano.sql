use app1;
create user 'app1user'@'localhost' identified by 'Student1';
grant all on app1.* to app1user;
set autocommit =0;

start transaction;
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)  unique NOT NULL
);

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    registration_date DATETIME NOT NULL
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    in_stock ENUM('Yes','No') NOT NULL,
    category_id int not null,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) on delete cascade
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    status ENUM('Pending','Shipped','Delivered') NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) on delete cascade
);

CREATE TABLE Order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)on delete cascade,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)on delete cascade
);

CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    review_date DATETIME NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

CREATE TABLE Addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    type ENUM('Shipping', 'Billing') NOT NULL,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    zip_code VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE Payments (
payment_id INT AUTO_INCREMENT PRIMARY KEY,
order_id INT NOT NULL,
payment_date DATETIME NOT NULL,
amount DECIMAL(10,2) NOT NULL,
payment_method ENUM('Credit Card', 'Debit Card', 'PayPal') NOT NULL,
card_number VARCHAR(16),
card_expiration VARCHAR(22),
card_cvv VARCHAR(4),
FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE
);

CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(50),
  PRIMARY KEY (id)
);
commit;

select * from users;

start transaction;
insert into Customers(name,email,password,registration_date) values ('eduard','eduard@email.cz','eduard123','2022-11-22 00:00:00'), ('petr','petr@email.cz','petr123','2022-11-22 23:12:55'),('lukas','lukas@email.cz','lukas123','2023-1-21 21:36:59') ;
insert into Categories(name) values ('elektronika'),('kancelarske protreby'),('domaci potreby');
insert into Products(name,description,price,in_stock,category_id) values ('Tablet','Sed elit dui, pellentesque a, faucibus vel, interdum nec, diam. In dapibus augue non sapien. In sem justo, commodo ut, suscipit at, pharetra vitae, orci',12590,1,1),
																		 ('Zidle','Integer vulputate sem a nibh rutrum consequat. Integer tempor.',6590,2,2),
                                                                         ('Mixer','Duis pulvinar. Etiam dictum tincidunt diam.',3456,1,3);
insert into Orders(customer_id,order_date,status,total_price) values(1,'2023-1-28 20:45:34',1,12590),(2,'2023-1-27 12:23:54',2,6590),(3,'2023-1-26 21:43:34',3,3456);
insert into Order_items(order_id,product_id,quantity) values(1,1,2),(2,2,2),(3,3,3);
insert into Customers(name,email,password,registration_date) values ('buzerant','buzerant@email.cz','buzerant123','2022-11-22 00:00:00');
INSERT INTO Reviews (customer_id, product_id, rating, comment, review_date) VALUES (1, 2, 4, 'This product is great!', '2023-04-11 10:00:00');
INSERT INTO Addresses (customer_id, type, name, street, city, zip_code, country) VALUES (1, 'Shipping', 'John Doe', '123 Main St', 'Anytown','12345', 'USA');

INSERT INTO Payments (order_id, payment_date, amount, payment_method, card_number, card_expiration, card_cvv) VALUES (1, NOW(), 150.00, 'Credit Card', '1234 5678 9012 3456', '12/24', '123');
INSERT INTO users (username, password, role) VALUES
('admin', 'a', 'admin'),
('user1', 'secret123', 'user'),
('user2', 'password', 'user');

commit;

SELECT payment_id, order_id,payment_date,card_number,payment_method  FROM Payments;


SELECT Payments.payment_id, Payments.order_id, Payments.payment_date, SUM(Order_items.quantity * Products.price) AS final_price, Payments.payment_method
FROM Payments
JOIN Orders ON Payments.order_id = Orders.order_id
JOIN Order_items ON Orders.order_id = Order_items.order_id
JOIN Products ON Order_items.product_id = Products.product_id
GROUP BY Payments.payment_id;




select Customers.name,order_date,status,total_price from Orders inner join Customers on Orders.customer_id = Customers.customer_id;
select * from Customers;
select * from Orders;
select name, email, password from Customers;
/*potreba pridat*/
SELECT Reviews.review_id, Reviews.customer_id, Products.name, Reviews.rating, Reviews.comment, Reviews.review_date, Customers.name AS customer_name
FROM Reviews
RIGHT JOIN Customers ON Reviews.customer_id = Customers.customer_id
INNER JOIN Products ON Reviews.product_id = Products.product_id;


/*potreba pridat*/
SELECT customer_id,type,name,city, zip_code,country
FROM Addresses 
WHERE customer_id = 1 AND type = 'Shipping';


/*potreba pridat*/
select name FROM categories;
UPDATE Categories SET name="domovina" WHERE Categories.name = "domaci potreby";

/*potreba pridat*/
UPDATE Addresses
SET city = 'New York', state = 'NY'
WHERE customer_id = 1 AND type = 'Billing' AND name = 'Jane Doe';

/*potreba pridat*/
UPDATE Reviews
SET rating = 5, comment = 'This product exceeded my expectations!'
WHERE review_id = 1;

drop table Payments;
drop table Reviews;
drop table Addresses;
drop table Order_items;
drop table Orders;
drop table Products;
drop table Customers;
drop table Categories;
drop view current_stock;
drop view recent_orders;

CREATE VIEW Current_stock AS
SELECT Products.product_id, Products.name, Products.price, Products.in_stock
FROM Products;


select * from Current_stock;

CREATE VIEW Recent_orders AS
SELECT Orders.order_id, Customers.name, Orders.order_date, Orders.status, Orders.total_price
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
ORDER BY Orders.order_date DESC
LIMIT 10;


select * from Recent_orders;


/*select objednavka, zakaznik jmeno,nazev produktu, pocek kolik jich bylo nakoupeno.*/
SELECT Orders.order_id AS objednavka, Customers.name AS zakaznik_jmeno, Products.name AS nazev_produktu, Order_items.quantity AS pocek_kolik_jich_bylo_nakoupeno
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
JOIN Order_items ON Orders.order_id = Order_items.order_id
JOIN Products ON Order_items.product_id = Products.product_id;

SELECT Orders.order_id AS order_name, Customers.name AS customer_name, 
        Products.name AS product_name, Order_items.quantity AS order_amount
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.customer_id
        JOIN Order_items ON Orders.order_id = Order_items.order_id
        JOIN Products ON Order_items.product_id = Products.product_id;
        
UPDATE Customers SET email='blazen@post.cz', password=121241 WHERE Customers.name = 'eduard';
UPDATE Customers SET email='blazen@post.cz', password=121241 WHERE Customers.name = 'eduard';

SELECT Products.name, Products.description, Products.price, Products.in_stock, Categories.name AS category_name
FROM Products
INNER JOIN Categories ON Products.category_id = Categories.category_id;


UPDATE Orders SET customer_id=3 WHERE Orders.order_id = 3

select Order_items.order_id, products.name, order_items.quantity
from Order_items inner join Products on Order_items.product_id = Products.product_id;

create view seznam_objednavek_produktu as
select Products.name, Products.price * Order_items.quantity as final_price, Order_items.quantity
from Products inner join Order_items on Order_items.product_id = Products.product_id;

SELECT Customers.name, Orders.order_date, Orders.status, Products.price * Order_items.quantity as final_price
FROM Orders
INNER JOIN Customers ON Orders.customer_id = Customers.customer_id
INNER JOIN Order_items ON Orders.order_id = Order_items.order_id
INNER JOIN Products ON Order_items.product_id = Products.product_id;

select * from seznam_objednavek_produktu;

drop view seznam_objednavek_produktu;

