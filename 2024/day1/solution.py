import sys
import os
import math
from collections import Counter

example_path = os.path.dirname(__file__) + "/example"
challenge_file = os.path.dirname(__file__) + "/challenge"

file_path = example_path if sys.argv[2] == "example" else challenge_file

with open(file_path) as f:
    lines = f.readlines()



first = []
last = []

def parse_numbers(lines):
    for line in lines:
        line = line.split()

        first.append(int(line[0]))
        last.append(int(line[1]))

def step1():
    parse_numbers(lines)

    first.sort()
    last.sort()

    total = 0
    for i in range(len(first)):
        distance = math.fabs(first[i] - last[i])
        total += distance

    print(total)

def step2():
    parse_numbers(lines)

    last_count = Counter(last)

    total = 0
    for v in first:
        total += v * last_count.get(v, 0)

    print(total)



step = int(sys.argv[1])

if step == 1:
    step1()
elif step == 2:
    step2()
