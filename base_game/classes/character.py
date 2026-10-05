class Character:
    def __init__(
            self,
            identifier: int,
            name: str,
            max_health: int,
            str_: int,
            def_: int,
            spd: int,
            luck: int,
            hp=None
    ) -> None:
        self.id = identifier
        self.name = name
        self.max_health = max_health
        self.hp = max_health if hp is None else hp
        self.str_ = str_
        self.def_ = def_
        self.spd = spd
        self.luck = luck

    def take_damage(self, damage: int) -> None:
        final_damage: int = damage - self.def_
        self.hp -= final_damage

    def attack(self, target: Character) -> None:
        target.take_damage(self.str_)

    def health_check(self) -> None:
        print(f"{self.name} a {self.hp} points de vie restants")

    def reload_health(self) -> None:
        self.hp = self.max_health
