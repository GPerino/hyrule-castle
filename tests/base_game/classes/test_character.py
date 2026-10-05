import pytest

from base_game.classes.character import Character


class TestCharacter:
    def test_init_keese(self):
        # Arrange
        # Act
        character = Character(
            5,
            "Keese",
            50,
            9,
            3,
            11,
            5,
            None
        )

        # Assert
        assert character.id == 5
        assert character.name == "Keese"
        assert character.max_health == 50
        assert character.hp == 50
        assert character.str_ == 9
        assert character.def_ == 3
        assert character.spd == 11
        assert character.luck == 5

    def test_init_link(self):
        # Arrange
        # Act
        character = Character(
            1,
            "Link",
            120,
            20,
            12,
            11,
            10,
            100
        )

        # Assert
        assert character.id == 1
        assert character.name == "Link"
        assert character.max_health == 120
        assert character.hp == 100
        assert character.str_ == 20
        assert character.def_ == 12
        assert character.spd == 11
        assert character.luck == 10

    def test_take_damage(self):
        # Arrange
        character = Character(
            4,
            "Link",
            120,
            20,
            12,
            11,
            10,
            100
        )

        # Act
        character.take_damage(50)

        # Assert
        assert character.hp == 62 # character.hp (100) - (damage (50) - character.def (12))

    def test_link_attacks_keese(self):
        # Arrange
        keese_character = Character(
            5,
            "Keese",
            50,
            9,
            3,
            11,
            5,
            None
        )
        link_character = Character(
            4,
            "Link",
            120,
            20,
            12,
            11,
            10,
            100
        )

        # Act
        link_character.attack(keese_character)

        # Assert
        assert keese_character.hp == 33 # keese_character.hp (50) - (damage alias link_character.str_ (20) - keese_character.def_ (3))
