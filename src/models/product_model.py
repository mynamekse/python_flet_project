from typing import List

class Product:
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    @staticmethod
    def get_products() -> List["Product"]:
        return [
            Product("Laptop", 999.99, "High performance laptop"),
            Product("Smartphone", 699.99, "Latest model smartphone"),
            Product("Headphones", 199.99, "Noise cancelling headphones"),
            Product("Smart Watch", 299.99, "Fitness tracker and more"),
        ]
