import pathlib

from advent_of_code.year_2023.day_17.main import solution

if __name__ == "__main__":
    sample = pathlib.Path(__file__).parent / "sample.data"
    print(solution(input_=sample.read_text().strip()))
