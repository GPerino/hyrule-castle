from base_game.classes.character import Character


class Boss(Character):
    def __init__(
            self,
            identifier: int,
            name: str,
            max_health: int,
            str_: int,
            def_: int,
            spd: int,
            luck: int
    ) -> None:
        super().__init__(identifier, name, max_health, str_, def_, spd, luck)

    def to_dict(self) -> dict:
        return {
            "identifier": self.identifier,
            "name": self.name,
            "max_health": self.max_health,
            "str_": self.str_,
            "def_": self.def_,
            "spd": self.spd,
            "luck": self.luck
        }

    @classmethod
    def from_dict(cls, data) -> Boss:
        return cls(**data)
