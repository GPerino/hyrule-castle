from tkinter import Menu

from base_game.classes.Character_manager import CharacterManager
from base_game.game import Game
from base_game.utils import display_character_card

class NewGameMenu:
    def __init__(self):
        self.manager = CharacterManager()
        self.game = Game()
def choose_difficulty(stdscr):
    pass


def choose_game_mode(stdscr):
    pass


def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Nouvelle Partie")
    stdscr.refresh()
    playername = stdscr.getch()
    stdscr.refresh()
    game_mode = choose_game_mode(stdscr)
    difficulty = choose_difficulty(stdscr)
    character = choose_character(stdscr)


def choose_character(self, stdscr):
    characters = self.manager.get_characters()
    screen_h, screen_w = stdscr.getmaxyx()
    start_y = (screen_h // 2) - (10 // 2)
    start_x = (screen_w // 2) - (35 // 2)
    selected_index = 0
    while True:
        stdscr.clear()
        stdscr.addstr(start_y - 2, start_x + 4, f"Choisissez votre personnage")
        stdscr.refresh()
        display_character_card(stdscr, characters[selected_index], start_y, start_x)
        key = stdscr.getkey()
        if key == "KEY_UP":
            selected_index = (selected_index - 1) % len(characters)
        elif key == "KEY_DOWN":
            selected_index = (selected_index + 1) % len(characters)
        elif key == "\n":
            return characters[selected_index]
