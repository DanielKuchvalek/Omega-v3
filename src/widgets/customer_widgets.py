import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_customer
from src.widgets import menu_widgets

class Cust_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master,role)

    def customers_widgets(self):
        customers_window = Toplevel(self.master)
        customers_window.title("Customers")
        customers_window.geometry("170x400+100+100")
        customers_window.config(bg='gray10')
        customers_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        # Show Customers button
        customers_button = Button(customers_window, text="Show Customers", command=methods_customer.show_customers,
                                  bg="#4a4a4a",
                                  fg="white")
        customers_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        if self.role == "admin":
            # Add Customers button
            add_customer_button = Button(customers_window, text="Add Customers", command=methods_customer.add_customer,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_customer_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            # Update Customers button
            update_customer_button = Button(customers_window, text="Update Customers",
                                            command=lambda: [customers_window.destroy(),
                                                             self.update_customer_widgets()],
                                            bg="#4a4a4a", fg="white")
            update_customer_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            # Delete Customers button
            delete_customer_button = Button(customers_window, text="Delete Customers",
                                            command=methods_customer.delete_customer_window, bg="#4a4a4a", fg="white",
                                            width=20,
                                            height=2)
            delete_customer_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

            # Import Customers button
            import_customer_button = Button(customers_window, text="Import Customers",
                                            command=methods_customer.import_customers,
                                            bg="#4a4a4a", fg="white")
            import_customer_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(customers_window, text="Back",
                             command=lambda: [customers_window.destroy(), menu_widgets.Menu_widget(self.master,self.role).menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")


    def update_customer_widgets(self):
        update_customer_window = Toplevel(self.master)
        update_customer_window.title("Update Customer")
        update_customer_window.geometry("170x400+100+100")
        update_customer_window.config(bg='gray10')
        update_customer_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        update_customer_button = Button(update_customer_window, text="Update Email and Password",
                                        command=methods_customer.update_customers,
                                        bg="#4a4a4a",
                                        fg="white")
        update_customer_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_email = Button(update_customer_window, text="Update Email",
                                       command=methods_customer.update_customers_email,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        update_customer_email.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_customer_password = Button(update_customer_window, text="Update Password",
                                          command=methods_customer.update_customers_password,
                                          bg="#4a4a4a",
                                          fg="white")
        update_customer_password.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        back_button = Button(update_customer_window, text="Back",
                             command=lambda: [update_customer_window.destroy(), self.customers_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell