"""
Tests for day 04.
"""

import unittest

from src.main.day04.main import data_input, part_1, part_2


class TestDay04(unittest.TestCase):
    """Test class for day 04."""

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [("test_data_1", 4512),
                                               ("data", 2496)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                game = data_input("../test/day04/" + filename)
                self.assertEqual(expected_result, part_1(game))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [("test_data_1", 1924),
                                               ("data", 25925)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                game = data_input("../test/day04/" + filename)
                self.assertEqual(expected_result, part_2(game))


if __name__ == '__main__':
    unittest.main()
