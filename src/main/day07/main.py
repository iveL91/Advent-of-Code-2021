"""
https://adventofcode.com/2021/day/7
"""
from typing import Callable


def data_input(filename: str = "data") -> list[int]:
    """Read instructions.

    :param filename: Filename
    :return: Crab horizontal positions
    """
    with open(filename) as file:
        return [int(age) for age in file.read().split(",")]


def sum_of_first_n_integers(n: int) -> int:
    """Sum of the first n integers.

    We use the well-known formula
        sum_{k=1}^{n} k = n * (n+1) / 2.

    :param n: Integer
    :return: Sum of the first n integers
    """
    return n * (n + 1) // 2


def determine_minimum_fuel(crab_horizontal_positions: list[int],
                           fuel_function: Callable[[int], int]) -> int:
    different_crab_horizontal_positions = set(crab_horizontal_positions)
    total_fuels = [
        sum(fuel_function(abs(crab_horizontal_position - pos)) for pos in
            crab_horizontal_positions) for crab_horizontal_position
        in range(min(different_crab_horizontal_positions),
                 max(different_crab_horizontal_positions) + 1)]
    return min(total_fuels)


def part_1(crab_horizontal_positions: list[int]) -> int:
    """Part 1.

    :param crab_horizontal_positions: Crab horizontal positions
    :return: Minimum total fuel for a linear fuel consumption
    """
    return determine_minimum_fuel(crab_horizontal_positions, lambda n: n)


def part_2(crab_horizontal_positions: list[int]) -> int:
    """Part 2.

    :param crab_horizontal_positions: Crab horizontal positions
    :return: Minimum total fuel for a quadratic fuel consumption
    """
    return determine_minimum_fuel(crab_horizontal_positions,
                                  sum_of_first_n_integers)


def main() -> None:
    """Main function."""
    crab_horizontal_positions = data_input()
    print(part_1(crab_horizontal_positions))
    crab_horizontal_positions = data_input()
    print(part_2(crab_horizontal_positions))


if __name__ == "__main__":
    main()
