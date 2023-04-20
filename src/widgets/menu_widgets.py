from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_reviews
from src.window_methods import methods_address
from src.widgets import customer_widgets
from src.widgets.order_widgets import Order_widget
from src.widgets.product_widgets import Produc_widget
from src.widgets.category_widgets import Category_widget
from src.widgets.order_item_widgets import Order_item_widget
from src.widgets.review_widgets import Review_widget
from src.widgets.address_widgets import Address_widget
from src.widgets.payment_widgets import Payment_widget
import sys


class Menu_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def menu_widgets(self):
        button_frame = Toplevel(self.master)
        button_frame.title("Menu")
        button_frame.configure(bg="gray10")
        button_frame.geometry("170x550+100+100")
        button_frame.protocol('WM_DELETE_WINDOW', self.quit_app)

        customers_button = Button(button_frame, text="Customers",
                                  command=lambda: [button_frame.destroy(),
                                                   customer_widgets.Cust_widget(self.master,
                                                                                self.role).customers_widgets()],
                                  bg="#4a4a4a",
                                  fg="white", width=20, height=2)
        customers_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        orders_button = Button(button_frame, text="Orders",
                               command=lambda: [button_frame.destroy(),
                                                Order_widget(self.master, self.role).order_widgets()],
                               bg="#4a4a4a",
                               fg="white")
        orders_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        product_button = Button(button_frame, text="Products",
                                command=lambda: [button_frame.destroy(),
                                                 Produc_widget(self.master, self.role).product_widgets()],
                                bg="#4a4a4a",
                                fg="white", width=20, height=2)
        product_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        category_button = Button(button_frame, text="Category",
                                 command=lambda: [button_frame.destroy(),
                                                  Category_widget(self.master, self.role).category_widgets()],
                                 bg="#4a4a4a",
                                 fg="white")
        category_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        order_item_button = Button(button_frame, text="Order item",
                                   command=lambda: [button_frame.destroy(),
                                                    Order_item_widget(self.master, self.role).order_item_widgets()],
                                   bg="#4a4a4a",
                                   fg="white", width=20, height=2)
        order_item_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        review_button = Button(button_frame, text="Review",
                               command=lambda: [button_frame.destroy(),
                                                Review_widget(self.master, self.role).review_widgets()],
                               bg="#4a4a4a",
                               fg="white")
        review_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        address_button = Button(button_frame, text="Adreess",
                                command=lambda: [button_frame.destroy(),
                                                 Address_widget(self.master, self.role).address_widgets()],
                                bg="#4a4a4a",
                                fg="white", width=20, height=2)
        address_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

        payment_button = Button(button_frame, text="Payment",
                                command=lambda: [button_frame.destroy(),
                                                 Payment_widget(self.master, self.role).payment_widgets()],
                                bg="#4a4a4a",
                                fg="white", width=20, height=2)
        payment_button.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

        quit_button = Button(button_frame, text="Quit",
                             command=self.quit_app,
                             bg="#4a4a4a",
                             fg="white")
        quit_button.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell
