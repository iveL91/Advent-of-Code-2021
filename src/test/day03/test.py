"""
Tests for day 03.
"""

import unittest

from src.main.day03.main import data_input, \
    determine_gamma_rate, determine_epsilon_rate, part_1, \
    determine_oxygen_generator_rating, determine_co2_scrubber_rating, part_2


class TestDay03(unittest.TestCase):
    """
    Test class for day 03.
    """

    def test_determine_gamma_rate(self) -> None:
        """
        Testing determine_gamma_rate
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 22)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                diagnostic_report = data_input("../test/day03/" + filename)
                self.assertEqual(expected_result,
                                 determine_gamma_rate(diagnostic_report))

    def test_determine_epsilon_rate(self) -> None:
        """
        Testing determine_epsilon_rate
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 9)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                diagnostic_report = data_input("../test/day03/" + filename)
                self.assertEqual(expected_result,
                                 determine_epsilon_rate(diagnostic_report))

    def test_part_1(self) -> None:
        """
        Testing part_1
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 198),
                                               ("data", 2261546)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                diagnostic_report = data_input("../test/day03/" + filename)
                self.assertEqual(expected_result, part_1(diagnostic_report))

    def test_determine_oxygen_generator_rating(self) -> None:
        """
        Testing determine_oxygen_generator_rating
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 23)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                diagnostic_report = data_input("../test/day03/" + filename)
                self.assertEqual(expected_result,
                                 determine_oxygen_generator_rating(
                                     diagnostic_report))

    def test_determine_co2_scrubber_rating(self) -> None:
        """
        Testing determine_co2_scrubber_rating
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 10)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                diagnostic_report = data_input("../test/day03/" + filename)
                self.assertEqual(expected_result,
                                 determine_co2_scrubber_rating(
                                     diagnostic_report))

    def test_part_2(self) -> None:
        """
        Testing part_2
        """
        subtest_list: list[tuple[str, int]] = [("test_data_1", 230),
                                               ("data", 6775520)]
        for filename, expected_result in subtest_list:
            with self.subTest():
                diagnostic_report = data_input("../test/day03/" + filename)
                self.assertEqual(expected_result, part_2(diagnostic_report))


if __name__ == '__main__':
    unittest.main()
