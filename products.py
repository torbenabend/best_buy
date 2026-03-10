class Product:
    """
    Represents a product with a name, price, quantity in stock, and an
    active status.

    A product can be purchased, which reduces its available quantity.
    When the quantity reaches zero, the product is automatically
    deactivated.
    """


    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new Product instance.

        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must not be
                           negative.
            quantity (int): The available quantity in stock. Must not
                            be negative.

        Raises:
            ValueError: If name is empty, or if price or quantity is
                        negative.
        """
        if not name.strip():
            raise ValueError("'name' must not be empty.")
        if price < 0:
            raise ValueError("'price' must not be negative.")
        if quantity < 0:
            raise ValueError("'quantity' must not be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """
        Return the current quantity available in stock.

        Returns:
            int: The remaining quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity: int):
        """
        Set the product quantity.

        If the quantity is set to zero, the product will automatically be
        marked as inactive.

        Args:
            quantity (int): The new quantity of the product.
        """
        if quantity < 0:
            raise ValueError("'quantity' must not be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """
        Check whether the product is active.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activate the product.

        An active product can be purchased if stock is available.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivate the product.

        A deactivated product is typically not available for purchase.
        """
        self.active = False


    def show(self):
        """
        Display the product information.

        Prints the product name, price, and current quantity to the
        console.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.

        The quantity in stock will be reduced by the purchased amount.

        Args:
            quantity (int): The number of items to purchase.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If the requested quantity exceeds the available
                        stock.
        """
        if quantity < 0:
            raise ValueError("'quantity' must not be negative.")

        quantity_left = self.quantity - quantity
        if quantity_left < 0:
            raise ValueError("Requested quantity exceeds available stock.")

        total_price = quantity * self.price
        self.set_quantity(quantity_left)
        return total_price
