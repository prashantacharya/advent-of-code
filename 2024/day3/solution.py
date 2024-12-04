import re 
import sys
import os

example_path = os.path.dirname(__file__) + "/example"
challenge_file = os.path.dirname(__file__) + "/challenge"

file_path = example_path if sys.argv[2] == "example" else challenge_file

with open(file_path) as f:
    lines = f.readlines()

def parser(line):
    pattern = r"(mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\))"
    
    line = re.findall(pattern, line)

    return line

def get_nums_to_mul(statement):
    pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'
    match = re.findall(pattern, statement)

    return match[0]

def get_mul_statements(lines):
    pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'

    mul_statements = []
    for line in lines:
        match = re.findall(pattern, line)
        for m in match:
            mul_statements.append((m[0],m[1]))

    return mul_statements


def step1():
    mul_statements = get_mul_statements(lines)

    total = 0
    for mul_statement in mul_statements:
        a,b = mul_statement
        total += int(a) * int(b)

    print(total)

def step2():
    is_disabled = False
    total = 0
    for line in lines:
        for statement in parser(line):
            if statement == "do()":
                is_disabled = False
                continue

            if is_disabled:
                continue

            if statement == "don't()":
                is_disabled = True
                continue

            a,b = get_nums_to_mul(statement)
            total += int(a) * int(b)
            
    print(total)


step = int(sys.argv[1])

if step == 1:
    step1()
elif step == 2:
    step2()
