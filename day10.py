X = 1
cycle = 1

input = []
with open('inputs/input10.txt') as f:
    for line in f:
        input.append(line.strip().split())

print(input)

strengths = []

pos = []
for i in range(40):
    pos.append('.')
for i in range(3):
    pos.append("#")

grid = []
for i in range(6):
    grid.append([])

def mark(cycle, X):
    y = int((cycle - 1) / 40)
    x = (cycle - 1) - (y * 40)
    print(x, y)
    if (cycle - 20) % 40 == 0:
        strengths.append((cycle, X))
    grid[y].append(render(x))

def render(x) -> str:
    if X == x or X - 1 == x or X + 1 == x:
        return '#'
    else:
        return '.'

i = 0
while i < len(input):
    line = input[i]
    if line[0] == 'noop':
        mark(cycle, X)
        cycle += 1
    elif line[0] == 'addx':
        mark(cycle, X)
        cycle += 1
        mark(cycle, X)
        cycle += 1

        X += eval(line[1])
    else: print('bad')

    i += 1

print(strengths)

metric = 0
for s in strengths:
    metric += s[0] * s[1]

print(metric)
for row in grid:
    for pixel in row:
        print(pixel, end = "")
    print()