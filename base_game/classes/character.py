class Character:
    def __init__(self, name, max_health, str_, def_, spd, luck, hp=None):
        self.name = name
        self.max_health = max_health
        self.hp = max_health if hp is None else hp
        self.strength = str_
        self.defense = def_
        self.spd = spd
        self.luck = luck

    def attack(self, target):
        target.take_damage(self.strength)

    def health_check(self):
        print("{} a {} points de vie restants".format(self.name, self.hp))

    def take_damage(self, damage):
        final_damage = damage - self.defense
        self.hp -= final_damage

    def reload_health(self):
        self.hp = self.max_health
