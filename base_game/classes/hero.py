from .character import Character


class Hero(Character):
    def __init__(self,  name, max_health, str_, def_, spd, luck, id=0, hp=0):
        super().__init__(name, max_health, str_, def_, spd, luck)

    def to_dict(self):
        return {
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