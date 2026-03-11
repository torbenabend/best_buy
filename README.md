# Store CLI Inventory System

A simple Python command-line application that simulates a store inventory system.
Users can view available products, check the total quantity of items in the store,
and create orders through an interactive menu.

The project demonstrates basic object-oriented programming concepts in Python,
including classes, object interaction, input handling, and simple command dispatching.

---

## Features

- Display all products available in the store
- Show the total quantity of items currently in stock
- Create orders by selecting products and quantities
- Automatic stock updates after purchases
- Products automatically deactivate when stock reaches zero
- Simple command-line interface (CLI)

---

## Project Structure
```
store-cli\
├── main.py
├── products.py
├── store.py
└── README.md
```
### main.py
Handles the CLI and user interaction.

Responsibilities:
- Displaying the menu
- Reading user input
- Dispatching commands
- Handling order creation

### products.py
Defines the **Product** class.

Responsibilities:
- Representing individual products
- Managing product quantity
- Handling product purchases
- Managing active/inactive status

### store.py
Defines the **Store** class and order processing logic.

Responsibilities:
- Managing the list of products
- Adding and removing products
- Calculating total inventory quantity
- Processing customer orders

---

## Requirements

Python 3.10 or newer.

No external dependencies are required.

---

## Running the Application

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the application:

```bash
  python main.py
```
---

## Example Menu
```
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```
## Example product output
```
------
1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250
------
```
---

## How ordering works

1. Choose **"Make an order"** from the menu.
2. Select a product by its number.
3. Enter the quantity you want to purchase.
4. Repeat until finished.
5. Press Enter without input to finalize the order.

Example:
```
Which product # do you want? 2
What amount do you want? 3
Product added to list!

Which product # do you want?
```
After completion, the system calculates the total price and updates the inventory.

## Example Order Output
```
********
Order made! Total payment: $750
```
## License

This project is intended for educational purposes.