class User:
    def __init__(self, username: str):
        self.username = username

    @staticmethod
    def authenticate(username: str, password: str) -> "User | None":
        # Mock authentication
        if username == "admin" and password == "1234":
            return User(username)
        return None
