"""
https://adventofcode.com/2021/day/10
"""


def data_input(filename: str = "data") -> list[str]:
    """Reads chunks.

    :param filename: Filename
    :return: List of chunks
    """
    with open(filename) as file:
        return file.read().splitlines()


def determine_first_illegal_character(chunk: str) -> str:
    """Determines first illegal character.

    :param chunk: Chunk
    :return: First illegal character
    """
    closed_open: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    open_parantheses: list[str] = []
    for character in chunk:
        if character in closed_open.values():
            open_parantheses.append(character)
            continue
        if open_parantheses and closed_open[character] == open_parantheses[-1]:
            open_parantheses.pop()
            continue
        return character
    return ""


def determine_sequence_of_closing_characters(chunk: str) -> str:
    """Determines the sequence of closing characters for a chunk.

    :param chunk: Chunk
    :return: Sequence of closing characters
    """
    closed_open: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    open_closed: dict[str, str] = {value: key for key, value in
                                   closed_open.items()}
    open_parantheses: list[str] = []
    for character in chunk:
        if character in closed_open.values():
            open_parantheses.append(character)
            continue
        if open_parantheses and closed_open[character] == open_parantheses[-1]:
            open_parantheses.pop()
            continue
        return ""
    return "".join(
        open_closed[character] for character in reversed(open_parantheses))


def calculate_score(completion_string: str) -> int:
    """Calculates the score for a completion string.

    :param completion_string: Completion string
    :return: Total score
    """
    values: dict[str, int] = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    total_score: int = 0
    for character in completion_string:
        total_score *= 5
        total_score += values[character]
    return total_score


def part_1(chunks: list[str]) -> int:
    """Part 1.

    :param chunks: Chunks
    :return: Total syntax error score
    """
    points: dict[str, int] = {
        "": 0,
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return sum(
        points[determine_first_illegal_character(chunk)] for chunk in chunks)


def part_2(chunks: list[str]) -> int:
    """Part 2.

    :param chunks: Chunks
    :return: Middle score
    """
    completion_strings: list[str] = [
        determine_sequence_of_closing_characters(chunk) for
        chunk in chunks]
    total_points: list[int] = [calculate_score(completion_string) for
                               completion_string in completion_strings if
                               completion_string != ""]
    total_points.sort()
    return total_points[len(total_points) // 2]


def main() -> None:
    """Main function."""
    chunks = data_input()
    print(part_1(chunks))
    chunks = data_input()
    print(part_2(chunks))


if __name__ == "__main__":
    main()
