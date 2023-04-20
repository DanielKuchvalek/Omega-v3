import re
from tkinter import Button, Toplevel, Text, BOTH, END, Label, Entry, Frame, BOTTOM, DISABLED, Y, TOP
from src.datatier import Datatier
from src.model import Review

data_tier = Datatier()


def show_review():
    #Displays a window containing a list of reviews from the database.
    result_window = Toplevel()
    result_window.title("Review")
    result_window.geometry("1450x600+100+100")
    result_window.configure(bg='gray10')

    reviews = data_tier.get_review()
    result_text = Text(result_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    # Definujte záhlaví a šířky sloupců výstupní tabulky.
    headers = ["No.", "Review ID", "Customer ID", "Product id", "Rating", "Comment", "Review Date", "Customer Name"]
    col_widths = [10, 25, 15, 15, 10, 25, 15, 15]

    # Formátování řádku hlavičky a vložení jejího textu do textového pole
    header_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
        *col_widths)
    result_text.insert(END, header_fmt.format(*headers))

    # Formátovat každý řádek výstupní tabulky a vložit jej do textového pole
    for i, review in enumerate(reviews, start=1):
        row_fmt = "{{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}  {{:<{}}}\n\n".format(
            *col_widths)
        review_date = review['review_date'].strftime('%Y-%m-%d')
        row_values = [i, review['review_id'], review['customer_id'], review['product_id'], review['rating'],
                      review['comment'], review_date, review['customer_name']]
        result_text.insert(END, row_fmt.format(*row_values))

    # Centrovat výstupní tabulku v textovém poli.
    result_text.tag_configure("center", justify="center")
    result_text.tag_add("center", "1.0", "end")

    # Vypni editaci textového pole a nastav písmo.
    result_text.config(state=DISABLED)
    result_text.configure(font=("Courier New", 12))

    # Zobrazit zprávu, která oznamuje, že jsou zobrazeny recenze.
    result_label = Label(result_window, text="Reviews are shown.", bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def update_review():

    # Zobrazí okno pro aktualizaci recenze a aktualizuje recenzi v databázi, když uživatel odešle formulář.
    update_window = Toplevel()
    update_window.title("Update Review+100+100")
    update_window.geometry("1200x750")
    update_window.configure(bg='gray10')

    # Zobrazit existující recenze v textovém poli
    reviews = data_tier.get_review()
    result_text = Text(update_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<25} {:<25} {:<25} {:<35} {:<35} {:<25} {:<25} \n".format("No.", "Review_id",
                                                                                            "customer_id",
                                                                                            "product_name",
                                                                                            "rating", "comment",
                                                                                            "review_date",
                                                                                            "customer_name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for review in reviews:
        cislo += 1
        review_date = review['review_date'].strftime('%Y-%m-%d')
        result_text.insert(END, "{:<5} {:<35} {:<35} {:<30} {:<35} {:<35} {:<25} {:<25} \n\n".format(str(cislo),
                                                                                                     review[
                                                                                                         'review_id'],
                                                                                                     str(review[
                                                                                                             'customer_id']),
                                                                                                     str(review[
                                                                                                             'product_id']),
                                                                                                     review['rating'],
                                                                                                     review['comment'],
                                                                                                     review_date,
                                                                                                     review[
                                                                                                         'customer_name'], ))
        result_text.insert(END, "-" * 225 + "\n")

    # Přidat vstupy formuláře pro aktualizaci recenze
    review_id_label = Label(update_window, text="Review id:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_id_label.pack(pady=(10, 0))
    review_id_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    review_id_entry.pack()

    review_rating_label = Label(update_window, text="New Rating:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_rating_label.pack(pady=(10, 0))
    review_rating_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    review_rating_entry.pack()

    review_comment_label = Label(update_window, text="New Comment:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_comment_label.pack(pady=(10, 0))
    review_comment_entry = Entry(update_window, bg='white', fg="black", font=("Helvetica", 12))
    review_comment_entry.pack()

    def update_products_in_database():
        # Funkce aktualizuje hodnocení a komentář existující recenze v databázi pomocí vstupních polí.
        review_id = review_id_entry.get()
        new_rating = review_rating_entry.get()
        new_comment = review_comment_entry.get()

        # Aktualizuje hodnocení a komentář v databázi pro danou recenzi
        data_tier.update_review_rating_comment(new_rating, new_comment, review_id)

        # Zobrazí zprávu o úspěšném dokončení aktualizace výstupním polem
        result_label.config(text="Review has been updated.")

    update_button = Button(update_window, text="Update Review", bg='white', fg="black", font=("Helvetica", 12),
                           command=update_products_in_database)
    update_button.pack(pady=(20, 0))

    result_label = Label(update_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack(pady=(10, 0))


def delete_review_window():
    # Vytvoření nového okna pro zadání jména zákazníka
    delete_window = Toplevel()
    delete_window.title("Delete Review")
    delete_window.geometry("1200x750+100+100")
    delete_window.configure(bg='gray10')

    reviews = data_tier.get_review()
    result_text = Text(delete_window, bg='gray10', fg="white", font=("Helvetica", 12))
    result_text.pack(fill=BOTH, expand=True)

    result_text.insert(END,
                       "\n{:<5} {:<25} {:<25} {:<25} {:<35} {:<35} {:<25} {:<25} \n".format("No.", "Review_id",
                                                                                            "customer_id",
                                                                                            "product_name",
                                                                                            "rating", "comment",
                                                                                            "review_date",
                                                                                            "customer_name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for review in reviews:
        cislo += 1
        review_date = review['review_date'].strftime('%Y-%m-%d')
        result_text.insert(END, "{:<5} {:<35} {:<35} {:<30} {:<35} {:<35} {:<25} {:<25} \n\n".format(str(cislo),
                                                                                                     review[
                                                                                                         'review_id'],
                                                                                                     str(review[
                                                                                                             'customer_id']),
                                                                                                     str(review[
                                                                                                             'product_id']),
                                                                                                     review['rating'],
                                                                                                     review['comment'],
                                                                                                     review_date,
                                                                                                     review[
                                                                                                         'customer_name'], ))
        result_text.insert(END, "-" * 225 + "\n")

    # Vytvoření popisku a vstupního pole pro zadání jména zákazníka
    review_id_label = Label(delete_window, text="Review id:", bg='gray10', fg="white", font=("Helvetica", 12))
    review_id_label.pack()
    review_id_entry = Entry(delete_window, font=("Helvetica", 14))
    review_id_entry.pack()

    def delete_reviews_from_controller():
        # Získat ID recenze z vstupního pole
        review_id = review_id_entry.get()

        # Smazat recenzi z kontroléru (controlleru)
        data_tier.delete_review(review_id)

        # Zobrazit zprávu oznamující, že byla recenze smazána
        result_label.config(text="Review deleted successfully.")

    # Vytvořit tlačítko pro smazání recenzí.
    delete_button = Button(delete_window, text="Delete Review", bg='gray10', fg="white",
                           command=delete_reviews_from_controller, font=("Helvetica", 12))
    delete_button.pack()

    # Vytvořit popisek pro zobrazení výsledku mazání recenzí.
    result_label = Label(delete_window, bg='gray10', fg="white", font=("Helvetica", 14))
    result_label.pack()


def add_review():
    add_window = Toplevel()
    add_window.title("Add Review")
    add_window.geometry("1200x800+100+100")
    add_window.configure(bg='gray10')

    customers = data_tier.get_customers()
    products = data_tier.get_product()

    # Vytvořit textové pole pro výstup.
    result_text = Text(add_window, bg='gray10', fg="white", font=("Helvetica", 9))
    result_text.pack(side=TOP, fill=BOTH, expand=False)

    # Zobrazit seznam hodnoceni.
    result_text.insert(END, "\n{:<5} {:<30} \n".format("Id.", "Name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for customer in customers:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30}\n\n".format(str(cislo), customer['name']))

    # Zobrazit seznam recenzí.
    result_text.insert(END, "\n{:<5} {:<30} \n".format("No.", "Product Name"))
    result_text.insert(END, "-" * 225 + "\n")

    cislo = 0
    for product in products:
        cislo += 1
        result_text.insert(END, "{:<5} {:<30}\n\n".format(str(cislo), product['Product_name']))

    # Vytvořte vstupní formulář.
    input_frame = Frame(add_window, bg='gray10')
    input_frame.pack(side=BOTTOM, fill=Y, pady=5)

    customer_id_label = Label(input_frame, text="Customer id:", bg='gray10', fg="white", font=("Helvetica", 12))
    customer_id_entry = Entry(input_frame, font=("Helvetica", 12))
    customer_id_label.pack(pady=5)
    customer_id_entry.pack()

    product_id_label = Label(input_frame, text="Product id:", bg='gray10', fg="white", font=("Helvetica", 12))
    product_id_entry = Entry(input_frame, font=("Helvetica", 12))
    product_id_label.pack(pady=5)
    product_id_entry.pack()

    rating_label = Label(input_frame, text="Rating:", bg='gray10', fg="white", font=("Helvetica", 12))
    rating_entry = Entry(input_frame, font=("Helvetica", 12))
    rating_label.pack(pady=5)
    rating_entry.pack()

    comment_label = Label(input_frame, text="Comment:", bg='gray10', fg="white", font=("Helvetica", 12))
    comment_entry = Entry(input_frame, font=("Helvetica", 12))
    comment_label.pack(pady=5)
    comment_entry.pack()

    result_label = Label(input_frame, text="", bg='gray10', fg="white", font=("Helvetica", 12))
    result_label.pack(pady=5)

    # Vytvořit tlačítko pro odeslání (Submit
    def submit_review():
        customer_id = customer_id_entry.get()
        product_id = product_id_entry.get()
        rating = rating_entry.get()
        comment = comment_entry.get()

        if not customer_id or not product_id or not rating or not comment:
            result_label.configure(text="Please fill all fields.", fg="red")
            return
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError
        except ValueError:
            result_label.configure(text="Rating must be a number between 1 and 5.", fg="red")
            return

        review = Review(customer_id, product_id, rating, comment)
        data_tier.add_review(review)

        # Vyčistit vstupní pole.
        customer_id_entry.delete(0, END)
        product_id_entry.delete(0, END)
        rating_entry.delete(0, END)
        comment_entry.delete(0, END)

        # Zobrazit zprávu o úspěšném dokončení akce.
        result_label.configure(text="Review added successfully.", fg="green")

    submit_button = Button(input_frame, text="Submit", bg="#4a4a4a",
                           fg="white", command=submit_review, font=("Helvetica", 14))
    submit_button.pack(pady=5)
