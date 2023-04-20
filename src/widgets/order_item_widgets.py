import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_order_item
from src.widgets import menu_widgets


class Order_item_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)


    def order_item_widgets(self):
        order_item_window = Toplevel(self.master)
        order_item_window.title("Order Item")
        order_item_window.geometry("170x400+100+100")
        order_item_window.config(bg='gray10')
        order_item_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        # Show Customers button
        order_item_button = Button(order_item_window, text="Show Order items",
                                   command=methods_order_item.show_orders_items,
                                   bg="#4a4a4a",
                                   fg="white")
        order_item_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(order_item_window, text="Back",
                             command=lambda: [order_item_window.destroy(), menu_widgets.Menu_widget(self.master,self.role).menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell