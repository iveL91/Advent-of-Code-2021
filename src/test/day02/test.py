"""
Tests for day 02.
"""

import unittest

from src.main.day02.main import data_input, part_1, part_2


class TestDay02(unittest.TestCase):
    """
    Test class for day 02.
    """

    def test_part_1(self) -> None:
        """
        Testing part 1
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 150),
                                               ("data", 1488669)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                commands = data_input("../test/day02/" + filename)
                self.assertEqual(expected_result, part_1(commands))

    def test_part_2(self) -> None:
        """
        Testing part 2
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 900),
                                               ("data", 1176514794)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                commands = data_input("../test/day02/" + filename)
                self.assertEqual(expected_result, part_2(commands))


if __name__ == '__main__':
    unittest.main()
