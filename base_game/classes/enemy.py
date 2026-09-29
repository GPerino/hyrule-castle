from base_game.classes.character import Character


class Enemy(Character):
    def __init__(self,  name, max_health, str_, def_, spd, luck, id=0, hp=0):
        super().__init__(id, name, max_health, str_, def_, spd, luck)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "max_health": self.max_health,
            "hp": self.hp,
            "str_": self.str_,
            "def_": self.def_,
            "spd": self.spd,
            "luck": self.luck
        }
    @classmethod
    def from_dict(cls, data):
        return cls(**data)