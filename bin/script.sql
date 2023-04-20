use app1;
create user 'app1user'@'localhost' identified by 'Student1';
grant all on app1.* to app1user;
set autocommit =0;

start transaction;
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
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
    in_stock boolean NOT NULL,
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

commit;

start transaction;
insert into Customers(name,email,password,registration_date) values ('eduard','eduard@email.cz','eduard123','2022-11-22 00:00:00'), ('petr','petr@email.cz','petr123','2022-11-22 23:12:55'),('lukas','lukas@email.cz','lukas123','2023-1-21 21:36:59') ;
insert into Categories(name) values ('elektronika'),('kancelarske protreby'),('domaci potreby');
insert into Products(name,description,price,in_stock,category_id) values ('Tablet','Sed elit dui, pellentesque a, faucibus vel, interdum nec, diam. In dapibus augue non sapien. In sem justo, commodo ut, suscipit at, pharetra vitae, orci',12590,true,1),
																		 ('Zidle','Integer vulputate sem a nibh rutrum consequat. Integer tempor.',6590,true,2),
                                                                         ('Mixer','Duis pulvinar. Etiam dictum tincidunt diam.',3456,false,3);
insert into Orders(customer_id,order_date,status,total_price) values(1,'2023-1-28 20:45:34',1,12590),(2,'2023-1-27 12:23:54',2,6590),(3,'2023-1-26 21:43:34',3,3456);
insert into Order_items(order_id,product_id,quantity) values(1,1,2),(2,2,2),(3,3,3);
commit;


select Customers.name,order_date,status,total_price from Orders inner join Customers on Orders.customer_id = Customers.customer_id;
select * from Customers;
select * from Orders;



drop table Order_items;
drop table Orders;
drop table Products;
drop table Customers;
drop table Categories;

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





