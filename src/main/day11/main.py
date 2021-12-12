"""
https://adventofcode.com/2021/day/11
"""
import dataclasses
from itertools import product
from typing import NamedTuple


class Position(NamedTuple):
    """Position."""
    row_index: int
    column_index: int


@dataclasses.dataclass
class Octopus:
    """Octopus."""
    energy_level: int
    position: Position
    has_flashed: bool = False

    def __hash__(self) -> int:
        return hash(self.position)


class OctopusesGrid(list[list[Octopus]]):
    """Grid of octopuses."""

    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.total_flashes: int = 0
        self.flashed_octopuses: set[Octopus] = None
        self.amount_of_steps: int = 0

    @property
    def grid_size(self) -> int:
        """Grid size.

        :return: Grid size.
        """
        return len(self) * len(self[0])

    def step(self) -> None:
        """Fulfills one step."""
        self.flashed_octopuses = set()
        self._increase_energy_levels_by_1()
        self._flash()
        self._add_flashes()
        self._reset_energy_levels()
        self.amount_of_steps += 1

    def _increase_energy_levels_by_1(self) -> None:
        """Increases all energy levels by 1."""
        for row in self:
            for octopus in row:
                octopus.has_flashed = False
                octopus.energy_level += 1

    def _propagate_flash(self, octopus: Octopus) -> None:
        """Propagates the flash of the given octopus through the grid.

        :param octopus: Flashed octopus
        """
        neighbors = self._determine_neighbors(octopus)
        for neighbor in neighbors:
            neighbor.energy_level += 1

        newly_flashed_neighbors: set[Octopus] = set()
        for neighbor in neighbors - self.flashed_octopuses:
            if neighbor.energy_level > 9:
                neighbor.has_flashed = True
                newly_flashed_neighbors.add(neighbor)
        self.flashed_octopuses.update(newly_flashed_neighbors)
        for newly_flashed_neighbor in newly_flashed_neighbors:
            self._propagate_flash(newly_flashed_neighbor)

    def _flash(self) -> None:
        """Lets the octopuses with enough energy flash."""
        for octopus in flatten(self):
            if octopus.energy_level > 9 and not octopus.has_flashed:
                octopus.has_flashed = True
                self.flashed_octopuses.add(octopus)
                self._propagate_flash(octopus)

    def _add_flashes(self) -> None:
        """Adds the number of flashed octopuses in a step to the total number
         of flashes."""
        self.total_flashes += len(self.flashed_octopuses)

    def _reset_energy_levels(self) -> None:
        """Resets the energy levels of the flashed octopuses in a step to 0."""
        for octopus in self.flashed_octopuses:
            octopus.energy_level = 0

    def _determine_neighbors(self, octopus: Octopus) -> set[Octopus]:
        """Determines the neighbors of the given octopus.

        :param octopus: Octopus
        :return: Neighbors of the given octopus
        """
        row_indices = set(
            min(max(octopus.position.row_index + row_offset, 0), len(self)) for
            row_offset in range(-1, 2))
        column_indices = set(
            min(max(octopus.position.column_index + column_offset, 0),
                len(self[0])) for column_offset in range(-1, 2))

        result: set[Octopus] = set()
        for row_index, column_index in product(row_indices, column_indices):
            try:
                if octopus.position.row_index == row_index \
                        and octopus.position.column_index == column_index:
                    continue
                result.add(self[row_index][column_index])
            except IndexError:
                pass
        return result


def flatten(lst: list[list]) -> list:
    """Flattens a list of list to a list.
    https://stackoverflow.com/a/952952

    :param lst: List of list
    :return: Flattened list
    """
    return [item for sublist in lst for item in sublist]


def data_input(filename: str = "data") -> OctopusesGrid:
    """Reads octopuses grid.

    :param filename: Filename
    :return: Octopuses grid
    """
    with open(filename) as file:
        return OctopusesGrid(
            [[Octopus(int(energy_level), Position(row_index, column_index)) for
              column_index, energy_level in enumerate(row)] for row_index, row
             in enumerate(file.read().splitlines())])


def part_1(octopuses_grid: OctopusesGrid) -> int:
    """Part 1.

    :param octopuses_grid: Octopuses grid
    :return: Total flashes after 100 steps
    """
    for _ in range(100):
        octopuses_grid.step()
    return octopuses_grid.total_flashes


def part_2(octopuses_grid: OctopusesGrid) -> int:
    """Part 2.

    :param octopuses_grid: Octopuses grid
    :return: First step during all octopuses flash
    """
    while octopuses_grid.flashed_octopuses is None or \
            len(octopuses_grid.flashed_octopuses) != octopuses_grid.grid_size:
        octopuses_grid.step()
    return octopuses_grid.amount_of_steps


def main() -> None:
    """Main function."""
    octopuses_grid = data_input()
    print(part_1(octopuses_grid))
    octopuses_grid = data_input()
    print(part_2(octopuses_grid))


if __name__ == "__main__":
    main()
