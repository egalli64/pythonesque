"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque exercism folder

Tisbury Treasure Hunt https://exercism.org/tracks/python/exercises/tisbury-treasure-hunt

Tuples
"""
from tisbury_treasure_hunt import *


class TestGivenSolutions:
    def test_get_coordinate(self):
        assert get_coordinate(("Scrimshawed Whale Tooth", "2A")) == "2A"

    def test_convert_coordinate(self):
        assert convert_coordinate("2A") == ("2", "A")

    def test_compare_records_1(self):
        left = ("Brass Spyglass", "4B")
        right = ("Seaside Cottages", ("1", "C"), "blue")

        assert compare_records(left, right) is False

    def test_compare_records_2(self):
        left = ("Model Ship in Large Bottle", "8A")
        right = ("Harbor Managers Office", ("8", "A"), "purple")

        assert compare_records(left, right) is True

    def test_create_record_1(self):
        left = ("Brass Spyglass", "4B")
        right = ("Abandoned Lighthouse", ("4", "B"), "Blue")
        expected = ("Brass Spyglass", "4B", "Abandoned Lighthouse", ("4", "B"), "Blue")
        assert create_record(left, right) == expected

    def test_create_record_2(self):
        left = ("Brass Spyglass", "4B")
        right = ("Seaside Cottages", ("1", "C"), "blue")
        assert create_record(left, right) == "not a match"

    def test_clean_up(self):
        group = (("Brass Spyglass", "4B", "Abandoned Lighthouse", ("4", "B"), "Blue"),
                 ("Vintage Pirate Hat", "7E", "Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange"),
                 ("Crystal Crab", "6A", "Old Schooner", ("6", "A"), "Purple"))
        expected = """('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')
"""
        assert clean_up(group) == expected
