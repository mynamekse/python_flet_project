import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text(value="Hello, Flet!", size=30),
        ft.Text(value="Running with uv", size=15)
    )

if __name__ == "__main__":
    ft.app(target=main)
