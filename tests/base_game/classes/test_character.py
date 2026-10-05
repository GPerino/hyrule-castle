import pytest

from base_game.classes.character import Character


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

    def test_init_link(self):
        # Arrange
        link_id: int = 1
        link_name: str = "Link"
        link_max_health: int = 120
        link_str: int = 20
        link_def: int = 12
        link_spd: int = 11
        link_luck: int = 10
        link_hp: int = 100

        # Act
        character = Character(
            link_id,
            link_name,
            link_max_health,
            link_str,
            link_def,
            link_spd,
            link_luck,
            link_hp
        )

        # Assert
        assert character.id == link_id
        assert character.name == link_name
        assert character.max_health == link_max_health
        assert character.hp == link_hp
        assert character.str_ == link_str
        assert character.def_ == link_def
        assert character.spd == link_spd
        assert character.luck == link_luck

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
        assert character.hp == 62 # character.hp (100) - damage (50) - character.def (12)

# def test_link_attacks_keese(self):
#     # Arrange
#     keese_character = Character(
#         5,
#         "Keese",
#         50,
#         9,
#         3,
#         11,
#         5,
#         None
#     )
#     link_character = Character(
#         4,
#         "Link",
#         120,
#         20,
#         12,
#         11,
#         10,
#         100
#     )
#
#     # Act
#     link_character.attack(keese_character)
#
#     # Assert
#     assert keese_character.hp == 73 # keese_character.hp (100) - link_character.str_ (20) - keese_character.def_ (3)
