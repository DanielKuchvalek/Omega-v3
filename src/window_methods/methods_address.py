import re
from tkinter import filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry, NSEW, Frame, BOTTOM, LEFT, RIGHT, Y, \
    TOP, DISABLED
from src.datatier import Datatier
from src.model import Addresses

data_tier = Datatier()


def show_address():
    result_window = Toplevel()
    result_window.title("Address")
    result_window.geometry("1450x600+100+100")
    result_window.configure(bg='gray10')

    addresses = data_tier.get_addresses()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "customer_id", "type", "name", "street", "city", "zip_code", "country"]
    col_widths = [10, 20, 20, 15, 15, 15, 20, 15]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
        *col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, address in enumerate(addresses, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
            *col_widths)
        row_values = [i, address['customer_id'], address['type'], address['name'], address['street'],
                      address['city'], address['zip_code'], address['country']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))
    result_label = Label(result_window, text="Addresses are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def delete_address_window():
    delete_window = Toplevel()
    delete_window.title("Delete Address")
    delete_window.geometry("1450x750+100+100")
    delete_window.configure(bg='gray10')

    addresses = data_tier.get_addresses()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "customer_id", "type", "name", "street", "city", "zip_code", "country"]
    col_widths = [10, 20, 20, 15, 15, 15, 20, 15]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
        *col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, address in enumerate(addresses, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
            *col_widths)
        row_values = [i, address['customer_id'], address['type'], address['name'], address['street'],
                      address['city'], address['zip_code'], address['country']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    address_id_label = Label(delete_window, text="Address id:", bg='gray10', fg="white", font=("Helvetica", 12))
    address_id_label.pack()
    address_id_entry = Entry(delete_window, font=("Helvetica", 14))
    address_id_entry.pack()

    def delete_address_from_controller():
        address_id = address_id_entry.get()

        address_ids = [str(address['address_id']) for address in addresses]
        if address_id not in address_ids:
            result_label.config(text="Address ID not found.", fg="red")
            return

        # Delete the order from the controller
        data_tier.delete_address(address_id)

        # Show a message indicating that the order was deleted
        result_label.config(text="Address deleted successfully.")

        address_id_entry.delete(0, END)

    # Create a button to delete the order
    delete_button = Button(delete_window, text="Delete Address", bg='gray10', fg="white",
                           command=delete_address_from_controller, font=("Helvetica", 12))
    delete_button.pack()

    # Create a label to display the result of deleting the order
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def add_address():
    add_window = Toplevel()
    add_window.title("Add Address")
    add_window.geometry("1450x1000+100+50")
    add_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    result_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Name"]
    col_widths = [10, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, customer in enumerate(customers, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}\n".format(*col_widths)
        row_values = [i, customer['name']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("left", justify="left")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    # Create input form
    input_frame = Frame(add_window, bg='gray10')
    input_frame.pack(side=BOTTOM, fill=Y, pady=2)

    customer_id_label = Label(input_frame, text="Customer id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_entry = Entry(input_frame, font=("Helvetica", 12))
    customer_id_label.pack(pady=2)
    customer_id_entry.pack()

    ptype_id_label = Label(input_frame, text="Type (Shipping/Billing):", bg='gray10', fg="white",
                           font=("Helvetica", 12))
    ptype_id_entry = Entry(input_frame, font=("Helvetica", 12))
    ptype_id_label.pack(pady=2)
    ptype_id_entry.pack()

    name_label = Label(input_frame, text="Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    name_entry = Entry(input_frame, font=("Helvetica", 12))
    name_label.pack(pady=2)
    name_entry.pack()

    street_label = Label(input_frame, text="Street:", bg='gray10', fg="white", font=("Helvetica", 12))
    street_entry = Entry(input_frame, font=("Helvetica", 12))
    street_label.pack(pady=2)
    street_entry.pack()

    city_label = Label(input_frame, text="City:", bg='gray10', fg="white", font=("Helvetica", 12))
    city_entry = Entry(input_frame, font=("Helvetica", 12))
    city_label.pack(pady=2)
    city_entry.pack()

    zip_code_label = Label(input_frame, text="Zip code:", bg='gray10', fg="white", font=("Helvetica", 12))
    zip_code_entry = Entry(input_frame, font=("Helvetica", 12))
    zip_code_label.pack(pady=2)
    zip_code_entry.pack()

    country_label = Label(input_frame, text="Country:", bg='gray10', fg="white", font=("Helvetica", 12))
    country_entry = Entry(input_frame, font=("Helvetica", 12))
    country_label.pack(pady=2)
    country_entry.pack()

    result_label = Label(input_frame, text="", bg='gray10', fg="white", font=("Helvetica", 12))
    result_label.pack(pady=2)

    # Create submit button
    def submit_review():
        customer_id = customer_id_entry.get()
        ptype = ptype_id_entry.get()
        name = name_entry.get()
        street = street_entry.get()
        city = city_entry.get()
        zip_code = zip_code_entry.get()
        country = country_entry.get()

        customer_ids = [str(customer['customer_id']) for customer in customers]
        if customer_id not in customer_ids:
            result_label.config(text="Customer ID not found.", fg="red")
            return
        if not ptype:
            result_label.configure(text="Please enter an address type.", fg="red")
            return

        if not name:
            result_label.configure(text="Please enter a name.", fg="red")
            return

        if not street:
            result_label.configure(text="Please enter a street.", fg="red")
            return

        if not city:
            result_label.configure(text="Please enter a city.", fg="red")
            return

        if not zip_code:
            result_label.configure(text="Please enter a zip code.", fg="red")
            return
        elif not zip_code.isdigit():
            result_label.configure(text="Please enter a valid zip code (numeric value).", fg="red")
            return

        if not country:
            result_label.configure(text="Please enter a country.", fg="red")
            return

        address = Addresses(customer_id, ptype, name, street, city, zip_code, country)
        data_tier.add_address(address)

        # Clear input fields
        customer_id_entry.delete(0, END)
        ptype_id_entry.delete(0, END)
        name_entry.delete(0, END)
        street_entry.delete(0, END)
        city_entry.delete(0, END)
        zip_code_entry.delete(0, END)
        country_entry.delete(0, END)

        # Display success message
        result_label.configure(text="Address added successfully.", fg="green")

    submit_button = Button(input_frame, text="Submit", bg="#4a4a4a",
                           fg="white", command=submit_review, font=("Helvetica", 14))
    submit_button.pack(pady=2,side=BOTTOM)


def update_address():
    update_window = Toplevel()
    update_window.title("Update Address")
    update_window.geometry("1450x900+100+100")
    update_window.configure(bg='gray10')


    addresses = data_tier.get_addresses()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "customer_id", "type", "name", "street", "city", "zip_code", "country"]
    col_widths = [10, 20, 20, 15, 15, 15, 20, 15]
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
        *col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, address in enumerate(addresses, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
            *col_widths)
        row_values = [i, address['customer_id'], address['type'], address['name'], address['street'],
                      address['city'], address['zip_code'], address['country']]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    customer_id_label = Label(update_window, text="Customer_id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_label.pack(pady=(10, 0))
    customer_id_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    customer_id_entry.pack()

    ptype_label = Label(update_window, text="Type:", bg='gray10', fg="white", font=("Helvetica", 12))
    ptype_label.pack(pady=(10, 0))
    ptype_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    ptype_entry.pack()

    city_label = Label(update_window, text="New City:", bg='gray10', fg="white", font=("Helvetica", 12))
    city_label.pack(pady=(10, 0))
    city_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    city_entry.pack()

    country_label = Label(update_window, text="New Country:", bg='gray10', fg="white", font=("Helvetica", 12))
    country_label.pack(pady=(10, 0))
    country_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    country_entry.pack()

    def update_address_in_database():
        customer_id = customer_id_entry.get()
        ptype = ptype_entry.get()
        new_city = city_entry.get()
        new_country = country_entry.get()

        customer_ids = [str(customer['customer_id']) for customer in addresses]
        if customer_id not in customer_ids:
            result_label.config(text="Customer ID not found.", fg="red")
            return
        if not customer_id or not ptype or not new_city or not new_country:
            result_label.config(text="Please fill in all fields.", fg="red")
        else:
            data_tier.update_address_city(new_city, new_country, int(customer_id), ptype)
            result_label.config(text="Address has been updated.", fg="green")

        # Clear input fields
        customer_id_entry.delete(0, END)
        ptype_entry.delete(0, END)
        city_entry.delete(0, END)
        country_entry.delete(0, END)

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))

    update_button = Button(update_window, text="Update Address", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_address_in_database)
    update_button.pack(pady=(20, 0))
