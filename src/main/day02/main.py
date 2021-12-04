"""
https://adventofcode.com/2021/day/2
"""

from typing import NamedTuple


class Command(NamedTuple):
    """Command."""
    movement: str
    amount: int


def data_input(filename: str = "data") -> list[Command]:
    """Reading commands from data.

    :param filename: Filename
    :return: List of commands
    """
    with open(filename) as file:
        return [Command(line.split(" ")[0], int(line.split(" ")[1])) for line
                in file.read().splitlines()]


def part_1(commands: list[Command]) -> int:
    """Part 1.

    :param commands: List of commands
    :return: Product of final horizontal position and final depth
    """
    commands_dict: dict[str, complex] = {"forward": 1,
                                         "down": 1j,
                                         "up": -1j}
    position: complex = sum(
        commands_dict[command.movement] * command.amount for command in
        commands)

    return int(position.real * position.imag)


def part_2(commands: list[Command]) -> int:
    """Part 2.

    :param commands: List commands
    :return: Product of final horizontal position and final depth
    """
    commands_dict: dict[str, int] = {"forward": 1,
                                     "down": 1,
                                     "up": -1}

    position: complex = 0
    aim = 0

    for command in commands:
        if command.movement in ["down", "up"]:
            aim += commands_dict[command.movement] * command.amount
        if command.movement == "forward":
            position += command.amount * complex(1, aim)

    return int(position.real * position.imag)


def main() -> None:
    """Main function."""
    commands = data_input()
    print(part_1(commands))
    print(part_2(commands))


if __name__ == "__main__":
    main()
