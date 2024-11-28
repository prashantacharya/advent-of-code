import sys
import os

example_path = os.path.dirname(__file__) + "/example"
challenge_file = os.path.dirname(__file__) + "/challenge"

file_path = example_path if sys.argv[2] == "example" else challenge_file

with open(file_path) as f:
    lines = f.readlines()


def step1():
    pass


def step2():
    pass


step = int(sys.argv[1])

if step == 1:
    step1()
elif step == 2:
    step2()
