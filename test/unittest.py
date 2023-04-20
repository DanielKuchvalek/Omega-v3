import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk

from src.widgets import customer_widgets
from src.window_methods import methods_customer


class TestCustWidget(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.widget = customer_widgets.Cust_widget(self.root, 'admin')

    def test_customers_widgets(self):
        # Mock methods_customer.show_customers
        with patch('src.window_methods.methods_customer.show_customers') as mock_show_customers:
            # Call customers_widgets
            self.widget.customers_widgets()

            # Check if the customers_window was created
            self.assertEqual(len(self.widget.master.winfo_children()), 1)

            # Click the Show Customers button
            show_customers_button = self.widget.master.winfo_children()[0].winfo_children()[0]
            show_customers_button.invoke()
            # Check if methods_customer.show_customers was called
            mock_show_customers.assert_called_once()

            if self.widget.role == "admin":
                # Mock methods_customer.add_customer
                with patch('src.window_methods.methods_customer.add_customer') as mock_add_customer:
                    # Click the Add Customers button
                    add_customer_button = self.widget.master.winfo_children()[0].winfo_children()[1]
                    add_customer_button.invoke()
                    # Check if methods_customer.add_customer was called
                    mock_add_customer.assert_called_once()

                # Mock self.update_customer_widgets
                self.widget.update_customer_widgets = MagicMock()
                # Click the Update Customers button
                update_customer_button = self.widget.master.winfo_children()[0].winfo_children()[2]
                update_customer_button.invoke()
                # Check if self.update_customer_widgets was called
                self.widget.update_customer_widgets.assert_called_once()

                # Mock methods_customer.delete_customer_window
                with patch('src.window_methods.methods_customer.delete_customer_window') as mock_delete_customer_window:
                    # Click the Delete Customers button
                    delete_customer_button = self.widget.master.winfo_children()[0].winfo_children()[3]
                    delete_customer_button.invoke()
                    # Check if methods_customer.delete_customer_window was called
                    mock_delete_customer_window.assert_called_once()

                # Mock methods_customer.import_customers
                with patch('src.window_methods.methods_customer.import_customers') as mock_import_customers:
                    # Click the Import Customers button
                    import_customer_button = self.widget.master.winfo_children()[0].winfo_children()[4]
                    import_customer_button.invoke()
                    # Check if methods_customer.import_customers was called
                    mock_import_customers.assert_called_once()

            # Click the Back button
            back_button = self.widget.master.winfo_children()[0].winfo_children()[5]
            back_button.invoke()
            # Check if the customers_window was destroyed and the menu_widgets was called
            self.assertEqual(len(self.widget.master.winfo_children()), 0)
