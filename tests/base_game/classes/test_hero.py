from base_game.classes.hero import Hero


class TestHero:
    def test_init_with_hp(self):
        # Arrange
        # Act
        hero = Hero(
            5,
            "Link",
            50,
            9,
            3,
            11,
            5,
            45,
        )

        # Assert
        assert hero.identifier == 5
        assert hero.name == "Link"
        assert hero.max_health == 50
        assert hero.hp == 45
        assert hero.str_ == 9
        assert hero.def_ == 3
        assert hero.spd == 11
        assert hero.luck == 5

    def test_init_without_hp(self):
        # Arrange
        # Act
        hero = Hero(
            5,
            "Link",
            50,
            9,
            3,
            11,
            5,
        )

        # Assert
        assert hero.identifier == 5
        assert hero.name == "Link"
        assert hero.max_health == 50
        assert hero.hp == 50
        assert hero.str_ == 9
        assert hero.def_ == 3
        assert hero.spd == 11
        assert hero.luck == 5

    def test_create_hero_from_dict(self):
        data = {
            "identifier": 1,
            "name": "Link",
            "max_health": 120,
            "hp": 50,
            "str_": 20,
            "def_": 12,
            "spd": 11,
            "luck": 10
        }
        hero = Hero.from_dict(data)
        assert hero.identifier == 1
        assert hero.name == "Link"
        assert hero.max_health == 120
        assert hero.hp == 50
        assert hero.str_ == 20
        assert hero.def_ == 12
        assert hero.spd == 11
        assert hero.luck == 10

    def test_create_dict_from_hero(self):
        data = {
            "identifier": 1,
            "name": "Link",
            "max_health": 120,
            "hp": 120,
            "str_": 9,
            "def_": 3,
            "spd": 11,
            "luck": 5
        }
        hero = Hero(
            1,
            "Link",
            120,
            9,
            3,
            11,
            5,
            120,
        )
        hero_dict = hero.to_dict()
        assert hero_dict == data
