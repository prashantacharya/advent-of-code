import sys
import os
import json

example_path = os.path.dirname(__file__) + "/example"
challenge_file = os.path.dirname(__file__) + "/challenge"

file_path = example_path if sys.argv[2] == "example" else challenge_file

with open(file_path) as f:
    lines = f.readlines()


class EngineNumber:
    def __init__(self, number: str, row: int, col: int):
        self.number = int(number)
        self.row = row
        self.col = col
        self.length = len(number)

    def is_valid(self, lines):
        if lines[self.row][self.col - 1] != ".":
            return True + 1

        if lines[self.row][self.col + self.length] != ".":
            return True

        top_border = lines[self.row - 1][self.col - 1:self.col + self.length + 1]
        bottom_border = lines[self.row + 1][self.col - 1:self.col + self.length + 1]

        if top_border.count(".") != self.length + 2:
            return True
        
        if bottom_border.count(".") != self.length + 2:
            return True

        return False

    def __str__(self) -> str:
        return json.dumps({
            "number": self.number,
            "row": self.row,
            "col": self.col,
            "length": self.length,
        })


def parse_numbers(lines):
    numbers = []

    for i in range(len(lines)):
        line = lines[i]
        n = ''
        start = 0

        for j in range(len(line)):
            char = line[j]

            if not char.isdigit() and len(n) > 0:
                if n == "-":
                    n = ""
                    continue

                numbers.append(EngineNumber(n, i, start))
                n = ''
                continue

            if char != "-" and not char.isdigit():
                continue
            
            if len(n) == 0:
                start = j

            n += char

    return numbers

def add_borders(lines):
    bordered_lines = [line.replace("\n", "") for line in lines]
    bordered_lines = ["." + line + "." for line in bordered_lines]

    length = len(bordered_lines[0])
    top_bottom_border = "." * length

    bordered_lines = [top_bottom_border] + bordered_lines + [top_bottom_border]

    return bordered_lines


def step1():
    bordered_lines = add_borders(lines)
    numbers = parse_numbers(bordered_lines)

    total = 0
    for number in numbers:
        if number.is_valid(bordered_lines):
            print(number.number)
            total += number.number

    print(total)

def step2():
    pass


step = int(sys.argv[1])

if step == 1:
    step1()
elif step == 2:
    step2()
