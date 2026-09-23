from .character import Character


class Hero(Character):
    def __init__(self,  name, max_health, str_, def_, spd, luck, id=0):
        super().__init__(name, max_health, str_, def_, spd, luck)

    def to_dict(self):
        return {
            "name": self.name,
            "max_health": self.max_health,
            "hp": self.hp,
            "strength": self.strength,
            "defense": self.defense,
            "spd": self.spd,
            "luck": self.luck
        }
