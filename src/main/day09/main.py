"""
https://adventofcode.com/2021/day/9
"""

import math


class Heightmap(list[list[int]]):
    """Heightmap."""
    low_point_positions: list[tuple[int, int]] = None
    low_points: list[int] = None
    basins: dict[tuple[int, int], set[tuple[int, int]]] = None

    def determine_low_points(self) -> None:
        """Determines the low points of the heightmap."""
        self._determine_low_point_positions()
        self.low_points = [self[index_row][index_column] for
                           index_row, index_column in self.low_point_positions]

    def determine_basins(self) -> None:
        """Determines the basins."""
        self._determine_low_point_positions()
        self.basins = {low_point_position: {low_point_position} for
                       low_point_position in self.low_point_positions}
        for low_point_position in self.basins:
            self._determine_higher_surrounding_positions_for_position(
                low_point_position,
                low_point_position)

    def _determine_low_point_positions(self) -> None:
        """Determines the positions of the low points of the heightmap."""
        self.low_point_positions = []
        for index_row, row in enumerate(self):
            for index_column, _ in enumerate(row):
                if self._is_number_low_point(index_row, index_column):
                    self.low_point_positions.append((index_row, index_column))

    def _is_number_low_point(self, index_row: int, index_column: int) -> bool:
        """Checks if the number corresponding to the row and column index is a
        low point.

        :param index_row: Row index
        :param index_column: Column index
        :return:
        """
        return self[index_row][index_column] < min(
            self._get_up(index_column, index_row),
            self._get_down(index_column, index_row),
            self._get_left(index_column, index_row),
            self._get_right(index_column, index_row))

    def _get_up(self, index_column: int, index_row: int) -> int:
        """Gets the value of the up position to the given indices."""
        return self[index_row - 1][index_column] if index_row != 0 else 10

    def _get_down(self, index_column: int, index_row: int) -> int:
        """Gets the value of the down position to the given indices."""
        return self[index_row + 1][index_column] if index_row != len(
            self) - 1 else 10

    def _get_left(self, index_column: int, index_row: int) -> int:
        """Gets the value of the left position to the given indices."""
        return self[index_row][
            index_column - 1] if index_column != 0 else 10

    def _get_right(self, index_column: int, index_row: int) -> int:
        """Gets the value of the right position to the given indices."""
        return self[index_row][index_column + 1] if index_column != len(
            self[0]) - 1 else 10

    def _determine_higher_surrounding_positions_for_position(self,
                                                             low_point_position:
                                                             tuple[int, int],
                                                             position: tuple[
                                                                 int, int]) \
            -> None:
        """Determines the the surrounding positions for a given position which
         are higher than the given position. Furthermore, those positions are
         added to the basin corresponding to the low point position.
        
        :param low_point_position: Position of the low point
        :param position: Position
        """
        new_boundary = [pos for pos in self._determine_boundary(position) if
                        pos not in self.basins[low_point_position]]
        self.basins[low_point_position].update(new_boundary)
        for boundary_position in new_boundary:
            self._determine_higher_surrounding_positions_for_position(
                low_point_position,
                boundary_position)

    def _determine_boundary(self, position: tuple[int, int]) -> \
            list[tuple[int, int]]:
        """Returns list of positions which are adjacent to the given position
        and are not tops.

        :param position: Position on the heightmap
        :return: List of positions which are adjacent to the given position
        and are not tops
        """
        new_boundary = []
        if self._get_up(position[1], position[0]) < 9:
            new_boundary.append(
                (position[0] - 1, position[1]))
        if self._get_down(position[1], position[0]) < 9:
            new_boundary.append(
                (position[0] + 1, position[1]))
        if self._get_left(position[1], position[0]) < 9:
            new_boundary.append(
                (position[0], position[1] - 1))
        if self._get_right(position[1], position[0]) < 9:
            new_boundary.append(
                (position[0], position[1] + 1))
        return new_boundary


def data_input(filename: str = "data") -> Heightmap:
    """Reads heightmap.

    :param filename: Filename
    :return: Heightmap
    """
    with open(filename) as file:
        return Heightmap([[int(number) for number in row] for row in
                          file.read().splitlines()])


def part_1(heightmap: Heightmap) -> int:
    """Part 1.

    :param heightmap: Heightmap
    :return: Sum of the risk levels of all low points on the heightmap
    """
    heightmap.determine_low_points()
    risk_levels = [low_point + 1 for low_point in heightmap.low_points]
    return sum(risk_levels)


def part_2(heightmap: Heightmap) -> int:
    """Part 2.

    :param heightmap: Horizontal positions of the crabs
    :return: Product of the sizes of the three largest basins
    """
    heightmap.determine_basins()
    three_largest_basins = sorted(
        [len(basin) for basin in heightmap.basins.values()])[-3:]
    return math.prod(three_largest_basins)


def main() -> None:
    """Main function."""
    heightmap = data_input()
    print(part_1(heightmap))
    heightmap = data_input()
    print(part_2(heightmap))


if __name__ == "__main__":
    main()
