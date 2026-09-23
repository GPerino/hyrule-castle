from base_game.classes.game import Game
from base_game.classes.hero import Hero


class Save:
    def __init__(self, metadata, game):
        self.metadata = metadata
        self.game = game

    @classmethod
    def from_dict(cls, data, audio):
        hero = Hero.from_dict(data["hero"])
        game = Game.from_dict(
            data["game"],
            hero=hero,
            audio=audio
        )

        return cls(
            metadata=data["metadata"],
            game=game
        )