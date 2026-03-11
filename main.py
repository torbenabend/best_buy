"""Command-line interface for interacting with a store inventory system.

This module provides a simple CLI that allows users to view available
products, check the total quantity of items in the store, and create
orders. The module initializes a store with predefined products and
uses a dispatch table to map user menu selections to the corresponding
functions.

Functions in this module handle user interaction, menu display, command
dispatching, and order creation.
"""
from typing import Callable
from products import Product
from store import Store


def init_store() -> Store:
    """Create and initialize the store with a predefined list of products.

    Returns:
        Store: A store instance containing the initial set of products.
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250,
                            quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    return Store(product_list)


def start(store: Store):
    """Start the command-line interface loop for the store application.

    Displays the menu, prompts the user for a command, and dispatches the
    selected command until the user chooses to quit.

    Args:
        store (Store): The store instance used during the application runtime.
    """
    while True:
        show_menu()
        user_command = prompt_user_command()
        store, is_running = dispatch_command(user_command, store)
        if not is_running:
            break


def dispatch_command(user_command: str, store: Store) -> tuple[Store, bool]:
    """Execute the function associated with a user command.

    Looks up the command in the dispatch table and executes the corresponding
    function. If the command is invalid, an error message is displayed.

    Args:
        user_command (str): The command entered by the user.
        store (Store): The current store instance.

    Returns:
        tuple[Store, bool]: The updated store instance and a flag indicating
        whether the application should continue running.
    """
    commands = get_dispatch_table()
    if user_command in commands:
        return commands[user_command]["function"](store)
    print("Error with your choice! Try again!\n")
    return store, True


def prompt_user_command() -> str:
    """Prompt the user to enter a menu command.

    Returns:
        str: The trimmed user input representing the selected command.
    """
    return input("Please choose a number: ").strip()


def show_menu():
    """Display the available store menu options.

    Retrieves the dispatch table and prints each available command
    with its corresponding menu description.
    """
    commands = get_dispatch_table()
    print("\n   Store Menu")
    print("   " + 10 * "-")
    for nr, command in commands.items():
        print(f"{nr}. {command['menu_item']}")


def list_products(store: Store) -> tuple[Store, bool]:
    """Display all available products in the store.

    Each product is printed with its index number, name, price,
    and available quantity.

    Args:
        store (Store): The store instance containing the products.

    Returns:
        tuple[Store, bool]: The unchanged store instance and a flag
        indicating that the application should continue running.
    """
    numbered_products = enumerate(store.products, 1)
    separator_line = 6 * "-"
    print(separator_line)
    for i, product in numbered_products:
        print(f"{i}. {product.name}, "
              f"Price: {product.price}, "
              f"Quantity: {product.quantity}")
    print(separator_line)
    return store, True


def show_total_amount(store: Store) -> tuple[Store, bool]:
    """Display the total quantity of all products in the store.

    Args:
        store (Store): The store instance containing the products.

    Returns:
        tuple[Store, bool]: The unchanged store instance and a flag
        indicating that the application should continue running.
    """
    total_amount = sum(product.quantity for product in store.products)
    print(f"Total of {total_amount} items in store")
    return store, True


def make_order(store: Store) -> tuple[Store, bool]:
    """Handle the order creation process.

    Displays available products, allows the user to build a shopping list,
    and attempts to place an order through the store instance.

    Args:
        store (Store): The store instance used to process the order.

    Returns:
        tuple[Store, bool]: The store instance and a flag indicating
        that the application should continue running.
    """
    _, _ = list_products(store)
    print("When you want to finish order, enter empty text.")
    shopping_list = fill_shopping_list(store)
    try:
        print(8 * "*")
        total_price = store.order(shopping_list)
        print(f"Order made! Total payment: ${total_price}")
    except ValueError as err:
        print(f"Error while making order! {err}")
    return store, True


def quit_cli(store: Store) -> tuple[Store, bool]:
    """Terminate the command-line interface loop.

    Args:
        store (Store): The current store instance.

    Returns:
        tuple[Store, bool]: The store instance and False to indicate
        that the application should stop running.
    """
    return store, False


def fill_shopping_list(store: Store) -> list[tuple[Product, str]]:
    """Create a shopping list based on user input.

    The user selects products by their index and specifies the desired
    quantity. Input continues until an empty value is entered.

    Args:
        store (Store): The store instance containing available products.

    Returns:
        list[tuple[Product, str]]: A list of tuples where each tuple contains
        a product and the requested quantity.
    """
    shopping_list = []
    while True:
        item_nr = input("Which product # do you want? ").strip()
        quantity = input("What amount do you want? ").strip()
        new_shopping_list_entry = (item_nr, quantity)
        if "" in new_shopping_list_entry:
            break
        try:
            item_nr = int(item_nr)
            product = store.products[item_nr - 1]
            new_shopping_list_entry = (product, quantity)
            shopping_list.append(new_shopping_list_entry)
            print("Product added to list!")
        except (ValueError, IndexError):
            print("Error adding product!")
    return shopping_list


def get_dispatch_table() -> dict[
    str, dict[str, Callable[[Store], tuple[Store, bool]]]
]:
    """Create the command dispatch table for the CLI menu.

    The dispatch table maps user command numbers to their corresponding
    menu descriptions and handler functions.

    Returns:
        dict[str, dict[str, Callable[[Store], tuple[Store, bool]]]]:
            A dictionary mapping command identifiers to their menu
            descriptions and callable handler functions.
    """
    commands = {
            "1": {
                "menu_item": "List all products in store",
                "function": list_products
            },
            "2": {
                "menu_item": "Show total amount in store",
                "function": show_total_amount
            },
            "3": {
                "menu_item": "Make an order",
                "function": make_order
            },
            "4": {
                "menu_item": "Quit",
                "function": quit_cli
            }
        }
    return commands


def main():
    """Initialize the store and start the CLI application."""
    best_buy = init_store()
    start(best_buy)


if __name__ == "__main__":
    main()
