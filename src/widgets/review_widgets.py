import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_reviews
from src.widgets import menu_widgets


class Review_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def review_widgets(self):
        review_window = Toplevel(self.master)
        review_window.title("Review")
        review_window.geometry("170x400+100+100")
        review_window.config(bg='gray10')
        review_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        select_review_button = Button(review_window, text="Show Reviews", command=methods_reviews.show_review,
                                      bg="#4a4a4a",
                                      fg="white")
        select_review_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        if self.role =="admin":
            add_category_button = Button(review_window, text="Add Review",
                                         command=methods_reviews.add_review,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_category_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            update_review_button = Button(review_window, text="Update Review",
                                          command=methods_reviews.update_review,
                                          bg="#4a4a4a", fg="white")
            update_review_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            delete_review_button = Button(review_window, text="Delete Reviews",
                                          command=methods_reviews.delete_review_window, bg="#4a4a4a",
                                          fg="white",
                                          width=20,
                                          height=2)
            delete_review_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(review_window, text="Back",
                             command=lambda: [review_window.destroy(),
                                              menu_widgets.Menu_widget(self.master, self.role).menu_widgets()],
                             bg="#4a4a4a", fg="white")
        back_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell