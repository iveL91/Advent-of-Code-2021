"""
https://adventofcode.com/2021/day/13
"""

import re
from typing import NamedTuple


class Position(NamedTuple):
    """Position."""
    x: int
    y: int


class FoldingInstruction(NamedTuple):
    """Instruction."""
    axis: str
    fold_index: int


class Paper:
    """Paper."""

    def __init__(self, dots: set[Position]) -> None:
        self.dots: set[Position] = dots

    def fold(self, instruction: FoldingInstruction) -> None:
        """Folds the paper following the instruction.

        :param instruction: Instruction
        """
        if instruction.axis == "x":
            self._fold_along_x_axis(instruction)
        if instruction.axis == "y":
            self._fold_along_y_axis(instruction)

    def print(self) -> None:
        """Prints the paper to the console to make it visible."""
        output: list[str] = []
        for row_index in range(max(dot.y for dot in self.dots) + 1):
            row = ""
            for column_index in range(max(dot.x for dot in self.dots) + 1):
                if Position(column_index, row_index) in self.dots:
                    row += "#"
                else:
                    row += "."
            output.append(row)
        for row in output:
            print(row)

    def _fold_along_x_axis(self, instruction: FoldingInstruction) -> None:
        new_dots: set[Position] = set()
        for dot in self.dots:
            if dot.x > instruction.fold_index:
                new_dots.add(
                    Position(dot.x - 2 * (dot.x - instruction.fold_index),
                             dot.y))
            else:
                new_dots.add(dot)
        self.dots = new_dots

    def _fold_along_y_axis(self, instruction: FoldingInstruction) -> None:
        new_dots: set[Position] = set()
        for dot in self.dots:
            if dot.y > instruction.fold_index:
                new_dots.add(
                    Position(dot.x,
                             dot.y - 2 * (dot.y - instruction.fold_index)))
            else:
                new_dots.add(dot)
        self.dots = new_dots


def data_input(filename: str = "data") -> \
        tuple[Paper, list[FoldingInstruction]]:
    """Reads paper and folding instructions.

    :param filename: Filename
    :return: Paper and folding instructions
    """
    with open(filename) as file:
        rows = file.read().splitlines()
        split_index = rows.index("")
        dots: set[Position] = set()
        for row in rows[:split_index]:
            x, y = row.split(",")
            dots.add(Position(int(x), int(y)))
        instructions: list[FoldingInstruction] = []
        pattern = re.compile(r"[xy]=\d+")
        for row in rows[split_index + 1:]:
            axis, index = re.search(pattern, row).group(0).split("=")
            instructions.append(FoldingInstruction(axis, int(index)))
        return Paper(dots), instructions


def part_1(paper: Paper, instructions: list[FoldingInstruction]) -> int:
    """Part 1.

    :param paper: Paper
    :param instructions: Folding instructions
    :return: Number of dots after first folding
    """
    paper.fold(instructions[0])
    return len(paper.dots)


def part_2(paper: Paper, instructions: list[FoldingInstruction]) -> None:
    """Part 2.

    :param paper: Paper
    :param instructions: Folding instructions
    :return: Print of the letters represented by the dots in the folded paper
    """
    for instruction in instructions:
        paper.fold(instruction)
    paper.print()


def main() -> None:
    """Main function."""
    paper, instructions = data_input()
    print(part_1(paper, instructions))
    paper, instructions = data_input()
    part_2(paper, instructions)


if __name__ == "__main__":
    main()
