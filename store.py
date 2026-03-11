from products import Product

class Store:
    """
    Represents a store containing multiple products.

    Provides methods to add or remove products, query total quantity,
    retrieve active products, and process orders.
    """


    def __init__(self, products: list[Product] | None = None):
        """
        Initialize a new Store instance.

        Args:
            products (list[Product] | None): Optional initial list of
                Product instances to include in the store. Defaults to
                an empty list.
        """
        if products is None:
            products = []
        self.products = products


    def add_product(self, product: Product):
        """
        Add a product to the store.

        Args:
            product (Product): The Product instance to add.
        """
        self.products.append(product)


    def remove_product(self, product: Product):
        """
        Remove a product from the store.

        Args:
            product (Product): The Product instance to remove.

        Raises:
            ValueError: If the product is not currently in the store.
        """
        if product not in self.products:
            raise ValueError(
                "'product' must be in 'store.products' to be removed."
            )
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.

        Returns:
            int: Sum of the quantities of all products.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self) -> list[Product]:
        """
        Retrieve all active products in the store.

        Returns:
            list[Product]: A list of Product instances that are active.
        """
        active_products = [
            product for product in self.products if product.active
        ]
        return active_products


    def order(self, shopping_list: list[tuple[Product, str]]):
        """
        Process an order consisting of multiple products and quantities.

        Each product in the shopping list must exist in the store. The
        method updates product quantities and calculates the total price.

        Args:
            shopping_list (list[tuple[Product, int]]): List of tuples,
                where each tuple contains a Product instance and the
                quantity to purchase.

        Returns:
            float: Total price of all purchased products.

        Raises:
            ValueError: If any product in the shopping list is not in
                the store.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} not found in store.")
            total_price += product.buy(int(quantity))
        return total_price
