"""
Tests for day 12.
"""

import unittest

from src.main.day12.main import data_input, part_1, part_2


class TestDay12(unittest.TestCase):
    """Test class for day 12."""

    directory: str = "../test/day12/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 10),
            ("test_data_2", 19),
            ("test_data_3", 226),
            ("data", 3369)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                cave_system = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(cave_system))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 36),
            ("test_data_2", 103),
            ("test_data_3", 3509),
            ("data", 85883)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                cave_system = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(cave_system))


if __name__ == '__main__':
    unittest.main()
