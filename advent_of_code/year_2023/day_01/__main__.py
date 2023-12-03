import pathlib

from advent_of_code.year_2023.day_01.main import solution

if __name__ == "__main__":
    for i in [0, 1]:
        sample = pathlib.Path(__file__).parent / f"sample-{i}.data"
        print(solution(input_=sample.read_text().strip())[i])
