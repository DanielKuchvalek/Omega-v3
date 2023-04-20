import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry, DISABLED
from src.datatier import Datatier
from src.model import Customer
import hashlib

data_tier = Datatier()


def show_customers():
    result_window = Toplevel()
    result_window.title("Customers")
    result_window.geometry("1200x600+100+100")
    result_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Name", "Email", "Password"]
    col_widths = [10, 30, 50, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, customer in enumerate(customers, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, customer['name'], customer['email'], customer['password']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Customers are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=10)


def add_customer():
    add_window = Toplevel()
    add_window.title("Add Customer")
    add_window.geometry("400x300+100+100")
    add_window.configure(bg='gray10')

    name_label = Label(add_window, text="Name:", bg='gray10', fg="white")
    name_label.pack()
    name_entry = Entry(add_window)
    name_entry.pack()

    email_label = Label(add_window, text="Email:", bg='gray10', fg="white")
    email_label.pack()
    email_entry = Entry(add_window)
    email_entry.pack()

    password_label = Label(add_window, text="Password:", bg='gray10', fg="white")
    password_label.pack()
    password_entry = Entry(add_window, show="*")
    password_entry.pack()

    def add_customer_to_database():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        # Validate the email using a regular expression
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, email):
            result_label.config(text="Invalid email address.")
            return

        # Validate password format (at least one digit and one letter, minimum length 8)
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            result_label.config(text="Invalid password format. At least one digit and one letter, minimum length 8")
            return

        # Validate customer name format (only letters and spaces)
        name_regex = r"^[A-Za-z\s]+$"
        if not re.match(name_regex, name):
            result_label.config(text="Invalid name.")
            return

        passbytes = bytes(password, 'UTF-8')
        alg = hashlib.sha512()
        alg.update(passbytes)

        customer = Customer(name, email, alg.hexdigest())
        data_tier.add_customer(customer)

        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

        result_label.config(text="Customer added.")

    add_button = Button(add_window, text="Add Customer", command=add_customer_to_database)
    add_button.pack(pady=10)

    result_label = Label(add_window, bg='gray10', fg="white")
    result_label.pack()

def delete_customer_window():
    delete_window = Toplevel()
    delete_window.title("Delete Customer")
    delete_window.geometry("600x800+100+100")
    delete_window.configure(bg='gray10')

    customers = data_tier.get_customers_name()
    delete_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    delete_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Name"]
    col_widths = [10, 50]
    header_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
    delete_text.insert(END, header_fmt.format(*headers))

    for i, customer in enumerate(customers, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, customer['name'][0]]
        delete_text.insert(END, row_fmt.format(*row_values))

    delete_text.tag_configure("center", justify="center")
    delete_text.tag_add("center", "1.0", "end")
    delete_text.config(state=DISABLED)
    delete_text.configure(font=("Courier New", 12))
    result_label = Label(delete_window, text="Select a customer to delete:", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=10)

    name_label = Label(delete_window, text="Customer Name:", bg='gray10', fg="white")
    name_label.pack()
    name_entry = Entry(delete_window)
    name_entry.pack()

    def delete_customer_from_controller():
        # Get the customer name from the entry field
        name = name_entry.get()

        customers = data_tier.get_customers()
        valid_name = False
        for customer in customers:
            if customer['name'] == name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid customer name.")
            return
        # Delete the customer from the database
        data_tier.delete_customer(name)

        # Show a message indicating that the customer was deleted
        result_label.config(text="Customer deleted successfully.")

        name_entry.delete(0, END)

    delete_button = Button(delete_window, text="Delete Customer", command=delete_customer_from_controller)
    delete_button.pack(pady=10)

    result_label = Label(delete_window, bg='gray10', fg="white")
    result_label.pack()

