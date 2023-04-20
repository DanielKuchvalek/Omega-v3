import sys
from tkinter import Button, Toplevel
from src.widgets.widget import Widget
from src.window_methods import methods_category
from src.widgets import menu_widgets

class Category_widget(Widget):
    def __init__(self, master, role):
        super().__init__(master, role)

    def category_widgets(self):
        category_window = Toplevel(self.master)
        category_window.title("Categories")
        category_window.geometry("170x400+100+100")
        category_window.config(bg='gray10')
        category_window.protocol('WM_DELETE_WINDOW', self.quit_app)

        # Show Customers button
        category_button = Button(category_window, text="Show Category", command=methods_category.show_category,
                                 bg="#4a4a4a",
                                 fg="white")
        category_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        if self.role == "admin":
            # Add Category button
            add_category_button = Button(category_window, text="Add Category",
                                         command=methods_category.add_category,
                                         bg="#4a4a4a", fg="white", width=20, height=2)
            add_category_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

            # Update Category button
            update_category_button = Button(category_window, text="Update Category",
                                            command=methods_category.update_category,
                                            bg="#4a4a4a", fg="white")
            update_category_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            # Delete Category button
            delete_category_button = Button(category_window, text="Delete Category",
                                            command=methods_category.delete_category_window, bg="#4a4a4a",
                                            fg="white",
                                            width=20,
                                            height=2)
            delete_category_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

            # Import Category button
            import_category_button = Button(category_window, text="Import Category",
                                            command=methods_category.import_category,
                                            bg="#4a4a4a", fg="white")
            import_category_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Back button
        back_button = Button(category_window, text="Back",
                             command=lambda: [category_window.destroy(), menu_widgets.Menu_widget(self.master,self.role).menu_widgets()], bg="#4a4a4a",
                             fg="white", width=20, height=2)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

    def quit_app(self):
        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell