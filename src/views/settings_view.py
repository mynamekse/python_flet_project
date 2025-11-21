import flet as ft
from components.navbar import Navbar

def SettingsView(page: ft.Page):
    return ft.View(
        "/settings",
        [
            Navbar(page, "Settings"),
            ft.Container(
                content=ft.Text("Settings Page", size=20),
                alignment=ft.alignment.center,
                expand=True
            ),
        ],
    )
