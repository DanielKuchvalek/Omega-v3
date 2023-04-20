import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_payment
from src.widgets import menu_widgets


class Payment_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def payment_widgets(self):
        payment_window = Toplevel(self.master)
        payment_window.title("Order Item")
        payment_window.geometry("170x400+100+100")
        payment_window.config(bg='gray10')
        payment_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        # Show Customers button
        order_item_button = Button(payment_window, text="Show Address",
                                   command=methods_payment.show_payment,
                                   bg="#4a4a4a",
                                   fg="white")
        order_item_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        if self.role == "admin":
            add_address_button = Button(payment_window, text="Add Payment",
                                        command=methods_payment.add_payment,
                                        bg="#4a4a4a", fg="white", width=20, height=2)
            add_address_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            update_review_button = Button(payment_window, text="Update Payment",
                                          command=lambda: [payment_window.destroy(),
                                                           self.update_payment_widgets()],
                                          bg="#4a4a4a", fg="white")
            update_review_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


            delete_customer_button = Button(payment_window, text="Delete payment",
                                            command=methods_payment.delete_payment_window, bg="#4a4a4a", fg="white",
                                            width=20,
                                            height=2)
            delete_customer_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(payment_window, text="Back",
                             command=lambda: [payment_window.destroy(),
                                              menu_widgets.Menu_widget(self.master, self.role).menu_widgets()],
                             bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def update_payment_widgets(self):
        update_payment_window = Toplevel(self.master)
        update_payment_window.title("Update Payment")
        update_payment_window.geometry("170x400+100+100")
        update_payment_window.config(bg='gray10')
        update_payment_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        update_number_button = Button(update_payment_window, text="Update card number",
                                        command=methods_payment.update_payment_card_number,
                                        bg="#4a4a4a",
                                        fg="white")
        update_number_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_card_cvv = Button(update_payment_window, text="Update card CVV",
                                       command=methods_payment.update_payment_card_cvv,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        update_card_cvv.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        back_button = Button(update_payment_window, text="Back",
                             command=lambda: [update_payment_window.destroy(), self.payment_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")








    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell
