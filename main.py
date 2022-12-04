"""
Advent of code 2022!

https://adventofcode.com/
"""
import advent_of_code.solutions
import advent_of_code.utils


def main() -> None:
    """
    Print the solutions.
    """
    advent_of_code.utils.create_files(day=5)

    advent_of_code.solutions.print_all_solutions(
        print_all=False,
        use_sample=False,
        profile_solutions=False,
        repeat=10_000,
    )


if __name__ == "__main__":
    main()
