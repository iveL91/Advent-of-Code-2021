"""
https://adventofcode.com/2021/day/1
"""


def data_input(filename: str = "data") -> list[int]:
    """Reading measurements of sea floor depths.

    :param filename: Filename
    :return: List of measurements of sea floor depths
    """
    with open(filename) as file:
        return [int(line) for line in file.read().splitlines()]


def part_1(measurements: list[int]) -> int:
    """Part 1.

    :param measurements: List of measurements of the sea floor depths
    :return: Number of times a depth measurement increases from the previous
             measurement
    """
    return sum(
        measurement_1 < measurement_2 for measurement_1, measurement_2 in
        zip(measurements, measurements[1:]))


def part_2(measurements: list[int]) -> int:
    """Part 2.

    :param measurements: List of measurements of the sea floor depths
    :return: Number of times a three-measurement sliding window increased
    """
    three_measurement_sliding_window = [
        sum(three_measurement_sliding_window) for
        three_measurement_sliding_window in
        zip(measurements, measurements[1:], measurements[2:])]
    return part_1(three_measurement_sliding_window)


def main() -> None:
    """Main function."""
    measurements = data_input()
    print(part_1(measurements))
    print(part_2(measurements))


if __name__ == "__main__":
    main()
