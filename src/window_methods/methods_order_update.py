import re
from tkinter import  Button, Toplevel, Text, BOTH, END, Label, Entry, DISABLED
from src.datatier import Datatier


data_tier = Datatier()


def update_order():
    update_window = Toplevel()
    update_window.title("Update Order")
    update_window.geometry("1000x900+100+100")
    update_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
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

    customer_id_label = Label(update_window, text="Order id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_label.pack(pady=(10, 0))
    customer_id_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    customer_id_entry.pack()

    status_label = Label(update_window, text="Status:", bg='gray10', fg="white", font=("Helvetica", 12))
    status_label.pack(pady=(10, 0))
    status_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    status_entry.pack()

    total_price_label = Label(update_window, text="Total Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    total_price_label.pack(pady=(10, 0))
    total_price_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    total_price_entry.pack()

    def update_order_in_database():
        customer_id = customer_id_entry.get()
        new_status = status_entry.get()
        new_total_price = total_price_entry.get()

        # Zkontrolovat, zda je ID zákazníka platné.
        customer_ids = [str(order['order_id']) for order in orders]
        if customer_id not in customer_ids:
            result_label.config(text="Invalid order ID.", fg='red')
            return

        # Zkontrolovat, zda je stav platný.
        if new_status not in ['Pending', 'Shipped', 'Delivered']:
            result_label.config(text="Invalid status.", fg='red')
            return

        # Zkontrolovat, zda je celková cena platná.
        if not re.match(r'^[1-9]\d*(\.\d+)?$', new_total_price):
            result_label.config(text="Invalid total price.", fg='red')
            return

        data_tier.update_order(new_status, new_total_price, customer_id)
        result_label.config(text="Order has been updated.", fg='green')

        customer_id_entry.delete(0, END)
        status_entry.delete(0, END)
        total_price_entry.delete(0, END)

    update_button = Button(update_window, text="Update Order", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_order_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))

def update_order_price():
    update_window = Toplevel()
    update_window.title("Update Order Price")
    update_window.geometry("1000x900+100+100")
    update_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
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

    customer_id_label = Label(update_window, text="Customer id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_label.pack()
    customer_id_entry = Entry(update_window)
    customer_id_entry.pack()

    total_price_label = Label(update_window, text="Total Price:", bg='gray10', fg="white", font=("Helvetica", 12))
    total_price_label.pack()
    total_price_entry = Entry(update_window)
    total_price_entry.pack()

    def update_order_in_database():
        customer_id = customer_id_entry.get()
        new_total_price = total_price_entry.get()

        customer_ids = [str(order['order_id']) for order in orders]
        if customer_id not in customer_ids:
            result_label.config(text="Invalid order ID.", fg='red')
            return

        if not re.match(r'^[1-9]\d*(\.\d+)?$', new_total_price):
            result_label.config(text="Invalid Total Price\n",fg="red")
            return

        # Vytvořit objekt objednávky a přidat ho do datové vrstvy.
        data_tier.update_order_price(new_total_price, customer_id)

        result_label.config(text="Order price updated successfully.\n",fg="green")

        customer_id_entry.delete(0, END)
        total_price_entry.delete(0, END)

    update_button = Button(update_window, text="Update Order", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_order_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_order_status():
    update_window = Toplevel()
    update_window.title("Update Order Status")
    update_window.geometry("1000x900+100+100")
    update_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
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

    customer_id_label = Label(update_window, text="Customer id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_label.pack()
    customer_id_entry = Entry(update_window)
    customer_id_entry.pack()

    status_label = Label(update_window, text="Status:", bg='gray10', fg="white", font=("Helvetica", 12))
    status_label.pack()
    status_entry = Entry(update_window)
    status_entry.pack()

    def update_order_in_database():
        customer_id = customer_id_entry.get()
        new_status = status_entry.get()

        customer_ids = [str(order['order_id']) for order in orders]
        if customer_id not in customer_ids:
            result_label.config(text="Invalid order ID.", fg='red')
            return
        if new_status == 'Pending' or new_status == 'Shipped' or new_status == 'Delivered':
            data_tier.update_order_status(new_status, customer_id)
            result_label.config(text="Order  status has been updated.", fg="green")
        else:
            result_label.config(text="Invalid status.", fg="red")

        customer_id_entry.delete(0, END)
        status_entry.delete(0, END)

    update_button = Button(update_window, text="Update Order status", command=update_order_in_database)
    update_button.pack(pady=10)

    result_label = Label(update_window, bg='gray10', fg="white")
    result_label.pack()