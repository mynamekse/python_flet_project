import flet as ft
from components.navbar import Navbar
from components.custom_card import CustomCard
from models.product_model import Product

def HomeView(page: ft.Page):
    products = Product.get_products()
    
    return ft.View(
        "/",
        [
            Navbar(page, "Home"),
            ft.Container(
                content=ft.Row(
                    [CustomCard(p) for p in products],
                    wrap=True,
                    scroll=ft.ScrollMode.AUTO,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=20,
                expand=True,
            ),
        ],
    )
