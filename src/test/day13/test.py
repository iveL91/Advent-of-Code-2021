"""
Tests for day 13.
"""

import unittest

from src.main.day13.main import data_input, part_1, part_2


class TestDay13(unittest.TestCase):
    """Test class for day 13."""

    directory: str = "../test/day13/"

    def test_part_1(self) -> None:
        """Testing part_1."""
        subtest_list: list[tuple[str, int]] = [
            ("test_data_1", 17),
            ("data", 735)
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                paper, instructions = data_input(self.directory + filename)
                self.assertEqual(expected_result, part_1(paper, instructions))

    def test_part_2(self) -> None:
        """Testing part_2."""
        subtest_list: list[tuple[str, str]] = [
            ("test_data_1", "O"),
            ("data", "UFRZKAUZ")
        ]
        for filename, expected_result in subtest_list:
            with self.subTest():
                paper, instructions = data_input(self.directory + filename)
                part_2(paper, instructions)
                # self.assertEqual(expected_result, part_2(data))


if __name__ == '__main__':
    unittest.main()
