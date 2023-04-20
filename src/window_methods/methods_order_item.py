import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry,DISABLED
from src.datatier import Datatier
from src.model import Order_items

data_tier = Datatier()


def show_orders_items():
    result_window = Toplevel()
    result_window.title("Orders items")
    result_window.geometry("950x600+100+100")
    result_window.configure(bg='gray10')

    orders = data_tier.get_order_item()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Order ID", "Product Name", "Quantity"]
    col_widths = [10, 35, 30, 10]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    cislo = 0
    for order in orders:
        cislo += 1
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [cislo, order['order_id'], order['name'], order['quantity']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Orders items are shown.", bg='gray10', fg="white",
                         font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))

