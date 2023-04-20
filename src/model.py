
from tkinter import messagebox
import mysql.connector
import configparser

class DBConnection:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf/conf.ini')
        try:
            self.cnx = mysql.connector.connect(user=config['database']['user'], password=config['database']['password'],
                                                host=config['database']['host'], database=config['database']['database'])
        except mysql.connector.Error as err:
            if err.errno == 2003:
                messagebox.showerror("Error", "Can't connect to MySQL server on 'localhost:3306' (10061)")
                raise ConnectionError("Can't connect to MySQL server on 'localhost:3306' (10061)")
            else:
                raise err

    # Funkce execute vykonává dotaz na databázi a případně s parametry, uloží změny
    def execute(self, query, params=None):
        cursor = self.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == 2003:
                messagebox.showerror("Error", "Can't connect to MySQL server on 'localhost:3306' (10061)")
                raise ConnectionError("Can't connect to MySQL server on 'localhost:3306' (10061)")
            else:
                raise err
        finally:
            cursor.close()

    # fetch_all vrátí výsledky všech řádků z databáze po provedení dotazu
    def fetch_all(self, query, params=None):
        cursor = self.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            list = []
            for values in cursor:
                list.append(values)
            return list
        except mysql.connector.Error as err:
            if err.errno == 2003:
                messagebox.showerror("Error", "Can't connect to MySQL server on 'localhost:3306' (10061)")
                raise ConnectionError("Can't connect to MySQL server on 'localhost:3306' (10061)")
            else:
                raise err
        finally:
            cursor.close()

    def cursor(self):
        return self.cnx.cursor()

    def close(self):
        self.cnx.close()


class Category:
    def __init__(self, name):
        self.name = name
        self.db = DBConnection()

    def add_category(self):
        query = "INSERT INTO Categories(name) VALUES (%s)"
        params = (self.name,)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'name': self.name,

        }


class Order:
    def __init__(self, customer_id, status, total_price):
        self.customer_id = customer_id
        self.status = status
        self.total_price = total_price
        self.objednavka = None
        self.customer_name = None
        self.db = DBConnection()

    def add_order(self):
        query = "INSERT INTO Orders(customer_id, status, total_price,order_date) VALUES (%s, %s, %s,NOW())"
        params = (self.customer_id, self.status, self.total_price)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'status': self.status,
            'total_price': self.total_price
        }


class Customer:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.db = DBConnection()

    def add_customer(self):
        query = "INSERT INTO Customers(name, email, password, registration_date) VALUES (%s, %s, %s, NOW())"
        params = (self.name, self.email, self.password)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }


class Products:
    def __init__(self, name, description, price, in_stock, category):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock
        self.category = category
        self.db = DBConnection()

    def add_product(self):
        query = "INSERT INTO Products(name, description, price, in_stock,category_id) VALUES (%s, %s, %s, %s, %s)"
        params = (self.name, self.description, self.price, self.in_stock, self.category)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'in_stock': self.in_stock,
            'category': self.category
        }


class Order_items:
    def __init__(self, order, product, quantity):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.db = DBConnection()

    def add_order_items(self):
        query = "INSERT INTO Order_items(order_id, product_id, quantity) VALUES (%s, %s, %s)"
        params = (self.order, self.product, self.quantity)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'order': self.order,
            'product': self.product,
            'quantity': self.quantity,
        }


class Review:
    def __init__(self, customer, product, rating, comment):
        self.customer = customer
        self.product = product
        self.rating = rating
        self.comment = comment
        self.db = DBConnection()

    def add_review(self):
        query = "INSERT INTO Reviews (customer_id, product_id, rating, comment, review_date) VALUES (%s,%s,%s,%s,NOW())"
        params = (self.customer, self.product, self.rating, self.comment)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'customer': self.customer,
            'product': self.product,
            'rating': self.rating,
            'comment': self.comment,

        }


class Addresses:
    def __init__(self, customer, ptype, name, street, city, zip_code, county):
        self.customer = customer
        self.ptype = ptype
        self.name = name
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = county
        self.db = DBConnection()

    def add_address(self):
        query = "INSERT INTO Addresses (customer_id, type, name, street, city, zip_code, country) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        params = (self.customer, self.ptype, self.name, self.street, self.city, self.zip_code, self.country)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'customer': self.customer,
            'type': self.ptype,
            'name': self.name,
            'street': self.street,
            'city': self.city,
            'zip code': self.zip_code,
            'country': self.country

        }


class Payments:
    def __init__(self, order, payment_method, card_number, card_expiration, card_cvv):
        self.order = order
        self.payment_method = payment_method
        self.card_number = card_number
        self.card_expiration = card_expiration
        self.card_cvv = card_cvv
        self.db = DBConnection()

    def add_payment(self):
        query = "INSERT INTO Payments (order_id, payment_date, amount, payment_method, card_number, card_expiration, card_cvv) VALUES (%s,NOW(),0,%s,%s,%s,%s);"
        params = (
            self.order, self.payment_method, self.card_number, self.card_expiration,
            self.card_cvv)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'order': self.order,
            'payment_method': self.payment_method,
            'card_number': self.card_number,
            'card_expiration': self.card_expiration,
            'card_cvv': self.card_cvv

        }
