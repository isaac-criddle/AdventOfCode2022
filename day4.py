import re

input_file = 'input4.txt'

input = []

with open(input_file) as f:
    for line in f:
        input.append(line.strip().split(','))

print(input)

pairs = []
for first, second in input:
    pairs.append([[int(s) for s in first.split("-")],
                  [int(s) for s in second.split("-")]])


count1 = 0
for pair1, pair2 in pairs:
    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1] \
        or pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        print(True)
        count1 += 1
    else:
        print(False)

print(count1)

count2 = 0
for pair1, pair2 in pairs:
    if(set(range(pair1[0], pair1[1] + 1)).intersection(
        set(range(pair2[0], pair2[1] + 1))) == set()): count2 += 1

print(1000 - count2)
