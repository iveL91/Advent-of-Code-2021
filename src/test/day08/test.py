"""
Tests for day 08.
"""

import unittest

from src.main.day08.main import data_input, part_1, part_2


class TestDay08(unittest.TestCase):
    """Test class for day 08."""

    directory: str = "../test/day08/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_2", 26),
            ("data", 362)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                data = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(data))

    # @unittest.skip
    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 5353),
            ("test_data_2", 61229),
            ("data", 1020159)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                lanternfish_school = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(lanternfish_school))


if __name__ == '__main__':
    unittest.main()
