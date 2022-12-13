test = False
queues = \
    [
        [79, 98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74]

    ] if test else \
        [
            [57],
            [58, 93, 88, 81, 72, 73, 65],
            [65, 95],
            [58, 80, 81, 83],
            [58, 89, 90, 96, 55],
            [66, 73, 87, 58, 62, 67],
            [85, 55, 89],
            [73, 80, 54, 94, 90, 52, 69, 58]
        ]

operations = \
    [
        lambda x: x * 19,
        lambda x: x + 6,
        lambda x: x * x,
        lambda x: x + 3
    ] if test else \
        [
            lambda x: x * 13,
            lambda x: x + 2,
            lambda x: x + 6,
            lambda x: x * x,
            lambda x: x + 3,
            lambda x: x * 7,
            lambda x: x + 4,
            lambda x: x + 7
        ]

tests = \
    [
        lambda x: 2 if x % 23 == 0 else 3,
        lambda x: 2 if x % 19 == 0 else 0,
        lambda x: 1 if x % 13 == 0 else 3,
        lambda x: 0 if x % 17 == 0 else 1
    ] if test else \
        [
            lambda x: 3 if x % 11 == 0 else 2,
            lambda x: 6 if x % 7 == 0 else 7,
            lambda x: 3 if x % 13 == 0 else 5,
            lambda x: 4 if x % 5 == 0 else 5,
            lambda x: 1 if x % 3 == 0 else 7,
            lambda x: 4 if x % 17 == 0 else 1,
            lambda x: 2 if x % 2 == 0 else 0,
            lambda x: 6 if x % 19 == 0 else 0
        ]

for i in range(len(queues)):
    queues[i].reverse()

def taketurn(idx):
    while len(queues[idx]) != 0:
        x = queues[idx].pop()
        x = operations[idx](x) % (96577 if test else 9699690)
        counts[idx] += 1
        queues[tests[idx](x)].insert(0, x)

counts = []
for i in range(len(queues)):
    counts.append(0)

for k in range(10000):
    if k % 100 == 0: print(k)
    for i in range(len(queues)):
        taketurn(i)

pass
print(counts)
