import pathlib

from advent_of_code.year_2023.day_10.main import solution

if __name__ == "__main__":
    sample_1 = pathlib.Path(__file__).parent / "sample-1.data"
    sample_2 = pathlib.Path(__file__).parent / "sample-2.data"

    print(solution(input_=sample_1.read_text().strip()))
    print(solution(input_=sample_2.read_text().strip()))
