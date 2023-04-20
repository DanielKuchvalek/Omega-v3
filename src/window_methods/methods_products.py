import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry, DISABLED
from src.datatier import Datatier
from src.model import Products

data_tier = Datatier()


def show_products():
    result_window = Toplevel()
    result_window.title("Products")
    result_window.geometry("900x600+100+100")
    result_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Product Name", "Price", "In Stock", "Category"]
    col_widths = [10, 30, 10, 10, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, product in enumerate(products, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, product['Product_name'], str(product['Products_price']) + "Kč", product['Products_in_stock'], product['Categories_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Products are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))



def add_product():
    add_window = Toplevel()
    add_window.title("Add Product")
    add_window.geometry("1200x950+50+50")
    add_window.configure(bg='gray10')

    categories = data_tier.get_category()
    result_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["Category id", "Category"]
    col_widths = [10, 35]
    header_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for category in categories:
        row_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [str(category['category_id']), category['Categories_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("left", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))
    # Vytvořit popisky a vstupní prvky pro informace o produktu

    product_name_label = Label(add_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_name_entry = Entry(add_window, font=("Helvetica", 12))
    product_name_label.pack(pady=2)
    product_name_entry.pack()

    description_label = Label(add_window, text="Description:", bg='gray10', fg="white", font=("Helvetica", 12))
    description_entry = Entry(add_window, font=("Helvetica", 12))
    description_label.pack(pady=2)
    description_entry.pack()

    price_label = Label(add_window, text="Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    price_entry = Entry(add_window, font=("Helvetica", 12))
    price_label.pack(pady=2)
    price_entry.pack()

    in_stock_label = Label(add_window, text="In Stock (Yes/No):", bg='gray10', fg="white", font=("Helvetica", 12))
    in_stock_entry = Entry(add_window, font=("Helvetica", 12))
    in_stock_label.pack(pady=2)
    in_stock_entry.pack()

    category_label = Label(add_window, text="Category:", bg='gray10', fg="white", font=("Helvetica", 12))
    category_entry = Entry(add_window, font=("Helvetica", 12))
    category_label.pack(pady=2)
    category_entry.pack()

    # Vytvořte funkci pro odeslání produktu.
    def submit_product():
        # Získejte informace o produktu z vstupních widgetů
        product_name = product_name_entry.get().strip()
        description = description_entry.get().strip()
        price = price_entry.get()
        in_stock = in_stock_entry.get()
        new_category = category_entry.get()

        # Zkontrolujte, zda je hodnota in_stock platná
        if in_stock not in ["Yes", "No"]:
            result_label.configure(text= "Invalid value for In Stock. Please enter either 'Yes' or 'No'.\n")
            return

        # Zkontrolujte, zda je hodnota ceny platná.
        if not re.match(r'^[1-9]\d*(\.\d+)?$', price):
            result_label.configure(text= "Invalid Price.\n")
            return

        # Zkontrolujte, zda jsou vyplněna pole pro název produktu a popis.
        if not product_name:
            result_label.configure(text= "Please enter a Product Name.\n", fg="red")
            return
        if not description:
            result_label.configure(text= "Please enter a Description.\n", fg="red")
            return

        category_ids = [str(category['category_id']) for category in categories]
        if new_category not in category_ids:
            result_label.config(text="Category ID not found.", fg="red")
            return
        # Vytvořte objekt produktů a přidejte ho do datové vrstvy
        product = Products(product_name, description, price, in_stock, new_category)
        data_tier.add_product(product)

        result_label.configure(text="Product added successfully.\n",fg="green")

    # Vytvořte tlačítko pro odeslání produktu.
    submit_button = Button(add_window, text="Submit", bg="#4a4a4a",
                           fg="white", command=submit_product, font=("Helvetica", 14))
    submit_button.pack(pady=2)

    # Vytvořte textový widget pro zobrazení výstupních zpráv.

    result_label = Label(add_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_label.pack(pady=10)





def delete_product_window():
    delete_window = Toplevel()
    delete_window.title("Products")
    delete_window.geometry("1200x600+100+100")
    delete_window.configure(bg='gray10')

    products = data_tier.get_product()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
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

    # Vytvoření popisku a vstupního pole pro zadání jména produktu
    name_label = Label(delete_window, text="Product Name:", bg='gray10', fg="white", font=("Helvetica", 14))
    name_label.pack()
    name_entry = Entry(delete_window, font=("Helvetica", 14))
    name_entry.pack()

    def delete_product_from_controller():
        # Získat název produktu z pole pro vstup
        name = name_entry.get()

        products = data_tier.get_product()
        valid_name = False
        for product in products:
            if product['Product_name'] == name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid product name.", fg="red")
            return

        # Odstranění produktu z controlleru.
        data_tier.delete_product(name)

        # Zobraz zprávu, která oznamuje, že produkt byl smazán.
        result_label.config(text="Product deleted successfully.", fg="green")

    # Vytvořit tlačítko pro smazání produktu.
    delete_button = Button(delete_window, text="Delete Product", command=delete_product_from_controller, bg="#4a4a4a",
                           fg="white", font=("Helvetica", 14))
    delete_button.pack()

    # Vytvořit popisek pro zobrazení výsledku odstranění produktu.
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def import_products():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_product_from_csv(filepath)
