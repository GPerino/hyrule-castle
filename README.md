# Hyrule Castle

Hyrule Castle is a turn-based RPG played in the terminal.

The goal is to progress through the dungeon, defeat its enemies and ultimately defeat the boss to complete the game.

The game is inspired by **The Legend of Zelda: Ocarina of Time**.

## Requirements

* Python 3.10 or higher
* A terminal with support for `curses`

## Installation

Clone the repository:

```bash
git clone https://github.com/GPerino/hyrule-castle.git
cd hyrule-castle
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the game with:

```bash
python -m base_game.main
```

## Project Structure

The project is organized around several main components:

* `Game`: manages the current game and its state
* `Hero`: represents the playable character
* `Character`: base class for characters
* `Dungeon`: represents a dungeon and its configuration
* `Room`: defines the different types of rooms
* `DungeonManager`: manages dungeon and room progression
* `Save`: represents a saved game
* `SaveManager`: handles game saves

## Tests

Unit tests are located in the `tests/` directory.

Run the test suite with:

```bash
pytest
```
## Next Features
- [x] Title screen
- [x] Character creation
- [x] Options
- [ ] Pause menu
- [x] Load game
- [ ] Music
- [ ] Difficulty levels
- [ ] Inventory
- [ ] Escape from the battle
- [ ] Chest loot

## Author
- [Gabriel PERINO](https://github.com/GPerino)
- [GitHub](https://github.com/GPerino/hyrule-castle)