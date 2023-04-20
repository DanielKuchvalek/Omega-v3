import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_address
from src.widgets import menu_widgets


class Address_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def address_widgets(self):
        address_window = Toplevel(self.master)
        address_window.title("Order Item")
        address_window.geometry("170x400+100+100")
        address_window.config(bg='gray10')
        address_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        # Show Customers button
        order_item_button = Button(address_window, text="Show Address",
                                   command=methods_address.show_address,
                                   bg="#4a4a4a",
                                   fg="white")
        order_item_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        if self.role == "admin":
            add_category_button = Button(address_window, text="Add Address",
                                         command=methods_address.add_address,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_category_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            update_review_button = Button(address_window, text="Update Address",
                                          command=methods_address.update_address,
                                          bg="#4a4a4a", fg="white")
            update_review_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            delete_customer_button = Button(address_window, text="Delete Address",
                                            command=methods_address.delete_address_window, bg="#4a4a4a", fg="white",
                                            width=20,
                                            height=2)
            delete_customer_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(address_window, text="Back",
                             command=lambda: [address_window.destroy(), menu_widgets.Menu_widget(self.master,self.role).menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell