import sys
import os

example_path = os.path.dirname(__file__) + "/example"
challenge_file = os.path.dirname(__file__) + "/challenge"

file_path = example_path if sys.argv[2] == "example" else challenge_file

with open(file_path) as f:
    lines = f.readlines()


def get_values(line):
    values = line.split()
    numerical_values = [int(value) for value in values]

    return numerical_values

def get_diffs_between_two_values(numerical_values):
    
    diffs = []
    
    for i in range(len(numerical_values) - 1):
        diffs.append(numerical_values[i] - numerical_values[i + 1])

    return diffs

def is_safe(numerical_values):
    diffs = get_diffs_between_two_values(numerical_values)

    for diff in diffs:
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    positive_diffs = [diff for diff in diffs if diff >= 0]
    negative_diffs = [diff for diff in diffs if diff < 0]

    return len(positive_diffs) == 0 or len(negative_diffs) == 0

def is_safe_after_removing_one(numerical_values):
    for i in range(len(numerical_values)):
        new_numerical_values = numerical_values[:i] + numerical_values[i + 1:]
        if is_safe(new_numerical_values):
            return True
    
    return False


def step1():
    true_counts = 0

    for line in lines:
        numerical_values = get_values(line)
        if is_safe(numerical_values):
            true_counts += 1
    
    print(true_counts)



def step2():
    safe_counts = 0

    for line in lines:
        numerical_values = get_values(line)
        if is_safe(numerical_values):
            safe_counts += 1
        else:
            if is_safe_after_removing_one(numerical_values):
                safe_counts += 1

    print(safe_counts)


step = int(sys.argv[1])

if step == 1:
    step1()
elif step == 2:
    step2()
