import re
from tkinter import Frame, filedialog, Button, Toplevel, Text, BOTH, END, Label, Entry, ttk,DISABLED
from src.datatier import Datatier
from src.model import Category

data_tier = Datatier()


def show_category():
    result_window = Toplevel()
    result_window.title("Category")
    result_window.geometry("400x600+100+100")
    result_window.configure(bg='gray10')

    categories = data_tier.get_category()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Category"]
    col_widths = [10, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, category in enumerate(categories, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, str(category['Categories_name'])]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    result_label = Label(result_window, text="Categories are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))



def add_category():
    add_window = Toplevel()
    add_window.title("Add Category")
    add_window.geometry("1200x800+100+100")
    add_window.configure(bg='gray10')

    category_name_label = Label(add_window, text="Category Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    category_name_entry = Entry(add_window, font=("Helvetica", 12))
    category_name_label.pack(pady=10)
    category_name_entry.pack()

    def submit_category():
        category_name = category_name_entry.get()

        if category_name.strip() == "":
            # Display error message and prevent category from being added
            output_text.insert(END, "Error: Category name cannot be blank.\n")
        else:
            category = Category(category_name)
            data_tier.add_category(category)
            category_name_entry.delete(0, END)
            output_text.insert(END, "Category added successfully.\n")

    submit_button = Button(add_window, text="Submit", bg="#4a4a4a",
                           fg="white", command=submit_category, font=("Helvetica", 14))
    submit_button.pack(pady=10)

    output_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 12))
    output_text.pack(fill=BOTH, expand=True)

    result_label = Label(add_window, text="Add Category", bg='gray10', fg="white", font=("Helvetica", 16))
    result_label.pack(pady=(10, 0))


def update_category():
    update_window = Toplevel()
    update_window.title("Update Category")
    update_window.geometry("1200x750+100+100")
    update_window.configure(bg='gray10')

    categories = data_tier.get_category()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Category"]
    col_widths = [10, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, category in enumerate(categories, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, str(category['Categories_name'])]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    category_name_label = Label(update_window, text="Category Name:", bg='gray10', fg="white", font=("Helvetica", 12))
    category_name_label.pack(pady=(10, 0))
    category_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    category_name_entry.pack()
    new_category_name_label = Label(update_window, text="New Category name:", bg='gray10', fg="white",
                                    font=("Helvetica", 12))
    new_category_name_label.pack(pady=(10, 0))
    new_category_name_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    new_category_name_entry.pack()

    def update_products_in_database():
        category_name = category_name_entry.get()
        new_category_name = new_category_name_entry.get()

        categories = data_tier.get_category()
        valid_name = False
        for name in categories:
            if name['Categories_name'] == category_name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid Category name.",fg="red")
            return

        data_tier.update_category_name(new_category_name, category_name)
        result_label.config(text="Category has been updated.",fg="green")

        category_name_entry.delete(0, END)
        new_category_name_entry.delete(0, END)

    update_button = Button(update_window, text="Update Category", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def delete_category_window():
    delete_window = Toplevel()
    delete_window.title("Category")
    delete_window.geometry("1200x600+100+100")
    delete_window.configure(bg='gray10')

    categories = data_tier.get_category()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    headers = ["No.", "Category"]
    col_widths = [10, 30]
    header_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    for i, category in enumerate(categories, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}\n\n".format(*col_widths)
        row_values = [i, str(category['Categories_name'])]
        result_text.insert(END, row_fmt.format(*row_values))

    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))


    name_label = Label(delete_window, text="Category Name:", bg='gray10', fg="white", font=("Helvetica", 14))
    name_label.pack()
    name_entry = Entry(delete_window, font=("Helvetica", 14))
    name_entry.pack()

    def delete_category_from_controller():
        name = name_entry.get()

        categories = data_tier.get_category()
        valid_name = False
        for name in categories:
            if name['Categories_name'] == name:
                valid_name = True
                break
        if not valid_name:
            result_label.config(text="Invalid Category name.", fg="red")
            return

        data_tier.delete_category(name)

        result_label.config(text="Category deleted successfully.")

    # Create a button to delete the order
    delete_button = Button(delete_window, text="Delete category", command=delete_category_from_controller, bg="#4a4a4a",
                           fg="white", font=("Helvetica", 14))
    delete_button.pack()

    # Create a label to display the result of deleting the order
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def import_category():
    filetypes = [('CSV files', '*.csv'), ('All files', '*.*')]
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        data_tier.import_category_from_csv(filepath)
