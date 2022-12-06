import re

test = False

with open("test5.txt" if test else "input5.txt") as f:
    input = f.readlines()

stacks_t = input[0:(8 if not test else 3)]
for line in stacks_t:
    line = line.strip()
moves = input[(10 if not test else 5):]

stacks_input = [[] for j in range(0, max(len(elem) for elem in stacks_t))]

for i in range(0, len(stacks_t)):
    line = stacks_t[i]
    for j in range(0, len(line)):
        character = line[j]
        print(j)
        stacks_input[j].insert(0, character)

stacks = [j for j in stacks_input if j[0] not in ('', ' ', '[', ']', '\n') and j[0]]

for i in range(len(stacks)):
    while stacks[i][len(stacks[i]) - 1] in (' ', ''):
        stacks[i].pop()

def move_stacks(count, first, second):
    first_idx = first - 1
    second_idx = second - 1

    claw = []
    for i in range(count):
        claw.append(stacks[first_idx].pop())
    for item in reversed(claw):
        stacks[second_idx].append(item)

for move in moves:
    count, first, second = tuple(map(int, re.split(r'\D+', move)[1:4]))
    move_stacks(count, first, second)

for stack in stacks:
    print(stack[len(stack) - 1], end="")