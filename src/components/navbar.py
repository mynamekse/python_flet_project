import flet as ft

def Navbar(page: ft.Page, title: str):
    return ft.AppBar(
        title=ft.Text(title),
        center_title=True,
        bgcolor=ft.Colors.BLUE_GREY,
        actions=[
            ft.IconButton(ft.Icons.HOME, on_click=lambda _: page.go("/")),
            ft.IconButton(ft.Icons.SETTINGS, on_click=lambda _: page.go("/settings")),
            ft.IconButton(ft.Icons.LOGOUT, on_click=lambda _: page.go("/login")),
        ]
    )
