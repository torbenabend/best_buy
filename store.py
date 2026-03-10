from products import Product

class Store:


    def __init__(self, products: list[Product] | None = None):
        if products is None:
            products = []
        self.products = products


    def add_product(self, product: Product):
        self.products.append(product)


    def remove_product(self, product: Product):
        if product not in self.products:
            raise ValueError(
                "'product' must be in 'store.products' to be removed."
            )
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self) -> list[Product]:
        active_products = [
            product for product in self.products if product.active
        ]
        return active_products


    def order(self, shopping_list: list[tuple[Product, int]]):
        total_price = 0
        for item in shopping_list:
            product = item[0]
            if product not in self.products:
                raise ValueError(f"Product {product.name} not found in store.")
            quantity = item[1]
            total_price += product.buy(quantity)
        return total_price

