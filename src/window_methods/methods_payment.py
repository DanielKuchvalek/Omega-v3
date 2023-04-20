import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry, DISABLED, TOP, Frame, BOTTOM, Y
from src.datatier import Datatier
from src.model import Payments

data_tier = Datatier()


def show_payment():
    result_window = Toplevel()
    result_window.title("Payment")
    result_window.geometry("1050x600+100+100")
    result_window.configure(bg='gray10')

    payments = data_tier.get_payment()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Payment ID", "Order ID", "Payment Date", "Final Price", "Payment Method"]
    col_widths = [10, 20, 20, 15, 15, 15]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, payment in enumerate(payments, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        payment_date = payment['payment_date'].strftime('%Y-%m-%d')
        row_values = [i, str(payment['payment_id']), str(payment['order_id']), payment_date,
                      str(payment['final_price']) + "Kč", payment['payment_method']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))
    result_label = Label(result_window, text="Payments are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def delete_payment_window():
    delete_window = Toplevel()
    delete_window.title("Delete payment")
    delete_window.geometry("1200x750+100+100")
    delete_window.configure(bg='gray10')

    payments = data_tier.get_payment()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Payment ID", "Order ID", "Payment Date", "Final Price", "Payment Method"]
    col_widths = [10, 20, 20, 15, 15, 15]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, payment in enumerate(payments, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        payment_date = payment['payment_date'].strftime('%Y-%m-%d')
        row_values = [i, str(payment['payment_id']), str(payment['order_id']), payment_date,
                      str(payment['final_price']) + "Kč", payment['payment_method']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    payment_id_label = Label(delete_window, text="Payment id:", bg='gray10', fg="white", font=("Helvetica", 12))
    payment_id_label.pack()
    payment_id_entry = Entry(delete_window, font=("Helvetica", 14))
    payment_id_entry.pack()

    def delete_payment_from_controller():
        # Získat ID platby z vstupního pole
        payment_id = payment_id_entry.get()

        # Zkontrolovat, zda ID platby existuje
        payment_ids = [str(payment['payment_id']) for payment in payments]
        if payment_id not in payment_ids:
            result_label.config(text="Payment ID not found.",fg="red")
            return

        # Smazat platbu z řadiče
        data_tier.delete_payment(payment_id)

        # Zobrazit zprávu oznamující, že platba byla smazána
        result_label.config(text="Payment deleted successfully.", fg="green")

    # Vytvořit tlačítko pro smazání platby
    delete_button = Button(delete_window, text="Delete Payment", bg='gray10', fg="white",
                           command=delete_payment_from_controller, font=("Helvetica", 12))
    delete_button.pack()

    # Vytvořit popisek pro zobrazení výsledku smazání platby
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def add_payment():
    add_window = Toplevel()
    add_window.title("Add Payment")
    add_window.geometry("1200x800+100+100")
    add_window.configure(bg='gray10')

    orders = data_tier.get_orders()
    result_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 12))
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

    # Vytvořit formulář pro zadání vstupů
    input_frame = Frame(add_window, bg='gray10')
    input_frame.pack(side=BOTTOM, fill=Y, pady=5)

    order_id_label = Label(input_frame, text="Order id:", bg='gray10', fg="white", font=("Helvetica", 12))
    order_id_entry = Entry(input_frame, font=("Helvetica", 12))
    order_id_label.pack(pady=5)
    order_id_entry.pack()

    payment_methods_label = Label(input_frame, text="Payment method(Credit Card, Debit Card, PayPal)", bg='gray10',
                                  fg="white", font=("Helvetica", 12))
    payment_methods_entry = Entry(input_frame, font=("Helvetica", 12))
    payment_methods_label.pack(pady=5)
    payment_methods_entry.pack()

    card_number_label = Label(input_frame, text="Card number:", bg='gray10', fg="white", font=("Helvetica", 12))
    card_number_entry = Entry(input_frame, font=("Helvetica", 12))
    card_number_label.pack(pady=5)
    card_number_entry.pack()

    card_expiration_label = Label(input_frame, text="Card expiration(MM/RR):", bg='gray10', fg="white", font=("Helvetica", 12))
    card_expiration_entry = Entry(input_frame, font=("Helvetica", 12))
    card_expiration_label.pack(pady=5)
    card_expiration_entry.pack()

    card_cvv_label = Label(input_frame, text="Card cvv:", bg='gray10', fg="white", font=("Helvetica", 12))
    card_cvv_entry = Entry(input_frame, font=("Helvetica", 12))
    card_cvv_label.pack(pady=5)
    card_cvv_entry.pack()

    result_label = Label(input_frame, text="", bg='gray10', fg="white", font=("Helvetica", 12))
    result_label.pack(pady=5)

    # Vytvořit tlačítko pro odeslání formuláře
    def submit_payment():
        order_id = order_id_entry.get()
        payment_method = payment_methods_entry.get()
        card_number = card_number_entry.get()
        card_expiration = card_expiration_entry.get()
        card_cvv = card_cvv_entry.get()

        order_ids = [str(order['order_id']) for order in orders]
        if order_id not in order_ids:
            result_label.config(text="Payment ID not found.",fg="red")
            return

        if payment_method not in ['Credit Card', 'Debit Card', 'PayPal']:
            result_label.configure(text="Invalid payment method.", fg="red")
            return

        card_number_pattern = re.compile(r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$')
        if not card_number_pattern.match(card_number):
            result_label.configure(text="Please enter a valid card number.", fg="red")
            return

        if not re.match(r"^\d{2}/\d{2}$", card_expiration):
            result_label.configure(text="Please enter a valid card expiration date (MM/YY format).", fg="red")
            return

        if not card_cvv:
            result_label.configure(text="Please enter a card CVV.", fg="red")
            return
        elif not card_cvv.isdigit() or len(card_cvv) != 3:
            result_label.configure(text="Invalid CVV. Please enter a 3-digit number.", fg="red")
            return

        payment = Payments(order_id, payment_method, card_number, card_expiration, card_cvv)
        data_tier.add_payment(payment)

        # Vyčistit vstupní pole
        order_id_entry.delete(0, END)
        payment_methods_entry.delete(0, END)
        card_number_entry.delete(0, END)
        card_expiration_entry.delete(0, END)
        card_cvv_entry.delete(0, END)

        # Zobrazit úspěšnou zprávu
        result_label.configure(text="Payment added successfully.", fg="green")

    submit_button = Button(input_frame, text="Submit", font=("Helvetica", 12), command=submit_payment)
    submit_button.pack(pady=5)


def update_payment_card_number():
    update_window = Toplevel()
    update_window.title("Update Payment")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    payments = data_tier.get_payment_number()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Payment ID", "Order ID", "Card Number", "Payment Method"]
    col_widths = [5, 25, 25, 25, 25]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, payment in enumerate(payments, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, str(payment['payment_id']), str(payment['order_id']),
                      str(payment['card_number']),
                      payment['payment_method']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    payment_id_label = Label(update_window, text="Payment_id:", bg='gray10', fg="white", font=("Helvetica", 12))
    payment_id_label.pack(pady=(10, 0))
    payment_id_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    payment_id_entry.pack()

    card_number_label = Label(update_window, text="Card number:", bg='gray10', fg="white", font=("Helvetica", 12))
    card_number_label.pack(pady=(10, 0))
    card_number_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    card_number_entry.pack()

    def update_address_in_database():
        payment_id = payment_id_entry.get()
        new_number = card_number_entry.get()

        payment_ids = [str(payment['payment_id']) for payment in payments]
        if payment_id not in payment_ids:
            result_label.config(text="Payment ID not found.",fg="red")
            return
        card_number_pattern = re.compile(r'^\d{4}\s\d{4}\s\d{4}\s\d{4}$')
        if not card_number_pattern.match(new_number):
            result_label.configure(text="Please enter a valid card number.", fg="red")
            return
        else:
            data_tier.update_payment(new_number, payment_id)
            result_label.config(text="Payment has been updated.", fg="green")

            # Vyčistit vstupní pole
            payment_id_entry.delete(0, END)
            card_number_entry.delete(0, END)

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))

    update_button = Button(update_window, text="Update Payment", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_address_in_database)
    update_button.pack(pady=(20, 0))


def update_payment_card_cvv():
    update_window = Toplevel()
    update_window.title("Update Payment Card CVV")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    payments = data_tier.get_payment_cvv()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Payment ID", "Order ID", "Card CVV", "Payment Method"]
    col_widths = [5, 25, 15, 25, 25]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, payment in enumerate(payments, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, str(payment['payment_id']), str(payment['order_id']),
                      str(payment['card_cvv']),
                      payment['payment_method']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    payment_id_label = Label(update_window, text="Payment_id:", bg='gray10', fg="white", font=("Helvetica", 12))
    payment_id_label.pack(pady=(10, 0))
    payment_id_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    payment_id_entry.pack()

    card_cvv_label = Label(update_window, text="Card cvv:", bg='gray10', fg="white", font=("Helvetica", 12))
    card_cvv_label.pack(pady=(10, 0))
    card_cvv_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    card_cvv_entry.pack()

    def update_cvv_in_database():
        payment_id = payment_id_entry.get()
        card_cvv = card_cvv_entry.get()

        if not payment_id or not card_cvv:
            result_label.config(text="Please fill in all fields.", fg="red")

        payment_ids = [str(payment['payment_id']) for payment in payments]
        if payment_id not in payment_ids:
            result_label.config(text="Payment ID not found.", fg="red")
            return
        if not card_cvv:
            result_label.configure(text="Please enter a card CVV.", fg="red")
            return
        elif not card_cvv.isdigit() or len(card_cvv) != 3:
            result_label.configure(text="Invalid CVV. Please enter a 3-digit number.", fg="red")
            return
        else:
            data_tier.update_payment_cvv(card_cvv, payment_id)
            result_label.config(text="Payment has been updated.", fg="green")

        # Vyčistit vstupní pole
        payment_id_entry.delete(0, END)
        card_cvv_entry.delete(0, END)

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))

    update_button = Button(update_window, text="Update Payment", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_cvv_in_database)
    update_button.pack(pady=(20, 0))
