"""
Tests for day 06.
"""

import unittest

from src.main.day06.main import data_input, part_1, part_2, LanternfishSchool


class TestDay06(unittest.TestCase):
    """Test class for day 06."""

    directory: str = "../test/day06/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 5934),
            ("data", 388739)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                lanternfish_school = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(lanternfish_school))

    def test_amount_of_lanternfish_for_one(self):
        """Testing get_amount_of_lanternfish for one fish."""
        subtest_list: list[tuple[int, int, int]] = [
            (3, 1, 1),
            (3, 2, 1),
            (3, 3, 1),
            (3, 4, 2),
            (3, 5, 2),
            (3, 6, 2),
            (3, 10, 2),
            (3, 11, 3),
            (3, 12, 3),
            (3, 13, 4)
        ]
        for start_age, days, expected_result in subtest_list:
            with self.subTest():
                lantern_school = LanternfishSchool([start_age])
                self.assertEqual(expected_result,
                                 lantern_school
                                 .get_amount_of_lanternfish(days))

    def test_amount_of_lanternfish(self):
        """Testing get_amount_of_lanternfish for several fish."""
        subtest_list: list[tuple[str, int, int]] = [
            ("test_data_1", 1, 5),
            ("test_data_1", 2, 6),
            ("test_data_1", 3, 7),
            ("test_data_1", 4, 9),
            ("test_data_1", 5, 10),
            ("test_data_1", 6, 10),
            ("test_data_1", 7, 10),
            ("test_data_1", 8, 10),
            ("test_data_1", 9, 11),
            ("test_data_1", 10, 12),
            ("test_data_1", 11, 15),
            ("test_data_1", 12, 17),
            ("test_data_1", 13, 19),
            ("test_data_1", 14, 20),
            ("test_data_1", 15, 20),
            ("test_data_1", 16, 21),
            ("test_data_1", 17, 22),
            ("test_data_1", 18, 26),
            ("test_data_1", 80, 5934),
            ("data", 80, 388739)
        ]
        for filename, days, expected_result in subtest_list:
            with self.subTest():
                lanternfish_school = data_input(self.directory + filename)
                self.assertEqual(expected_result,
                                 lanternfish_school
                                 .get_amount_of_lanternfish(days))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 26_984_457_539),
            ("data", 1_741_362_314_973)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                lanternfish_school = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(lanternfish_school))


if __name__ == '__main__':
    unittest.main()
