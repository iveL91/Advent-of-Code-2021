"""
https://adventofcode.com/2021/day/3
"""
from collections import Counter


class BinaryNumber(str):
    pass


def data_input(filename: str = "data") -> list[BinaryNumber]:
    """
    Reading diagnostic report.

    :param filename: Filename
    :return: Diagnostic report
    """
    with open(filename) as file:
        return [BinaryNumber(line) for line in file.read().splitlines()]


def determine_gamma_rate(diagnostic_report: list[BinaryNumber]) -> int:
    """
    Determine gamma rate.

    :param diagnostic_report: Diagnostic report
    :return: Gamma rate
    """
    binary_numbers = _transpose_binary_numbers(diagnostic_report)
    gamma_rate_binary: BinaryNumber = BinaryNumber(
        "".join([Counter(row).most_common(1)[0][0] for row in binary_numbers]))
    return int(gamma_rate_binary, 2)


def determine_epsilon_rate(diagnostic_report: list[BinaryNumber]) -> int:
    """
    Determine epsilon rate.

    :param diagnostic_report: Diagnostic report
    :return: Epsilon rate
    """
    binary_numbers = _transpose_binary_numbers(diagnostic_report)
    epsilon_rate_binary: BinaryNumber = BinaryNumber(
        "".join(
            ["1" if Counter(row).most_common(1)[0][0] == "0" else "0" for row
             in binary_numbers]))
    return int(epsilon_rate_binary, 2)


def determine_oxygen_generator_rating(
        diagnostic_report: list[BinaryNumber]) -> int:
    """
    Determine oxygen generator rating.

    :param diagnostic_report: Diagnostic report
    :return: Oxygen generator rating
    """
    available_binary_numbers = diagnostic_report.copy()
    for index in range(len(diagnostic_report[0])):
        binary_numbers = _transpose_binary_numbers(available_binary_numbers)
        most_common_bit = _determine_most_common_bit(binary_numbers[index])
        new_available_binary_numbers = [binary_number for binary_number in
                                        available_binary_numbers if
                                        binary_number[
                                            index] == most_common_bit]
        if len(new_available_binary_numbers) == 1:
            return int(new_available_binary_numbers[0], 2)
        available_binary_numbers = new_available_binary_numbers


def determine_co2_scrubber_rating(
        diagnostic_report: list[BinaryNumber]) -> int:
    """
    Determine CO2 scrubber rating.

    :param diagnostic_report: Diagnostic report
    :return: CO2 scrubber rating
    """
    available_binary_numbers = diagnostic_report.copy()
    for index in range(len(diagnostic_report[0])):
        binary_numbers = _transpose_binary_numbers(available_binary_numbers)
        least_common_bit = _determine_least_common_bit(binary_numbers[index])
        new_available_binary_numbers = [binary_number for binary_number in
                                        available_binary_numbers if
                                        binary_number[
                                            index] == least_common_bit]
        if len(new_available_binary_numbers) == 1:
            return int(new_available_binary_numbers[0], 2)
        available_binary_numbers = new_available_binary_numbers


def part_1(diagnostic_report: list[BinaryNumber]) -> int:
    """
    Part 1.

    :param diagnostic_report: Diagnostic report
    :return: Power consumption
    """
    return determine_gamma_rate(diagnostic_report) * determine_epsilon_rate(
        diagnostic_report)


def part_2(diagnostic_report: list[BinaryNumber]) -> int:
    """
    Part 2.

    :param diagnostic_report: Diagnostic report
    :return: Life support rating
    """
    return determine_oxygen_generator_rating(
        diagnostic_report) * determine_co2_scrubber_rating(diagnostic_report)


def main() -> None:
    """
    Main function.
    """
    diagnostic_report = data_input()
    print(part_1(diagnostic_report))
    print(part_2(diagnostic_report))


def _transpose_binary_numbers(diagnostic_report: list[BinaryNumber]) -> \
        list[BinaryNumber]:
    """
    Transpose a list of binary numbers.

    :param diagnostic_report: Diagnostic report
    :return: List of binary numbers
    """
    return [BinaryNumber(
        "".join([number_string[index] for number_string in diagnostic_report]))
        for index, _ in enumerate(diagnostic_report[0])]


def _determine_most_common_bit(binary_number: BinaryNumber) -> str:
    """
    Determine the most common bit of a binary number.

    :param binary_number: Binary number
    :return: The most common bit
    """
    count = Counter(binary_number)
    most_common_bits_in_row = count.most_common(2)
    if len(count) == 1:
        return most_common_bits_in_row[0][0]
    if most_common_bits_in_row[0][1] == most_common_bits_in_row[1][1]:
        return "1"
    return most_common_bits_in_row[0][0]


def _determine_least_common_bit(binary_number: BinaryNumber) -> str:
    """
    Determine the least common bit of a binary number.

    :param binary_number: Binary number
    :return: The least common bit
    """
    count = Counter(binary_number)
    most_common_bits_in_row = count.most_common(2)
    if len(count) == 1:
        least_common_bit = most_common_bits_in_row[0][0]
    else:
        if most_common_bits_in_row[0][1] == most_common_bits_in_row[1][1]:
            least_common_bit = "0"
        else:
            if most_common_bits_in_row[0][0] == "0":
                least_common_bit = "1"
            else:
                least_common_bit = "0"
    return least_common_bit


if __name__ == "__main__":
    main()
