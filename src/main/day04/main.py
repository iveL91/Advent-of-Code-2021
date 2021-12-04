"""
https://adventofcode.com/2021/day/4
"""

import re
from typing import NamedTuple


class BoardSquare(NamedTuple):
    """Square on a Board."""
    number: int
    is_marked: bool = False


class Board(list[list[BoardSquare]]):
    """Board."""
    board_length: int = 5
    number: int
    _won_instruction: int = None

    def __init__(self, rows: list[str], number: int) -> None:
        super().__init__()
        self.number = number
        for row in rows:
            pattern = re.compile(r"\d+")
            matches = [BoardSquare(int(number)) for number in
                       re.findall(pattern, row)]
            self.append(matches)

    @property
    def is_playable(self) -> bool:
        """Check if the board is playable."""
        return self._won_instruction is None

    @property
    def score(self) -> int:
        """Get the score."""
        return self._sum_of_all_unmarked_numbers() * self._won_instruction

    def play(self, instruction: int) -> None:
        """One play on the board with the given instruction.

        A play consists of marking the squares corresponding to the instruction
        and saving the instruction if the board wins.

        :param instruction: Number to mark
        """
        if self._won_instruction:
            return
        self._mark_board(instruction)
        if self._is_won():
            self._won_instruction = instruction

    def _mark_board(self, instruction: int) -> None:
        for row_index, row in enumerate(self):
            for square_index, square in enumerate(row):
                if square.number == instruction:
                    self[row_index][square_index] = BoardSquare(square.number,
                                                                True)

    def _is_won(self) -> bool:
        return self._won_instruction \
               or self._is_won_on_row() \
               or self._is_won_on_column()

    def _is_won_on_row(self) -> bool:
        return any(all(marked for _, marked in row) for row in self)

    def _is_won_on_column(self) -> bool:
        return any(
            all(self[row_index][column_index].is_marked for row_index in
                range(Board.board_length)) for column_index in
            range(Board.board_length))

    def _sum_of_all_unmarked_numbers(self) -> int:
        return sum([sum(
            [number for number, marked in row if not marked]) for row in
            self])


class Game(NamedTuple):
    """Game."""
    instructions: list[int]
    boards: list[Board]
    won_board_numbers: list[int]


def data_input(filename: str = "data") -> Game:
    """Read game.

    :param filename: Filename
    :return: Game
    """
    with open(filename) as file:
        rows = file.read().splitlines()
        instructions = [int(number) for number in rows[0].split(",")]
        amount_of_boards = (len(rows[2:]) + 1) // (Board.board_length + 1)
        boards = [Board(rows[2 + i * (Board.board_length + 1):2 + i * (
                Board.board_length + 1) + Board.board_length], i) for i in
                  range(amount_of_boards)]
        return Game(instructions, boards, [])


def part_1(game: Game) -> int:
    """Part 1.

    :param game: Game
    :return: Final score of the first won game
    """
    boards = game.boards
    for instruction in game.instructions:
        for board in boards:
            board.play(instruction)
        game.won_board_numbers.extend(
            board.number for board in boards if not board.is_playable)
        boards = [board for board in boards if board.is_playable]
        if game.won_board_numbers:
            return game.boards[game.won_board_numbers[-1]].score
    raise Exception


def part_2(game: Game) -> int:
    """Part 2.

    :param game: Game
    :return: Final score of the last won game
    """
    boards = game.boards
    for instruction in game.instructions:
        if not boards:
            break
        for board in boards:
            board.play(instruction)
        game.won_board_numbers.extend(
            board.number for board in boards if not board.is_playable)
        boards = [board for board in boards if board.is_playable]
    if game.won_board_numbers:
        return game.boards[game.won_board_numbers[-1]].score
    raise Exception


def main() -> None:
    """Main function."""
    game = data_input()
    print(part_1(game))
    game = data_input()
    print(part_2(game))


if __name__ == "__main__":
    main()
