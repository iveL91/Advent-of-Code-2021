"""
Tests for day 01.
"""

import unittest

from src.main.day01.main import data_input, part_1, part_2


class TestDay01(unittest.TestCase):
    """
    Test class for day 01.
    """

    def test_part_1(self) -> None:
        """
        Testing part 1
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 7),
                                               ("data", 1624)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                measurements = data_input("../test/day01/" + filename)
                self.assertEqual(expected_result, part_1(measurements))

    def test_part_2(self) -> None:
        """
        Testing part 2
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 5),
                                               ("data", 1653)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                measurements = data_input("../test/day01/" + filename)
                self.assertEqual(expected_result, part_2(measurements))


if __name__ == '__main__':
    unittest.main()
