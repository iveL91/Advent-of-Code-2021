"""
Tests for day 07.
"""

import unittest

from src.main.day07.main import data_input, part_1, part_2


class TestDay07(unittest.TestCase):
    """Test class for day 07."""

    directory: str = "../test/day07/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 37),
            ("data", 325528)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                lanternfish_school = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(lanternfish_school))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 168),
            ("data", 85015836)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                lanternfish_school = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(lanternfish_school))


if __name__ == '__main__':
    unittest.main()
