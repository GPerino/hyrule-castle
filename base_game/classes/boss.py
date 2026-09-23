from base_game.classes.character import Character


class Boss(Character):
    def __init__(self, name, max_health, str_, def_, spd, luck):
        super().__init__(name, max_health, str_, def_, spd, luck)
