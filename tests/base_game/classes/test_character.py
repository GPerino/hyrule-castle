import pytest

from base_game.classes.character import Character


# "name": "Link",
# "hp": 120,
# "max_health": 120,
# "str_": 20,
# "def_": 12,
# "spd": 11,
# "luck": 10
class TestCharacter:
    def test_init_keese(self):
        # Arrange
        keese_id: int = 5
        keese_name: str = "Keese"
        keese_max_health: int = 50
        keese_str: int = 9
        keese_def: int = 3
        keese_spd: int = 11
        keese_luck: int = 5

        # Act
        character = Character(
            keese_id,
            keese_name,
            keese_max_health,
            keese_str,
            keese_def,
            keese_spd,
            keese_luck,
            None
        )

        # Assert
        assert character.id == keese_id
        assert character.name == keese_name
        assert character.max_health == keese_max_health
        assert character.hp == keese_max_health
        assert character.str_ == keese_str
        assert character.def_ == keese_def
        assert character.spd == keese_spd
        assert character.luck == keese_luck
