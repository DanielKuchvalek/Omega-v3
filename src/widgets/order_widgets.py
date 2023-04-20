import sys
from src.widgets.widget import Widget
from tkinter import Button, Toplevel
from src.window_methods import methods_orders
from src.widgets import menu_widgets
from src.window_methods import  methods_order_update


class Order_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def order_widgets(self):
        order_window = Toplevel(self.master)
        order_window.title("Orders")
        order_window.geometry("170x500+100+100")
        order_window.config(bg='gray10')
        order_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        select_order_button = Button(order_window, text="Show Order", command=methods_orders.show_orders, bg="#4a4a4a",
                                     fg="white")
        select_order_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        select_order_data = Button(order_window, text="Show Order Data", command=methods_orders.show_order_data,
                                   bg="#4a4a4a",
                                   fg="white", width=20, height=2)
        select_order_data.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        select_order_price_data = Button(order_window, text="Show Order Price",
                                         command=methods_orders.show_orders_price,
                                         bg="#4a4a4a",
                                         fg="white", width=20, height=2)
        select_order_price_data.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        if self.role == "admin":
            # Add Customers button
            add_order_button = Button(order_window, text="Add Order", command=methods_orders.add_order, bg="#4a4a4a",
                                      fg="white")
            add_order_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
            # Delete Customers button
            delete_order_button = Button(order_window, text="Delete Order", command=methods_orders.delete_order_window,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            delete_order_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
            # Update Customers button
            update_order_button = Button(order_window, text="Update Order",
                                         command=lambda: [order_window.destroy(), self.update_order_widgets()],
                                         bg="#4a4a4a",
                                         fg="white")
            update_order_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
            # Import Orders button
            import_orders_button = Button(order_window, text="Import Orders", command=methods_orders.import_orders,
                                          bg="#4a4a4a",
                                          fg="white", width=20, height=2)
            import_orders_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(order_window, text="Back", command=lambda: [order_window.destroy(),
                                                                         menu_widgets.Menu_widget(self.master,
                                                                                                  self.role).menu_widgets()],
                             bg="#4a4a4a", fg="white")
        back_button.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

    def update_order_widgets(self):
        update_order_window = Toplevel(self.master)
        update_order_window.title("Update Order")
        update_order_window.geometry("240x400+100+100")
        update_order_window.config(bg='gray10')
        update_order_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        update_customer_button = Button(update_order_window, text="Update Customer , Status, Price in Order",
                                        command=methods_order_update.update_order,
                                        bg="#4a4a4a",
                                        fg="white")
        update_customer_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_email = Button(update_order_window, text="Update Status",
                                       command=methods_order_update.update_order_status,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        update_customer_email.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_password = Button(update_order_window, text="Update total price",
                                          command=methods_order_update.update_order_price,
                                          bg="#4a4a4a",
                                          fg="white")
        update_customer_password.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        back_button = Button(update_order_window, text="Back",
                             command=lambda: [update_order_window.destroy(), self.order_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell
