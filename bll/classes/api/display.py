from termcolor import colored
from tabulate import tabulate
from bll.classes.api.utils import display_as_table, display_as_list

class DisplayStrategy:
    def display(self, data, headers=None, header_color="blue"):
        raise NotImplementedError("Method 'display' should be implemented.")

class TableDisplayStrategy(DisplayStrategy):
    def display(self, data, headers=None, header_color="blue"):
        display_as_table(data, headers, header_color)

class ListDisplayStrategy(DisplayStrategy):
    def display(self, data, headers=None, header_color="blue"):
        display_as_list(data)

class DisplayFactory:
    def get_display_strategy(self, format_type):
        if format_type == "table":
            return TableDisplayStrategy()
        elif format_type == "list":
            return ListDisplayStrategy()
        else:
            raise ValueError("Unsupported display format type.")