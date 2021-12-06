"""
https://adventofcode.com/2021/day/6
"""

from collections import Counter
from functools import lru_cache


class LanternfishSchool:
    """Lanternfish school."""
    initial_evolution_period: int = 9
    evolution_period: int = 7

    initial_ages_of_lanternfishes: list[int]
    amount_of_lanternfishes: int

    def __init__(self, initial_ages_of_lanternfishes: list[int]) -> None:
        self.initial_ages_of_lanternfishes = initial_ages_of_lanternfishes
        self.amount_of_lanternfishes = len(initial_ages_of_lanternfishes)

    def get_amount_of_lanternfish(self, days: int) -> int:
        """Get amount of lanternfish for given amount of days

        :param days: Amount of days
        :return: Amount of lanternfish for given amount of days
        """
        count_of_different_ages = Counter(self.initial_ages_of_lanternfishes)
        return sum(
            self._amount_of_lanternfish_for_one_fish(age, days) * amount for
            age, amount in count_of_different_ages.items())

    @lru_cache(maxsize=256)
    def _amount_of_lanternfish_for_one_fish(self, start_age: int,
                                            days: int) -> int:
        days -= start_age + 1
        if days < 0:
            return 1
        amount: int = days // self.evolution_period + 1
        return sum(self._amount_of_lanternfish_for_one_fish(
            self.initial_evolution_period - 1,
            days - i * self.evolution_period)
                   for i in range(amount)) + 1


def data_input(filename: str = "data") -> LanternfishSchool:
    """Read instructions.

    :param filename: Filename
    :return: Instructions
    """
    with open(filename) as file:
        return LanternfishSchool([int(age) for age in file.read().split(",")])


def part_1(lanternfish_school: LanternfishSchool) -> int:
    """Part 1.

    :param lanternfish_school: Lanternfish school
    :return: The number of lanternfish after 80 days
    """
    return lanternfish_school.get_amount_of_lanternfish(80)


def part_2(lanternfish_school: LanternfishSchool) -> int:
    """Part 2.

    :param lanternfish_school: Lanternfish school
    :return: The number of lanternfish after 256 days
    """
    return lanternfish_school.get_amount_of_lanternfish(256)


def main() -> None:
    """Main function."""
    lanternfish_school = data_input()
    print(part_1(lanternfish_school))
    lanternfish_school = data_input()
    print(part_2(lanternfish_school))


if __name__ == "__main__":
    main()
