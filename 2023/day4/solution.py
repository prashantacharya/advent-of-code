import sys
import os

example_path = os.path.dirname(__file__) + "/example"
challenge_file = os.path.dirname(__file__) + "/challenge"

file_path = example_path if sys.argv[2] == "example" else challenge_file

with open(file_path) as f:
    lines = f.readlines()


def process_card(card):
    a = card.split(":")[-1].strip()
    [nums, winning_nums] = a.split("|")
    nums = nums.split()
    winning_nums = winning_nums.split()

    nums = [int(x) for x in nums]
    winning_nums = [int(x) for x in winning_nums]

    count = 0
    winning_nums_set = set(winning_nums)

    for num in nums:
        if num in winning_nums_set:
            count += 1
    
    if count == 0:
        return 0

    return count



def step1():
    total = 0
    for card in lines:
        score = process_card(card)

        if score == 0:
            continue

        total += 2 ** (score - 1)

    print(total)


def step2():
    cards = {}
    for i in range(len(lines)):
        cards[i] = 1 

    for i in range(len(lines)):
        score = process_card(lines[i])

        if score == 0:
            continue
        
        for j in range(i+1, i + score + 1):
            cards[j] += cards[i]


    print(cards)
    
    total = 0
    for card, value in cards.items():
        total += value
    
    print(total)


step = int(sys.argv[1])

if step == 1:
    step1()
elif step == 2:
    step2()


print("Done!", file_path)
