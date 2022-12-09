input = []
with open('inputs/input8.txt') as f:
    for line in f:
        input.append(line.strip())

visible = []
grid = []
for line in input:
        row = []
        row_visible = []
        for char in line:
            row.append(eval(char))
            row_visible.append(False)
        grid.append(row)
        visible.append(row_visible)

row_num = len(grid)
col_num = len(grid[0])

prev = []
for i in range(col_num):
    prev.append(-1)
for row_idx in range(row_num):
    for col_idx in range(col_num):
        if prev[col_idx] < grid[row_idx][col_idx]:
            prev[col_idx] = grid[row_idx][col_idx]
            visible[row_idx][col_idx] = True

prev = []
for i in range(col_num):
    prev.append(-1)
for row_idx in range(row_num-1, 0, -1):
    for col_idx in range(col_num):
        if prev[col_idx] < grid[row_idx][col_idx]:
            prev[col_idx] = grid[row_idx][col_idx]
            visible[row_idx][col_idx] = True

prev = []
for i in range(row_num):
    prev.append(-1)
for row_idx in range(row_num):
    for col_idx in range(col_num):
        if prev[row_idx] < grid[row_idx][col_idx]:
            prev[row_idx] = grid[row_idx][col_idx]
            visible[row_idx][col_idx] = True

prev = []
for i in range(row_num):
    prev.append(-1)
for row_idx in range(row_num):
    for col_idx in range(col_num-1, 0, -1):
        if prev[row_idx] < grid[row_idx][col_idx]:
            prev[row_idx] = grid[row_idx][col_idx]
            visible[row_idx][col_idx] = True

count = 0
for row in visible:
    for item in row:
        if item == True:
            count+=1

print(count)

def below(row_idx, col_idx):
    center = grid[row_idx][col_idx]
    below = 0
    for row_below in range(row_idx + 1, row_num):
        if center > grid[row_below][col_idx]:
            below += 1
        else:
            below += 1
            break
    return below

def above(row_idx, col_idx):
    center = grid[row_idx][col_idx]
    above = 0
    for row_above in range(row_idx - 1, -1, -1):
        if center > grid[row_above][col_idx]:
            above += 1
        else:
            above += 1
            break
    return above

def right(row_idx, col_idx):
    center = grid[row_idx][col_idx]
    right = 0
    for col_right in range(col_idx + 1, col_num):
        if center > grid[row_idx][col_right]:
            right += 1
        else:
            right += 1
            break
    return right

def left(row_idx, col_idx):
    center = grid[row_idx][col_idx]
    left = 0
    for col_left in range(col_idx -1, -1, -1):
        if center > grid[row_idx][col_left]:
            left += 1
        else:
            left += 1
            break
    return left

max = 0
for row_idx in range(1, row_num):
    for col_idx in range(1, col_num):
        s = 1
        s *= below(row_idx, col_idx)
        s *= above(row_idx, col_idx)
        s *= right(row_idx, col_idx)
        s *= left(row_idx, col_idx)
        if s > max:
            max = s

print(max)