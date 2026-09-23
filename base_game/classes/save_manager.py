import glob
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SaveManager:
    def __init__(self):
        pass

    def save_game(self, game, name):
        saves = [
            file
            for file in glob.glob(BASE_DIR + "/saves/*.json")
        ]
        if saves.count(BASE_DIR + f"/saves/{name}.json") > 0:
            name = name + f"__{saves.count(name)+1}"
        file = open(BASE_DIR + "/saves/" + name + ".json", "w")
        content = game.to_dict()
        json.dump(content, file, indent=2)
        file.close()

