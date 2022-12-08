input = []

with open('inputs/input7.txt') as f:
    for line in f:
        input.append(line.strip())

root = {}
curr_dir = root
ptr = []
for i in range(len(input)):
    line = input[i]
    cmd = line.split(' ')
    if cmd[0] == '$':
        print(str(cmd) + str(root))
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                if(len(ptr) > 0):
                    ptr.pop()
            elif cmd[2] != '/':
                ptr.append(cmd[2])
            curr_dir = root
            for dir in ptr:
                curr_dir = curr_dir[dir]
        elif cmd[1] == 'ls':
            ls_output = []
            next_cmd = []
            while i+1 < len(input):
                next_cmd = input[i + 1].split()
                if next_cmd[0] != '$':
                    ls_output.append(next_cmd)
                    i += 1
                else:
                    break
            for thing in ls_output:
                if thing[0] == 'dir':
                    if thing[1] not in curr_dir:
                        curr_dir[thing[1]] = {}
                else:
                    if thing[1] not in curr_dir:
                        curr_dir[thing[1]] = eval(thing[0])
                print(thing)
    else:
        pass


sizes = {}
def post_order(directory, title):
    size = 0
    for item in directory:
        if type(directory[item]) is dict:
            size += post_order(directory[item], title + "/" + item)
        else:
            size += directory[item]
    sizes[title] = size
    return size

print(post_order(root, 'root'))
print(sizes)


total = 0
for key in sizes:
    if sizes[key] <= 100000:
        total += sizes[key]

print(total)
print(sum(size for size in sizes.values() if size <= 100000))

print(30000000 - (70000000 - sizes['root']))

biggest = ['root', sizes['root']]
for key in sizes:
    if sizes[key] > 30000000 - (70000000 - sizes['root']):
        if sizes[key] < biggest[1]:
            biggest = [key, sizes[key]]

print(biggest)