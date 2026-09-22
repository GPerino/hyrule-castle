class User:

    def __init__(self, username: str) -> None:
        self.username = username

    def tostring(self):
        return f" Joueur {self.username}"

    def get_username(self):
        return self.username