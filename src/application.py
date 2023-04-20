from tkinter import Frame, Button, Label, Entry, messagebox
import sys
import re
import mysql.connector
from src.widgets.menu_widgets import Menu_widget
from src.datatier import DBConnection


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.role = None
        self.pack()
        self.db = DBConnection()
        self.login_window()

    def login_window(self):
        login_window = Frame(self.master, bg="gray10")
        login_window.pack(fill="both", expand=True)

        username_label = Label(login_window, text="Username:", fg="white", bg="gray10", font=("Arial", 12))
        username_label.grid(row=0, column=0, pady=5)
        username_entry = Entry(login_window, bg="gray25", fg="white", font=("Arial", 12))
        username_entry.grid(row=0, column=1)

        password_label = Label(login_window, text="Password:", fg="white", bg="gray10", font=("Arial", 12))
        password_label.grid(row=1, column=0, pady=5)
        password_entry = Entry(login_window, show="*", bg="gray25", fg="white", font=("Arial", 12))
        password_entry.grid(row=1, column=1)

        register_button = Button(login_window, text="Register", bg="gray40", fg="white", font=("Arial", 12),
                                 command=lambda: [login_window.destroy(), self.register_window()])
        register_button.grid(row=2, column=0, pady=10, padx=60)

        login_button = Button(login_window, text="Login", bg="gray40", fg="white", font=("Arial", 12),
                              command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.grid(row=2, column=1, pady=10, padx=60)

        self.master.bind("<Return>", lambda event: self.login(username_entry.get(), password_entry.get()))

        username_entry.focus_set()

    def register_window(self):
        register_window = Frame(self.master, bg="gray10")
        register_window.pack(fill="both", expand=True)

        # Add labels and entry fields for username, password and confirm password
        username_label = Label(register_window, text="Username:", fg="white", bg="gray10", font=("Arial", 12))
        username_label.grid(row=0, column=0, pady=5)
        username_entry = Entry(register_window, bg="gray25", fg="white", font=("Arial", 12))
        username_entry.grid(row=0, column=1)

        password_label = Label(register_window, text="Password:", fg="white", bg="gray10", font=("Arial", 12))
        password_label.grid(row=1, column=0, pady=5)
        password_entry = Entry(register_window, show="*", bg="gray25", fg="white", font=("Arial", 12))
        password_entry.grid(row=1, column=1)

        confirm_password_label = Label(register_window, text="Confirm Password:", fg="white", bg="gray10",
                                       font=("Arial", 12))
        confirm_password_label.grid(row=2, column=0, pady=5)
        confirm_password_entry = Entry(register_window, show="*", bg="gray25", fg="white", font=("Arial", 12))
        confirm_password_entry.grid(row=2, column=1)

        # Add a button to register the new user
        register_button = Button(register_window, text="Register", bg="gray40", fg="white", font=("Arial", 12),
                                 command=lambda: self.register(username_entry.get(), password_entry.get(),
                                                               confirm_password_entry.get()))
        register_button.grid(row=3, column=1, pady=10, padx=60)

        # Add a button to go back to the login window
        login_button = Button(register_window, text="Back to Login", bg="gray40", fg="white", font=("Arial", 12),
                              command=lambda: [register_window.destroy(), self.login_window()])
        login_button.grid(row=3, column=0, pady=10, padx=60)

        # Focus on the username entry field
        username_entry.focus_set()

    def login(self, username, password):
        # Remove any existing error messages
        for widget in self.master.winfo_children():
            if isinstance(widget, Label) and widget.cget("fg") == "red":
                widget.destroy()

        # Check the username and password against the database
        cursor = self.db.cursor()
        cursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        if result:
            self.role = result[0]
        else:
            self.role = None

        if self.role:
            self.menu_widgets()
            self.master.withdraw()  # skryje okno s login formulářem
        else:
            # Display an error message if the login is unsuccessful
            error_message = Label(self.master, text="Incorrect username or password.", fg="red")
            error_message.pack()

    def register(self, username, password, confirm_password):
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Check if the username already exists
        cursor = self.db.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result[0] > 0:
            messagebox.showerror("Error", "Username already exists")
            return

        # Check the password pattern
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            messagebox.showerror("Error",
                                 "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
            return

        # Insert the new user into the database
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, 'user');"
        params = username, password
        self.db.execute(query, params)

        # Display a message to inform the user that the registration was successful
        self.login_window()
        self.master.withdraw()
        success_message = Label(self.master, text="Registration successful.", fg="green")
        success_message.pack()

    def menu_widgets(self):
        self.widgets = Menu_widget(self.master, self.role)
        self.widgets.menu_widgets()

    def quit_app(self):
        # Close the database connection before quitting the application
        self.db.close()

        if sys.stdin.isatty():  # Check if running as a standalone process
            self.master.destroy()
            sys.exit()  # Exit the process
        else:
            self.master.destroy()  # Quit the app if running in an interactive shell
