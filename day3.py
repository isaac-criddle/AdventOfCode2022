if __name__ == "__main__":
    m, n, x = list(map(int, input().split()))
    d = []
    for i in range(m):
        d.append(input().split())


    def newVal(fishType, currVal):
        if currVal == '0':
            return fishType
        elif currVal > fishType:
            return fishType
        else:
            return currVal


    again = True
    while (again):
        again = False
        for i in range(n):
            for j in range(m):
                if (d[i][j] not in ('0', '1')):
                    if (i - 1 >= 0):
                        if newVal(d[i][j], d[i - 1][j]) != d[i - 1][j]:
                            d[i - 1][j] = newVal(d[i][j], d[i - 1][j])
                            again = True
                    if (i + 1 <= n - 1):
                        if newVal(d[i][j], d[i + 1][j]) != d[i + 1][j]:
                            d[i + 1][j] = newVal(d[i][j], d[i + 1][j])
                            again = True
                    if (j - 1 >= 0):
                        if newVal(d[i][j], d[i][j - 1]) != d[i][j - 1]:
                            d[i][j - 1] = newVal(d[i][j], d[i][j - 1])
                            again = True
                    if (j + 1 <= m - 1):
                        if newVal(d[i][j], d[i][j + 1]) != d[i][j + 1]:
                            d[i][j + 1] = newVal(d[i][j], d[i][j + 1])
                            again = True
                elif (d[i][j] == 1):
                    continue

    print()
    for row in d:
        print(row)