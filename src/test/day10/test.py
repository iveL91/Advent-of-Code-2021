"""
Tests for day 10.
"""

import unittest

from src.main.day10.main import data_input, part_1, part_2


class TestDay10(unittest.TestCase):
    """Test class for day 10."""

    directory: str = "../test/day10/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 26397),
            ("data", 268845)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                chunks = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(chunks))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 288957),
            ("data", 4038824534)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                chunks = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_2(chunks))


if __name__ == '__main__':
    unittest.main()