def update_customers():
    update_window = Toplevel()
    update_window.title("Update Customers")
    update_window.geometry("1200x900+100+100")
    update_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    update_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    update_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Name", "Email", "Password"]
    col_widths = [10, 30, 50, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    update_text.insert(END, header_fmt.format(*headers))

    for i, customer in enumerate(customers, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, customer['name'], customer['email'], customer['password']]
        update_text.insert(END, row_fmt.format(*row_values))

    update_text.tag_configure("center", justify="center")
    update_text.tag_add("center", "1.0", "end")
    update_text.config(state=DISABLED)
    update_text.configure(font=("Courier New", 12))

    result_label = Label(update_window, text="Select a customer to update:", bg='gray10', fg="white",
                         font=("Helvetica", 14))
    result_label.pack(pady=10)

    customer_name_label = Label(update_window, text="Customer name:", bg='gray10', fg="white")
    customer_name_label.pack(pady=(10, 0))
    customer_name_entry = Entry(update_window)
    customer_name_entry.pack()

    email_label = Label(update_window, text=" New Email:", bg='gray10', fg="white")
    email_label.pack(pady=(10, 0))
    email_entry = Entry(update_window)
    email_entry.pack()

    password_label = Label(update_window, text="New Password:", bg='gray10', fg="white")
    password_label.pack(pady=(10, 0))
    password_entry = Entry(update_window)
    password_entry.pack()

    def update_customer_in_database():
        new_email = email_entry.get()
        new_password = password_entry.get()
        customer_name = customer_name_entry.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            result_label.config(text="Invalid email format.")
            return

        # Validate password format (at least one digit and one letter, minimum length 8)
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", new_password):
            result_label.config(text="Invalid password format. At least one digit and one letter, minimum length 8")
            return

        # Check if the customer name entered by the user matches one of the names in the database
        customers = data_tier.get_customers()
        valid_name = False
        for customer in customers:
            if customer['name'] == customer_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid customer name.")
            return

        # Update the customer's email and password in the database
        data_tier.update_customers(new_email, new_password, customer_name)
        result_label.config(text="Customer has been updated.")

        email_entry.delete(0, END)
        password_entry.delete(0,END)

    update_button = Button(update_window, text="Update Customers email", command=update_customer_in_database)
    update_button.pack(pady=10)

    result_label = Label(update_window, bg='gray10', fg="white")
    result_label.pack()


def update_customers_email():
    update_window = Toplevel()
    update_window.title("Update Customers email")
    update_window.geometry("1200x850+100+100")
    update_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    update_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    update_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Name", "Email", "Password"]
    col_widths = [10, 30, 50, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    update_text.insert(END, header_fmt.format(*headers))

    for i, customer in enumerate(customers, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, customer['name'], customer['email'], customer['password']]
        update_text.insert(END, row_fmt.format(*row_values))

    update_text.tag_configure("center", justify="center")
    update_text.tag_add("center", "1.0", "end")
    update_text.config(state=DISABLED)
    update_text.configure(font=("Courier New", 12))
    result_label = Label(update_window, text="Select a customer to update:", bg='gray10', fg="white",
                         font=("Helvetica", 14))
    result_label.pack(pady=10)

    customer_name_label = Label(update_window, text="Customer name:", bg='gray10', fg="white")
    customer_name_label.pack(pady=(10, 0))
    customer_name_entry = Entry(update_window)
    customer_name_entry.pack()

    email_label = Label(update_window, text=" New Email:", bg='gray10', fg="white")
    email_label.pack(pady=(10, 0))
    email_entry = Entry(update_window)
    email_entry.pack()

    def update_customer_in_database():
        new_email = email_entry.get()
        customer_name = customer_name_entry.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            result_label.config(text="Invalid email format.")
            return

        # Check if the customer name entered by the user matches one of the names in the database
        customers = data_tier.get_customers()
        valid_name = False
        for customer in customers:
            if customer['name'] == customer_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid customer name.")
            return

        data_tier.update_customers_email(new_email, customer_name)
        result_label.config(text="Customers email has been updated.")

        email_entry.delete(0, END)
        customer_name_entry.delete(0, END)

    update_button = Button(update_window, text="Update Customers email",command=update_customer_in_database)
    update_button.pack(pady=10)

    result_label = Label(update_window, bg='gray10', fg="white")
    result_label.pack()


def update_customers_password():
    update_window = Toplevel()
    update_window.title("Update Customers password")
    update_window.geometry("1200x850+100+100")
    update_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    update_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    update_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Name", "Email", "Password"]
    col_widths = [10, 30, 50, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
    update_text.insert(END, header_fmt.format(*headers))

    for i, customer in enumerate(customers, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, customer['name'], customer['email'], customer['password']]
        update_text.insert(END, row_fmt.format(*row_values))

    update_text.tag_configure("center", justify="center")
    update_text.tag_add("center", "1.0", "end")
    update_text.config(state=DISABLED)
    update_text.configure(font=("Courier New", 12))
    result_label = Label(update_window, text="Select a customer to update:", bg='gray10', fg="white",
                         font=("Helvetica", 14))
    result_label.pack(pady=10)

    customer_name_label = Label(update_window, text="Customer name:", bg='gray10', fg="white")
    customer_name_label.pack(pady=(10, 0))
    customer_name_entry = Entry(update_window)
    customer_name_entry.pack()

    password_label = Label(update_window, text="New Password:", bg='gray10', fg="white")
    password_label.pack(pady=(10, 0))
    password_entry = Entry(update_window)
    password_entry.pack()

    def update_customer_in_database():

        new_password = password_entry.get()
        customer_name = customer_name_entry.get()

        # Validate password format (at least one digit and one letter, minimum length 8)
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", new_password):
            result_label.config(text="Invalid password format. At least one digit and one letter, minimum length 8")
            return

        # Check if the customer name entered by the user matches one of the names in the database
        customers = data_tier.get_customers()
        valid_name = False
        for customer in customers:
            if customer['name'] == customer_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid customer name.")
            return

        data_tier.update_customers_password(new_password, customer_name)
        result_label.config(text="Customers password has been updated.")

        password_entry.delete(0, END)
        customer_name_entry.delete(0, END)

    update_button = Button(update_window, text="Update Customers password", command=update_customer_in_database)
    update_button.pack(pady=10)

    result_label = Label(update_window,bg='gray10', fg="white")
    result_label.pack()


def import_customers():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_customers_from_csv(filepath)
