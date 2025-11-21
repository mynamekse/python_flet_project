import flet as ft
from models.user_model import User
from utils.validators import is_valid_email

def LoginView(page: ft.Page):
    username_field = ft.TextField(label="Username", width=300)
    password_field = ft.TextField(label="Password", password=True, width=300)
    error_text = ft.Text(color=ft.Colors.RED)

    def login_click(e):
        if not username_field.value or not password_field.value:
            error_text.value = "Please fill in all fields"
            error_text.update()
            return

        user = User.authenticate(username_field.value, password_field.value)
        if user:
            page.session.set("user", user.username)
            page.go("/")
        else:
            error_text.value = "Invalid credentials (try admin/1234)"
            error_text.update()

    return ft.View(
        "/login",
        [
            ft.AppBar(title=ft.Text("Login"), bgcolor=ft.Colors.BLUE_GREY),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Welcome Back", size=30, weight=ft.FontWeight.BOLD),
                        username_field,
                        password_field,
                        ft.ElevatedButton("Login", on_click=login_click),
                        error_text,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ],
    )
