"""
Tests for day 11.
"""

import unittest

from src.main.day11.main import data_input, part_1, part_2


class TestDay11(unittest.TestCase):
    """Test class for day 11."""

    directory: str = "../test/day11/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 1656),
            ("data", 1649)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                octopuses_grid = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(octopuses_grid))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 195),
            ("data", 256)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                octopuses_grid = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(octopuses_grid))


if __name__ == '__main__':
    unittest.main()
