"""
https://adventofcode.com/2021/day/12
"""

import re
from collections import defaultdict


class CaveSystem:
    """Cave system."""

    def __init__(self, connections: list[tuple[str, ...]]):
        self.connected_to: defaultdict[str, set[str]] = defaultdict(set[str])
        for connection in connections:
            self.connected_to[connection[0]].add(connection[1])
            self.connected_to[connection[1]].add(connection[0])
        self.paths: list[list[str]] = []

    def determine_paths(self, current_path: list[str] = None,
                        small_caves_can_be_visited_twice=True) -> None:
        """Determines all possible paths from start to end.

        :param current_path: Currently processed path
        :param small_caves_can_be_visited_twice: Indicates if one small cave in
         the path can be visited twice
        """
        if current_path is None:
            current_path = ["start"]
        for connected_cave in self.connected_to[current_path[-1]]:
            if connected_cave == "start":
                continue
            if connected_cave == "end":
                self.paths.append(current_path + [connected_cave])
                continue
            if connected_cave.islower() and connected_cave in current_path:
                if not small_caves_can_be_visited_twice:
                    continue
                self.determine_paths(current_path + [connected_cave], False)
            else:
                self.determine_paths(current_path + [connected_cave],
                                     small_caves_can_be_visited_twice)


def data_input(filename: str = "data") -> CaveSystem:
    """Reads connections and returns the corresponding cave system.

    :param filename: Filename
    :return: Cave system
    """
    with open(filename) as file:
        pattern = re.compile(r"([A-Za-z]+)-([A-Za-z]+)")
        connections = []
        for row in file.read().splitlines():
            if (match := re.match(pattern, row)) is not None:
                connections.append(match.group(1, 2))
        return CaveSystem(connections)


def part_1(cave_system: CaveSystem) -> int:
    """Part 1.

    :param cave_system: Cave system
    :return: Number of paths from start to end where small caves can only be
     visited once.
    """
    cave_system.determine_paths(small_caves_can_be_visited_twice=False)
    return len(cave_system.paths)


def part_2(cave_system: CaveSystem) -> int:
    """Part 2.

    :param cave_system: Cave system
    :return: Number of paths from start to end where one small cave can be
     visited twice and the others can only be visited once.
    """
    cave_system.determine_paths(small_caves_can_be_visited_twice=True)
    return len(cave_system.paths)


def main() -> None:
    """Main function."""
    octopuses_grid = data_input()
    print(part_1(octopuses_grid))
    octopuses_grid = data_input()
    print(part_2(octopuses_grid))


if __name__ == "__main__":
    main()
