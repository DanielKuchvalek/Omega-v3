import re
from tkinter import Button, Toplevel, Text, BOTH, END, Label, Entry, DISABLED
from src.datatier import Datatier

data_tier = Datatier()

def update_product():
    update_window = Toplevel()
    update_window.title("Update Product")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Product Name", "Price", "In Stock", "Category"]
    col_widths = [10, 30, 10, 10, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, product in enumerate(products, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, product['Product_name'], str(product['Products_price']) + "Kč", product['Products_in_stock'],
                      product['Categories_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    product_name_label = Label(update_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_label.pack(pady=(10, 0))
    product_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    product_name_entry.pack()
    price_label = Label(update_window, text="New Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    price_label.pack(pady=(10, 0))
    price_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    price_entry.pack()

    in_stock_label = Label(update_window, text="Update Stock:", bg='gray10', fg="white", font=("Helvetica", 12))
    in_stock_label.pack(pady=(10, 0))
    in_stock_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    in_stock_entry.pack()

    def update_products_in_database():
        # Získání informací o produktu z vstupních prvků.
        product_name = product_name_entry.get().strip()
        new_price = price_entry.get()
        in_stock = in_stock_entry.get()

        # V kontrole přidej kontrolu, zda název produktu již existuje v databázi.
        products = data_tier.get_product()
        valid_name = False
        for product in products:
            if product['Product_name'] == product_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid product name.",fg="red")
            return

        # Kontrolujte, zda je hodnota ceny platná.
        if not re.match(r'^[1-9]\d*(\.\d+)?$', new_price):
            result_label.configure(text="Invalid Price.\n",fg="red")
            return

        # Zkontroluje, zda je hodnota in_stock platná.id
        if in_stock not in ["Yes", "No"]:
            result_label.configure(text="Invalid value for In Stock. Please enter either 'Yes' or 'No'.\n",fg="red")
            return

        # Aktualizuje produkt v databázi.
        data_tier.update_product(new_price, in_stock, product_name)

        result_label.configure(text="Product has been updated.",fg="green")

    update_button = Button(update_window, text="Update Product", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_product_description():
    update_window = Toplevel()
    update_window.title("Update Product Description")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Product Name", "Price", "In Stock", "Category"]
    col_widths = [10, 30, 10, 10, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, product in enumerate(products, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, product['Product_name'], str(product['Products_price']) + "Kč", product['Products_in_stock'],
                      product['Categories_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    product_name_label = Label(update_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_label.pack(pady=(10, 0))
    product_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    product_name_entry.pack()

    description_label = Label(update_window, text="New Description:", bg='gray10', fg="white", font=("Helvetica", 12))
    description_label.pack(pady=(10, 0))
    description_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    description_entry.pack()

    def update_products_in_database():
        product_name = product_name_entry.get()
        new_description = description_entry.get()

        products = data_tier.get_product()
        valid_name = False
        for product in products:
            if product['Product_name'] == product_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid product name.", fg="red")
            return

        data_tier.update_product_description(new_description, product_name)
        result_label.config(text="Product has been updated.")

    update_button = Button(update_window, text="Update Product", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_product_price():
    update_window = Toplevel()
    update_window.title("Update Product Price")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Product Name", "Price", "In Stock", "Category"]
    col_widths = [10, 30, 10, 10, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, product in enumerate(products, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, product['Product_name'], str(product['Products_price']) + "Kč", product['Products_in_stock'],
                      product['Categories_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    product_name_label = Label(update_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_label.pack(pady=(10, 0))
    product_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    product_name_entry.pack()

    price_label = Label(update_window, text="New Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    price_label.pack(pady=(10, 0))
    price_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    price_entry.pack()

    def update_products_in_database():
        product_name = product_name_entry.get()
        new_price = price_entry.get()

        products = data_tier.get_product()
        valid_name = False
        for product in products:
            if product['Product_name'] == product_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid product name.", fg="red")
            return

        if not re.match(r'^[1-9]\d*(\.\d+)?$', new_price):
            result_label.configure(text="Invalid Price.\n",fg="red")
            return

        data_tier.update_product_price(new_price, product_name)
        result_label.config(text="Product has been updated.",fg="green")

    update_button = Button(update_window, text="Update Product", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))