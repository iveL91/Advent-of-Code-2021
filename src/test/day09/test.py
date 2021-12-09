"""
Tests for day 09.
"""

import unittest

from src.main.day09.main import data_input, part_1, part_2


class TestDay09(unittest.TestCase):
    """Test class for day 09."""

    directory: str = "../test/day09/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 15),
            ("data", 452)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                data = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(data))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 1134),
            ("data", 1263735)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                area = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(area))


if __name__ == '__main__':
    unittest.main()
