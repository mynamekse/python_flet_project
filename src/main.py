import flet as ft
from views.home_view import HomeView
from views.login_view import LoginView
from views.settings_view import SettingsView

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(HomeView(page))
        elif page.route == "/login":
            page.views.append(LoginView(page))
        elif page.route == "/settings":
            page.views.append(SettingsView(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
