import curses
import os
import re
import sys
import time

from pick import pick

from base_game.classes.Character_manager import CharacterManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_special_characters(text: str):
    """
    Check if user's input is only an integer
    :param text:
    :return: bool
    """
    regex = re.compile("[@.€ç_!#$%^&*()<>' '?\"/\\|}{~:A-z]")
    if regex.search(text) is not None:
        print("Only number please")
        return False
    elif text == "":
        print("Type something ....")
        return False
    else:
        return True


def display_ascii_art(file):
    """Display ASCII art from a file."""
    abs_path = os.path.join(BASE_DIR, file)

    with open(abs_path, "r") as f:
        print(f.read())


def typewriter_effect(text):
    """Write text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()


def show_intro(stdscr, lines=None, title=None, delay_ms=0):
    if lines is None:
        lines = []
    clear_screen(stdscr)
    h, w = stdscr.getmaxyx()
    block = []
    if title:
        block.append(title)
        block.append("")
    block.extend(lines)
    block.append("")
    block.append("Appuie sur une touche pour continuer…")
    y = max(0, (h - len(block)) // 2)
    for i, line in enumerate(block):
        x = max(0, (w - len(line)) // 2)
        stdscr.addstr(y + i, x, line)
        stdscr.refresh()
        if delay_ms > 0:
            curses.napms(delay_ms)
    stdscr.getch()


def choose_difficulty(stdscr):
    stdscr.clear()
    title = "Choisissez la difficulté"
    options = ["Facile", "Normal", "Hardcore"]
    level, _ = pick(options, title, screen=stdscr)
    return level


def choose_game_mode(stdscr):
    stdscr.clear()
    title = "Choisissez le mode de jeu"
    options = ["Histoire", "Difficile", "Aléatoire"]
    # @TODO Afficher détails des options
    mode, index = pick(options, title, screen=stdscr)
    return mode


def choose_character(stdscr):
    manager = CharacterManager()
    characters = manager.get_hero()
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


def display_character_card(stdscr, character, y: int = 2, x: int = 2):
    w = 35
    h = 10
    name = character["name"] if isinstance(character, dict) else character.name
    hp = character["hp"] if isinstance(character, dict) else character.hp
    str_ = character["str_"] if isinstance(character, dict) else character.str_
    def_ = character["def_"] if isinstance(character, dict) else character.def_
    spd = character["spd"] if isinstance(character, dict) else character.spd
    luck = character["luck"] if isinstance(character, dict) else character.luck

    draw_box(stdscr, y, x, h, w, name)
    stdscr.addstr(y + 2, x + 2, f"HP   : {hp_to_hearts(hp)}  ({hp})")
    stdscr.addstr(y + 3, x + 2, f"STR  : {str_}")
    stdscr.addstr(y + 4, x + 2, f"DEF  : {def_}")
    stdscr.addstr(y + 5, x + 2, f"SPD  : {spd}")
    stdscr.addstr(y + 6, x + 2, f"LUCK : {luck}")
    stdscr.addstr(y + 8, x + 2, "↑↓ choisir   ENTER confirmer")


def hp_to_hearts(hp: int, per_heart: int = 10, max_hearts: int = 15) -> str:
    hearts = int(round(hp / per_heart))
    hearts = max(0, min(hearts, max_hearts))
    return "♥" * hearts + "·" * (max_hearts - hearts)


def draw_box(stdscr, y: int, x: int, h: int, w: int, title: str = ""):
    stdscr.addstr(y, x, "┌" + "─" * (w - 2) + "┐")
    stdscr.addstr(y, x + (w - len(title)) // 2, title)
    for i in range(1, h - 1):
        stdscr.addstr(y + i, x, "│" + " " * (w - 2) + "│")
    stdscr.addstr(y + h - 1, x, "└" + "─" * (w - 2) + "┘")


def handle_exit():
    print("\nSaving your progress...")
    # @TODO: Ajouter une logique de sauvegarde
    print("Progress saved.")
    print("Goodbye, adventurer!")


def clear_screen(stdscr):
    """Clear the screen."""
    stdscr.clear()
    stdscr.refresh()
