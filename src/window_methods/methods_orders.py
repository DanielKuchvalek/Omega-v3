import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry,DISABLED
from src.datatier import Datatier
from src.model import Order

data_tier = Datatier()


def show_orders_name():
    result_window = Toplevel()
    result_window.title("Orders by Customer Name")
    result_window.geometry("1200x600+100+100")
    result_window.configure(bg='gray10')

    orders = data_tier.get_orders_name()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Customer Name"]
    col_widths = [10, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    result_text.insert(END, "-" * sum(col_widths) + "\n")

    for i, order in enumerate(orders, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, order['Customer_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Orders by Customer Name are shown.", bg='gray10', fg="white",
                         font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))



def show_orders():
    result_window = Toplevel()
    result_window.title("Orders")
    result_window.geometry("1100x600+100+100")
    result_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Customer name", "Order date", "Status", "Total price"]
    col_widths = [10, 30, 20, 20, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, order in enumerate(orders, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        order_date = order['Order_date'].strftime('%Y-%m-%d')
        row_values = [i, order['Customer_name'], order_date, order['Status'], str(order['Total_price']) + " Kč"]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Orders are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=10)


def show_orders_price():
    result_window = Toplevel()
    result_window.title("Orders Price")
    result_window.geometry("850x600+100+100")
    result_window.configure(bg='gray10')

    orders = data_tier.get_order_final_price()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Product name", "Final price", "Quantity"]
    col_widths = [10, 30, 20, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, order in enumerate(orders, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, order['Products_name'], str(order['Final_price']) + " Kč", str(order['Order_items_quantity'])]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Orders final price are shown.", bg='gray10', fg="white",
                         font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))



def add_order():
    add_window = Toplevel()
    add_window.title("Add Order")
    add_window.geometry("700x800+100+100")
    add_window.configure(bg='gray10')

    customers = data_tier.get_customers_name()
    result_text = Text(add_window, fg='white', bg='gray10', height=20)
    result_text.pack()

    headers = ["Customer id","Name"]
    col_widths = [10, 55]
    header_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for customer in customers:
        row_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [str(customer['customer_id']), str(customer['name'])]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("left", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    # Vytvořit popisky a vstupní widgety pro informace o objednávce
    customer_id_label = Label(add_window, text="Customer ID:", bg='gray10', fg='white')
    customer_id_entry = Entry(add_window)
    customer_id_label.pack()
    customer_id_entry.pack()

    status_label = Label(add_window, text="Status(Shipped, Delivered, Pending):", bg='gray10', fg='white')
    status_entry = Entry(add_window)
    status_label.pack()
    status_entry.pack()

    total_price_label = Label(add_window, text="Total Price:", bg='gray10', fg='white')
    total_price_entry = Entry(add_window)
    total_price_label.pack()
    total_price_entry.pack()

    # Vytvořit funkci pro odeslání objednávky
    def submit_order():
        # Získat informace o objednávce z vstupních widgetů
        customer_id = customer_id_entry.get()
        status = status_entry.get()
        total_price = total_price_entry.get()

        # Zkontrolovat, zda je ID zákazníka platné
        customer_ids = [str(customer['customer_id']) for customer in customers]
        if customer_id not in customer_ids:
            result_label.config(text="Invalid customer ID.", fg="red")
            return

        # Zkontrolovat, zda je stav platný
        if status not in ['Pending', 'Shipped', 'Delivered']:
            result_label.config(text="You have to add Pending, Shipped or Delivered\n", fg="red")
            return

        # Zkontrolovat, zda je celková cena platná
        if not re.match(r'^[1-9]\d*(\.\d+)?$', total_price):
            result_label.config(text="Invalid price.", fg="red")
            return

        # Vytvořit objekt objednávky a přidat ho do datové vrstvy
        order = Order(customer_id, status, total_price)
        data_tier.add_order(order)

        result_label.config(text="Order added.", fg="green")

        customer_id_entry.delete(0, END)
        status_entry.delete(0, END)
        total_price_entry.delete(0, END)

    # Vytvořit tlačítko pro odeslání objednávky
    submit_button = Button(add_window, text="Submit", command=submit_order)
    submit_button.pack(pady=10)

    # Vytvořit textový widget pro zobrazení výstupních zpráv
    result_label = Label(add_window, bg='gray10', fg="white")
    result_label.pack()


def delete_order_window():
    # Vytvoření nového okna pro smazani objednavky
    delete_window = Toplevel()
    delete_window.title("Delete Order")
    delete_window.geometry("1200x600+100+100")
    delete_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Customer name", "Order date", "Status", "Total price"]
    col_widths = [10, 30, 20, 20, 20]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, order in enumerate(orders, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        order_date = order['Order_date'].strftime('%Y-%m-%d')
        row_values = [i, order['Customer_name'], order_date, order['Status'], str(order['Total_price']) + " Kč"]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    name_label = Label(delete_window, text="Customer Name:", bg='gray10', fg='white')
    name_label.pack()
    name_entry = Entry(delete_window)
    name_entry.pack()

    def delete_order_from_controller():
        # Získat jméno zákazníka z vstupního pole
        name = name_entry.get()

        # Zkontrolovat, zda je jméno zákazníka platné.
        customer_names = [customer['name'] for customer in data_tier.get_customers()]
        if name not in customer_names:
            result_label.config(text="Invalid customer name.", fg='red')
            return

        # Smazat objednávku z řadiče.
        data_tier.delete_order(name)

        # Zobrazit zprávu oznamující, že objednávka byla smazána.
        result_label.config(text="Order deleted successfully.", fg='green')

        name_entry.delete(0, END)

    # Vytvořit tlačítko pro smazání objednávky.
    delete_button = Button(delete_window, text="Delete Order", command=delete_order_from_controller)
    delete_button.pack()

    # Vytvořit popisek pro zobrazení výsledku smazání objednávky.
    result_label = Label(delete_window, bg='gray10', fg='white')
    result_label.pack()

def show_order_data():
    result_window = Toplevel()
    result_window.title("Order Data")
    result_window.geometry("950x600+100+100")
    result_window.configure(bg='gray10')

    orders = data_tier.get_order_data()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Order", "Customer Name", "Product name", "Amount"]
    col_widths = [10, 15, 25, 25, 10]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, order in enumerate(orders, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, order['order'], order['customer_name'], order['product_name'], order['product_amount']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Order Data is shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def import_orders():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_order_from_csv(filepath)
