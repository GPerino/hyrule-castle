class Dungeon:
    def __init__(self, id, name, theme, boss, enemies, elites, rooms):
        self.id = id
        self.name = name
        self.theme = theme
        self.boss = boss
        self.enemies = enemies
        self.elites = elites
        self.rooms = rooms

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "theme": self.theme,
            "boss": self.boss,
            "enemies": self.enemies,
            "elites": self.elites,
            "rooms": self.rooms,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
