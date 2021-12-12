"""
https://adventofcode.com/2021/day/5
"""

import re
from collections import defaultdict
from typing import NewType

Instruction = NewType("Instruction", tuple[complex, complex])


class Plane(defaultdict):
    """Plane."""

    def mark_horizontally(self,
                          instructions: list[Instruction]) -> None:
        """Mark plane with all horizontal instructions."""
        horizontal_instructions = [instruction for instruction in instructions
                                   if
                                   instruction[0].imag == instruction[1].imag]

        for line in horizontal_instructions:
            horizontal_dimensions = (int(min(line[0].real, line[1].real)),
                                     int(max(line[0].real, line[1].real)))

            for horizontal_index in range(horizontal_dimensions[0],
                                          horizontal_dimensions[1] + 1):
                self[complex(horizontal_index, line[0].imag)] += 1

    def mark_vertically(self,
                        instructions: list[Instruction]) -> None:
        """Mark plane with all vertical instructions."""
        vertical_instructions = [instruction for instruction in instructions if
                                 instruction[0].real == instruction[1].real]
        for line in vertical_instructions:
            vertical_dimensions = (int(min(line[0].imag, line[1].imag)),
                                   int(max(line[0].imag, line[1].imag)))

            for vertical_index in range(vertical_dimensions[0],
                                        vertical_dimensions[1] + 1):
                self[complex(line[0].real, vertical_index)] += 1

    def mark_diagonally(self,
                        instructions: list[Instruction]) -> None:
        """Mark plane with all diagonal instructions."""
        diagonal_instructions = [instruction for instruction in instructions if
                                 instruction[0].real != instruction[1].real and
                                 instruction[0].imag != instruction[1].imag]
        for line in diagonal_instructions:
            left_point = line[0] if line[0].real < line[1].real else line[1]
            right_point = line[1] if left_point == line[0] else line[0]

            direction: float = (right_point.imag - left_point.imag) / (
                    right_point.real - left_point.real)
            direction /= abs(direction)
            slope: complex = complex(1, direction)
            for i in range(int(abs(line[0].real - line[1].real)) + 1):
                self[left_point + i * slope] += 1

    def amount_of_points_with_at_least_two_overlaps(self) -> int:
        """Return the number of points where at least two lines overlap.

        :return: The number of points where at least two lines overlap
        """
        return sum(value >= 2 for value in self.values())


def data_input(filename: str = "data") -> list[Instruction]:
    """Read instructions.

    :param filename: Filename
    :return: Instructions
    """
    with open(filename) as file:
        pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
        instructions: list[Instruction] = []
        for row in file.read().splitlines():
            match = re.match(pattern, row)
            instructions.append(Instruction((complex(int(match.group(1)),
                                                     int(match.group(2))),
                                             complex(int(match.group(3)),
                                                     int(match.group(4))))))
        return instructions


def part_1(instructions: list[Instruction]) -> int:
    """Part 1.

    :param instructions: Instructions
    :return: The number of points where at least two lines overlap
    """
    plane = Plane(int)
    plane.mark_horizontally(instructions)
    plane.mark_vertically(instructions)
    return plane.amount_of_points_with_at_least_two_overlaps()


def part_2(instructions: list[Instruction]) -> int:
    """Part 2.

    :param instructions: Instructions
    :return: The number of points where at least two lines overlap
    """
    plane = Plane(int)
    plane.mark_horizontally(instructions)
    plane.mark_vertically(instructions)
    plane.mark_diagonally(instructions)
    return plane.amount_of_points_with_at_least_two_overlaps()


def main() -> None:
    """Main function."""
    instructions = data_input()
    print(part_1(instructions))
    instructions = data_input()
    print(part_2(instructions))


if __name__ == "__main__":
    main()
