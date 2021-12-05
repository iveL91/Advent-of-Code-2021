"""
Tests for day 05.
"""

import unittest

from src.main.day05.main import data_input, part_1, part_2


class TestDay05(unittest.TestCase):
    """Test class for day 05."""

    directory: str = "../test/day05/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [("test_data_1", 5),
                                               ("data", 6548)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                game = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(game))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [("test_data_1", 12),
                                               ("data", 19663)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                game = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(game))


if __name__ == '__main__':
    unittest.main()
