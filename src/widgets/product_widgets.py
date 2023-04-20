import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_products
from src.widgets import menu_widgets
from src.window_methods import methods_product_update


class Produc_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def product_widgets(self):
        product_window = Toplevel(self.master)
        product_window.title("Products")
        product_window.geometry("170x400+100+100")
        product_window.config(bg='gray10')
        product_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        select_product_button = Button(product_window, text="Show Product", command=methods_products.show_products,
                                       bg="#4a4a4a",
                                       fg="white", width=20, height=2)
        select_product_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        if self.role == "admin":
            add_product_button = Button(product_window, text="Add Product", command=methods_products.add_product,
                                        bg="#4a4a4a",
                                        fg="white")
            add_product_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            update_product_button = Button(product_window, text="Update Product",
                                           command=lambda: [product_window.destroy(), self.update_product_widgets()],
                                           bg="#4a4a4a",
                                           fg="white", width=20, height=2)
            update_product_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            delete_product_button = Button(product_window, text="Delete Product",
                                           command=methods_products.delete_product_window,
                                           bg="#4a4a4a", fg="white")
            delete_product_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

            import_product_button = Button(product_window, text="Import Products",
                                           command=methods_products.import_products,
                                           bg="#4a4a4a",
                                           fg="white", width=20, height=2)
            import_product_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        # Back button
        back_button = Button(product_window, text="Back",
                             command=lambda: [product_window.destroy(),
                                              menu_widgets.Menu_widget(self.master, self.role).menu_widgets()],
                             bg="#4a4a4a", fg="white")
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def update_product_widgets(self):
        update_product_window = Toplevel(self.master)
        update_product_window.title("Update Product")
        update_product_window.geometry("170x400+100+100")
        update_product_window.config(bg='gray10')
        update_product_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        update_product_all = Button(update_product_window, text="Update product",
                                    command=methods_product_update.update_product,
                                    bg="#4a4a4a",
                                    fg="white")
        update_product_all.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        update_product_description = Button(update_product_window, text="Update description",
                                            command=methods_product_update.update_product_description,
                                            bg="#4a4a4a",
                                            fg="white", width=20, height=2)
        update_product_description.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        update_product_price = Button(update_product_window, text="Update price",
                                      command=methods_product_update.update_product_price,
                                      bg="#4a4a4a",
                                      fg="white")
        update_product_price.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        back_button = Button(update_product_window, text="Back",
                             command=lambda: [update_product_window.destroy(), self.product_widgets()],
                             bg="#4a4a4a", fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell
