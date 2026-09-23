import glob
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SaveManager:
    def __init__(self):
        pass

    def print_all_saves(self):
        """
        return all filename in saves.json
        :return:
        """
        saves = []
        for file in glob.glob(BASE_DIR + "/saves/*.json"):
            saves.append(file)
        for save in saves:
            print(save.character.name)
        return saves

    def save_game(self, game, name):
        file = open(BASE_DIR + "/saves/" + name + ".json", "w")
        content = game.to_dict()
        json.dump(content, file, indent=2)
        file.close()

