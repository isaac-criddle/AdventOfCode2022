grid = []
with open('inputs/input12.txt') as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(ord(char))
        grid.append(row)

S = []
E = []
for row_idx in range(len(grid)):
    for col_idx in range(len(grid[0])):
        if grid[row_idx][col_idx] == 83:
            S = [row_idx, col_idx]
        elif grid[row_idx][col_idx] == 69:
            E = [row_idx, col_idx]

grid[S[0]][S[1]] = ord('a')
grid[E[0]][E[1]] = ord('z')

for row in grid:
    print(row)
print()

As = []
for row_idx in range(len(grid)):
    for col_idx in range(len(row)):
        if grid[row_idx][col_idx] == ord('a'):
            As.append([row_idx, col_idx])
            print([row_idx, col_idx])

dist_from_e = []
for row in grid:
    dist_row = []
    for level in row:
        dist_row.append(-1)
    dist_from_e.append(dist_row)

dist_from_e[E[0]][E[1]] = 0

changed = True

def calc_neighbor_val(home, neighbor):
    global changed
    if neighbor == -1:
        changed = True
        return home + 1
    else:
        if home + 1 < neighbor:
            changed = True
            return home + 1
        else:
            return neighbor

def are_negatives():
    for row_idx in range(len(dist_from_e)):
        for col_idx in range(len(dist_from_e[0])):
            if dist_from_e[row_idx][col_idx] == -1 and grid[row_idx][col_idx] == ord('a'):
                return True
    return False

for i in range(4000):
    changed
    for row_idx in range(len(dist_from_e)):
        for col_idx in range(len(row)):
            val = dist_from_e[row_idx][col_idx]
            if val != -1:
                if col_idx + 1 < len(dist_from_e[0]):
                    if grid[row_idx][col_idx] - grid[row_idx][col_idx + 1] <= 1:
                        dist_from_e[row_idx][col_idx + 1] = calc_neighbor_val(val, dist_from_e[row_idx][col_idx + 1])
                if col_idx - 1 >= 0:
                    if grid[row_idx][col_idx] - grid[row_idx][col_idx - 1] <= 1:
                        dist_from_e[row_idx][col_idx - 1] = calc_neighbor_val(val, dist_from_e[row_idx][col_idx - 1])
                if row_idx + 1 < len(dist_from_e):
                    if grid[row_idx][col_idx] - grid[row_idx + 1][col_idx] <= 1:
                        dist_from_e[row_idx + 1][col_idx] = calc_neighbor_val(val, dist_from_e[row_idx + 1][col_idx])
                if row_idx - 1 >= 0:
                    if grid[row_idx][col_idx] - grid[row_idx - 1][col_idx] <= 1:
                        dist_from_e[row_idx - 1][col_idx] = calc_neighbor_val(val, dist_from_e[row_idx - 1][col_idx])

    for row in dist_from_e:
        print(row)
    print()

print(dist_from_e[S[0]][S[1]])

min = -1
for A in As:
    if min == -1:
        min = dist_from_e[A[0]][A[1]]
    if dist_from_e[A[0]][A[1]] < min and dist_from_e[A[0]][A[1]] != -1:
        min = dist_from_e[A[0]][A[1]]

print()
print(min)
