"""
https://adventofcode.com/2021/day/8
"""

import re


class Decoder:
    """Decoder."""
    displayable_letters: str = "abcdefg"
    original_numbers_to_display: dict[int, str] = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }

    def __init__(self, encoded_numbers: list[str]) -> None:
        self.encoded_numbers = encoded_numbers
        self.wiring_old_new: dict[str, str] = {letter: None for letter in
                                               self.displayable_letters}
        self.display_to_numbers: dict[str, int] = None

    def determine_wiring(self) -> None:
        """Determines the connection between the original layout and the new
         layout."""
        encoded_1 = \
            [encoded_number for encoded_number in self.encoded_numbers if
             len(encoded_number) == len(
                 self.original_numbers_to_display[1])][0]
        encoded_7 = \
            [encoded_number for encoded_number in self.encoded_numbers if
             len(encoded_number) == len(
                 self.original_numbers_to_display[7])][0]
        encoded_8 = \
            [encoded_number for encoded_number in self.encoded_numbers if
             len(encoded_number) == len(
                 self.original_numbers_to_display[8])][0]

        self.wiring_old_new["a"] = set_to_single_element(
            set(encoded_7).difference(encoded_1))
        cf = set(encoded_1)
        abfg = set.intersection(
            *[set(encoded_number) for encoded_number in self.encoded_numbers if
              len(encoded_number) == len(
                  self.original_numbers_to_display[0])])  # 0, 6, 9
        adg = set.intersection(
            *[set(encoded_number) for encoded_number in self.encoded_numbers if
              len(encoded_number) == len(
                  self.original_numbers_to_display[2])])  # 2, 3, 5
        self.wiring_old_new["d"] = set_to_single_element(adg - abfg)
        self.wiring_old_new["g"] = set_to_single_element(
            adg - {self.wiring_old_new["a"], self.wiring_old_new["d"]})
        bf = abfg - adg
        self.wiring_old_new["f"] = set_to_single_element(bf & cf)
        self.wiring_old_new["b"] = set_to_single_element(
            bf - set(self.wiring_old_new["f"]))
        self.wiring_old_new["c"] = set_to_single_element(
            cf - set(self.wiring_old_new["f"]))
        self.wiring_old_new["e"] = set_to_single_element(
            set.difference(set(encoded_8),
                           *[set(val) for key, val in
                             self.wiring_old_new.items() if key != "e"]))

        self.display_to_numbers = {"".join(
            sorted([self.wiring_old_new[letter] for letter in string])): number
                                   for number, string in
                                   self.original_numbers_to_display.items()}

    def decode_number(self, encoded_number: str) -> int:
        """Decodes an encoded number.

        :param encoded_number: Encoded number
        :return: Decoded number
        """
        return self.display_to_numbers["".join(sorted(encoded_number))]


def data_input(filename: str = "data") -> list[tuple[list[str], list[str]]]:
    """Reads data.

    :param filename: Filename
    :return: List of list with encoded numbers and encoded output value
    """
    with open(filename) as file:
        pattern = re.compile(r"([a-z]+)")
        result: list[tuple[list[str], list[str]]] = []
        for row in file.read().splitlines():
            matches = re.findall(pattern, row)
            result.append((matches[:10], matches[10:]))
        return result


def flatten(lst: list[list]) -> list:
    """Flattens a list of list to a list.
    https://stackoverflow.com/a/952952

    :param lst: List of list
    :return: Flattened list
    """
    return [item for sublist in lst for item in sublist]


def set_to_single_element(set_with_one_element: set):
    """Returns the element of a set with only one element.

    :param set_with_one_element: Set with one element
    :return: The one element of the set
    """
    for element in set_with_one_element:
        return element


def determine_output_value(entry: tuple[list[str], list[str]]) -> int:
    """Determines the output value.

    :param entry: List with encoded numbers and encoded output value
    :return: Decoded output value
    """
    decoder = Decoder(entry[0])
    decoder.determine_wiring()

    return sum(decoder.decode_number(encoded_number) * 10 ** (
            len(entry[1]) - i - 1) for i, encoded_number in
               enumerate(entry[1]))


def part_1(data: list[tuple[list[str], list[str]]]) -> int:
    """Part 1.

    :param data:List of list with encoded numbers and encoded output value
    :return: Number of times the digits 1, 4, 7, 8 appear
    """
    number_dict = {number: len(string) for number, string in
                   Decoder.original_numbers_to_display.items() if
                   number in [1, 4, 7, 8]}
    flattened_output_list = flatten([tup[1] for tup in data])
    return sum(len(number_string) in number_dict.values() for number_string in
               flattened_output_list)


def part_2(data: list[tuple[list[str], list[str]]]) -> int:
    """Part 2.

    :param data: List of list with encoded numbers and encoded output value
    :return: Sum of all output values
    """
    return sum(determine_output_value(entry) for entry in data)


def main() -> None:
    """Main function."""
    data = data_input()
    print(part_1(data))
    data = data_input()
    print(part_2(data))


if __name__ == "__main__":
    main()
