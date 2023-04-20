import csv

from src.model import DBConnection
from src.model import Customer
from src.model import Order
from src.model import Products
from src.model import Category
from src.model import Order_items
from src.model import Review
from src.model import Addresses


class Datatier:
    def __init__(self):
        self.db = DBConnection()

    def add_customer(self, customer):
        customer.add_customer()

    def add_order(self, order):
        order.add_order()

    def add_product(self, products):
        products.add_product()

    def add_category(self, category):
        category.add_category()

    def add_order_item(self, order_item):
        order_item.add_order_items()

    def add_review(self, review):
        review.add_review()

    def add_address(self, address):
        address.add_address()

    def add_payment(self, payment):
        payment.add_payment()

    def get_order_item(self):
        query = "select Order_items.order_id, products.name, order_items.quantity " \
                "from Order_items inner join Products on Order_items.product_id = Products.product_id;"
        order_item = self.db.fetch_all(query)
        return [{'order_id': order_id, 'name': name, 'quantity': quantity} for order_id, name, quantity in order_item]

    def get_customers(self):
        query = "SELECT customer_id, name, email, password FROM Customers;"
        customers = self.db.fetch_all(query)
        return [{'customer_id': customer_id, 'name': name, 'email': email, 'password': password} for
                customer_id, name, email, password in customers]

    def get_customers_name(self):
        query = "SELECT customer_id, name from Customers;"
        customers = self.db.fetch_all(query)
        return [{'customer_id': customer_id, 'name': name} for customer_id, name in customers]

    def get_addresses(self):
        query = "SELECT address_id,customer_id, type, name, city, street,zip_code, country FROM Addresses;"
        result = self.db.fetch_all(query)
        return [{'address_id': address_id, 'customer_id': customer_id, 'type': ptype, 'name': name, 'city': city,
                 'street': street,
                 'zip_code': zip_code,
                 'country': country} for address_id, customer_id, ptype, name, city, street, zip_code, country in
                result]

    def get_order_final_price(self):
        query = "SELECT Products.name, Products.price * Order_items.quantity as final_price, Order_items.quantity " \
                "from Products inner join Order_items on Order_items.product_id = Products.product_id;"
        price = self.db.fetch_all(query)
        return [{'Products_name': pro_name, 'Final_price': final_price, 'Order_items_quantity': order_quantity} for
                pro_name, final_price, order_quantity in price]

    def get_category(self):
        query = "SELECT Categories.category_id, Categories.name FROM Categories;"
        categories = self.db.fetch_all(query)
        return [{'category_id': category_id, 'Categories_name': name} for category_id, name in categories]

    def get_orders(self):
        query = "SELECT order_id,Customers.name,order_date,status,total_price FROM Orders inner join Customers on Orders.customer_id = Customers.customer_id;"
        orders = self.db.fetch_all(query)
        return [{"order_id": order_id, "Customer_name": customer_name, "Order_date": order_date, "Status": status,
                 "Total_price": total_price}
                for order_id, customer_name, order_date, status, total_price in orders]

    def get_payment(self):
        query = "SELECT Payments.payment_id, Payments.order_id, Payments.payment_date, SUM(Order_items.quantity * " \
                "Products.price) AS final_price, Payments.payment_method FROM Payments JOIN Orders ON " \
                "Payments.order_id = Orders.order_id JOIN Order_items ON Orders.order_id = Order_items.order_id JOIN " \
                "Products ON Order_items.product_id = Products.product_id GROUP BY Payments.payment_id; "
        payment = self.db.fetch_all(query)
        return [
            {'payment_id': payment_id, 'order_id': order_id, 'payment_date': payment_date, 'final_price': final_price,
             'payment_method': payment_method} for payment_id, order_id, payment_date, final_price, payment_method in
            payment]

    def get_payment_number(self):
        query = "SELECT payment_id, order_id,payment_date,card_number,payment_method FROM Payments;"
        payment = self.db.fetch_all(query)
        return [
            {'payment_id': payment_id, 'order_id': order_id, 'payment_date': payment_date, 'card_number': card_number,
             'payment_method': payment_method} for payment_id, order_id, payment_date, card_number, payment_method in
            payment]

    def get_payment_cvv(self):
        query = "SELECT payment_id, order_id,payment_date,card_cvv,payment_method FROM Payments;"
        payment = self.db.fetch_all(query)
        return [
            {'payment_id': payment_id, 'order_id': order_id, 'payment_date': payment_date, 'card_cvv': card_cvv,
             'payment_method': payment_method} for payment_id, order_id, payment_date, card_cvv, payment_method in
            payment]

    def get_orders_name(self):
        query = "SELECT DISTINCT Customers.name from Orders inner join Customers on Orders.customer_id = Customers.customer_id;"
        orders_name = self.db.fetch_all(query)
        return [{"Customer_name": customer_name} for customer_name in orders_name]

    def get_product(self):
        query = "SELECT Products.name, Products.description, Products.price, Products.in_stock, Categories.name AS category_name " \
                "FROM Products INNER JOIN Categories ON Products.category_id = Categories.category_id;"
        product = self.db.fetch_all(query)
        return [{'Product_name': name, 'Products_description': description, 'Products_price': price,
                 'Products_in_stock': in_stock, 'Categories_name': category_name} for
                name, description, price, in_stock, category_name in product]

    def get_product_no_description(self):
        query = "SELECT Products.name, Products.price, Products.in_stock, Categories.name AS category_name " \
                "FROM Products INNER JOIN Categories ON Products.category_id = Categories.category_id;"
        product = self.db.fetch_all(query)
        return [{'Product_name': name, 'Products_price': price, 'Products_in_stock': in_stock,
                 'Categories_name': category_name} for name, price, in_stock, category_name in product]

    def get_product_name(self):
        query = "SELECT Product_id,Products.name FROM Products;"
        products = self.db.fetch_all(query)
        return [{'product_id': product_id, 'name': name} for product_id, name in products]

    def get_review(self):
        query = "SELECT Reviews.review_id, Reviews.customer_id, Products.name, Reviews.rating, Reviews.comment, " \
                "Reviews.review_date, Customers.name AS customer_name FROM Reviews RIGHT JOIN Customers ON " \
                "Reviews.customer_id = Customers.customer_id INNER JOIN Products ON Reviews.product_id = " \
                "Products.product_id; "
        review = self.db.fetch_all(query)
        return [{'review_id': review_id, 'customer_id': customer_id, 'product_id': product_id, 'rating': rating,
                 'comment': comment, 'review_date': review_date, 'customer_name': customer_name}
                for review_id, customer_id, product_id, rating, comment, review_date, customer_name in review]

    def delete_order(self, customer_name):
        query = "DELETE from Orders WHERE customer_id=(SELECT customer_id from Customers WHERE Customers.name=%s);"
        params = (customer_name,)
        self.db.execute(query, params)

    def delete_customer(self, customer_name):
        query = "DELETE from Customers WHERE Customers.name = %s;"
        params = (customer_name,)
        self.db.execute(query, params)

    def delete_product(self, product_name):
        query = "DELETE from Products WHERE Products.name = %s;"
        params = (product_name,)
        self.db.execute(query, params)

    def delete_review(self, review_name):
        query = "DELETE from Reviews WHERE Reviews.review_id = %s;"
        params = (review_name,)
        self.db.execute(query, params)

    def delete_category(self, category_name):
        query = "DELETE from Categories WHERE Categories.name = %s;"
        params = (category_name,)
        self.db.execute(query, params)

    def delete_address(self, address_id):
        query = "DELETE from Addresses WHERE Addresses.address_id = %s;"
        params = (address_id,)
        self.db.execute(query, params)

    def delete_payment(self, payment_id):
        query = "DELETE from Payments WHERE Payments.payment_id = %s;"
        params = (payment_id,)
        self.db.execute(query, params)

    def update_order(self, new_status, new_total_price, customer_id):
        query = "UPDATE Orders SET status=%s, total_price=%s WHERE Orders.order_id = %s;"
        params = (new_status, new_total_price, customer_id)
        self.db.execute(query, params)

    def update_order_status(self, new_status, customer_id):
        query = "UPDATE Orders SET status=%s WHERE Orders.order_id = %s;"
        params = (new_status, customer_id)
        self.db.execute(query, params)

    def update_order_price(self, new_total_price, customer_id):
        query = "UPDATE Orders SET total_price=%s WHERE Orders.order_id = %s;"
        params = (new_total_price, customer_id)
        self.db.execute(query, params)

    def update_payment(self, new_card_number, payment_id):
        query = "UPDATE Payments SET Payments.card_number = %s WHERE payment_id = %s;"
        params = (new_card_number, payment_id)
        self.db.execute(query, params)

    def update_payment_cvv(self, new_card_cvv, payment_id):
        query = "UPDATE Payments SET Payments.card_cvv = %s WHERE payment_id = %s;"
        params = (new_card_cvv, payment_id)
        self.db.execute(query, params)

    def update_customers(self, new_email, new_password, customers_name):
        queue = "UPDATE Customers SET email=%s, password=%s WHERE Customers.name = %s;"
        params = (new_email, new_password, customers_name)
        self.db.execute(queue, params)

    def update_customers_email(self, new_email, customer_name):
        queue = "UPDATE Customers SET email= %s WHERE Customers.name = %s;"
        params = (new_email, customer_name)
        self.db.execute(queue, params)

    def update_customers_password(self, new_password, customer_name):
        queue = "UPDATE Customers SET password= %s WHERE Customers.name = %s;"
        params = (new_password, customer_name)
        self.db.execute(queue, params)

    def update_product(self, new_price, new_stock, product_id):
        queue = "UPDATE Products SET price = %s, in_stock = %s WHERE Products.name = %s;"
        params = (new_price, new_stock, product_id)
        self.db.execute(queue, params)

    def update_product_description(self, new_description, product_id):
        queue = "UPDATE Products SET description = %s WHERE Products.name = %s;"
        params = (new_description, product_id)
        self.db.execute(queue, params)

    def update_product_price(self, new_price, product_id):
        queue = "UPDATE Products SET price = %s WHERE Products.name = %s;"
        params = (new_price, product_id)
        self.db.execute(queue, params)

    def update_category_name(self, new_name, customer_id):
        query = "UPDATE Categories SET name=%s WHERE Categories.name = %s;"
        params = (new_name, customer_id)
        self.db.execute(query, params)

    def update_review_rating_comment(self, new_rating, new_comment, review_id):
        query = "UPDATE Reviews SET rating = %s, comment = %s WHERE review_id = %s;"
        params = (new_rating, new_comment, review_id)
        self.db.execute(query, params)

    def update_address_city(self, new_city, new_country, customer_id, ptype):
        query = "UPDATE Addresses SET city = %s, country = %s WHERE customer_id = %s AND type = %s;"
        params = (new_city, new_country, customer_id, ptype)
        self.db.execute(query, params)

    def get_order_data(self):
        query = """
        SELECT Orders.order_id AS order_id, Customers.name AS customer_name, 
        Products.name AS product_name, Order_items.quantity AS order_amount
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.customer_id
        JOIN Order_items ON Orders.order_id = Order_items.order_id
        JOIN Products ON Order_items.product_id = Products.product_id;
        """
        order_data = self.db.fetch_all(query)
        return [{"order": order, "customer_name": customer_name,
                 "product_name": product_name, "product_amount": product_amount}
                for order, customer_name, product_name, product_amount in order_data]

    def import_customers_from_csv(self, path):
        with open(path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                print(row)
                customer = Customer(row[0], row[1], row[2])
                self.add_customer(customer)

    def import_order_from_csv(self, path):
        with open(path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                print(row)
                order = Order(row[0], row[1], row[2])
                print(order)
                self.add_order(order)

    def import_product_from_csv(self, path):
        with open(path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                print(row)
                product = Products(row[0], row[1], row[2], row[3], row[4])
                print(product)
                self.add_product(product)

    def import_category_from_csv(self, path):
        with open(path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                print(row)
                category = Category(row[0])
                print(category)
                self.add_category(category)
