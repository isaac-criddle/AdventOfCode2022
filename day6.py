with open('inputs/input6.txt') as f:
    file = f.readlines()[0]

print(file)

start = []
for i in range(0, len(file)):
    if i < 14:
        start.insert(0, file[i])
        print(start)
    else:
        start.pop()
        start.insert(0, file[i])
        print(start)
        if len(set(start)) == 14:
            print(i + 1)
            break