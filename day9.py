rope = []
for i in range(10):
    rope.append([0,0])
tail_pos = set()

input = []
with open('inputs/input9.txt') as f:
    for line in f:
        input.append(line.split())

for line in input:
    line[1] = eval(line[1])

print(input)

def resolve():

    for i in range(len(rope) - 1):
        head = rope[i]
        tail = rope[i + 1]

        delta = [head[0] - tail[0], head[1] - tail[1]]
        if abs(delta[0]) <= 1 and abs(delta[1]) <= 1:
            pass
        else:
            if delta[0] == 0: # vertical
                if delta[1] == 2:
                    tail[1] += 1
                elif delta[1] == -2:
                    tail[1] -= 1
                else:
                    print('bad')
            elif delta[1] == 0: # sideways
                if delta[0] == 2:
                    tail[0] += 1
                elif delta[0] == -2:
                    tail[0] -= 1
                else:
                    print('bad')
            else: # diagonal
                direction = [-1 if delta[0] < 1 else 1,
                             -1 if delta[1] < 1 else 1]
                tail[0] += direction[0]
                tail[1] += direction[1]

        if i == 8:
            tail_pos.add(tuple(tail))

for line in input:
    match line[0]:
        case 'R':
            for i in range(line[1]):
                rope[0][0] += 1
                resolve()
            print(line)
        case 'L':
            for i in range(line[1]):
                rope[0][0] -= 1
                resolve()
            print(line)
        case 'U':
            for i in range(line[1]):
                rope[0][1] += 1
                resolve()
            print(line)
        case 'D':
            for i in range(line[1]):
                rope[0][1] -= 1
                resolve()
            print(line)
        case _:
            print('Error')

print(len(tail_pos))