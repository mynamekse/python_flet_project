import flet as ft
from models.product_model import Product

def CustomCard(product: Product):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.SHOPPING_BAG),
                        title=ft.Text(product.name),
                        subtitle=ft.Text(product.description),
                    ),
                    ft.Row(
                        [
                            ft.Text(f"${product.price}", size=20, weight=ft.FontWeight.BOLD),
                            ft.ElevatedButton("Buy"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
