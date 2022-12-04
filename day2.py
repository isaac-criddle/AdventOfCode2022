if __name__ == '__main__':
    matches = []

    def mapToABC(m) -> str:
        if m == 'X':
            return 'A'
        if m == 'Y':
            return 'B'
        if m == 'Z':
            return 'C'

    with open('input.txt') as f:
        for line in f:
            o, m = line.strip().split()
            matches.append((o, m))

    f.close()

    print(matches)

    def winningPoints(o, m) -> int:
        if o == m:
            return 3
        else:
            if o == 'A' and m == 'B':
                return 6
            if o == 'A' and m == 'C':
                return 0
            if o == 'B' and m == 'A':
                return 0
            if o == 'B' and m == 'C':
                return 6
            if o == 'C' and m == 'A':
                return 6
            if o == 'C' and m == 'B':
                return 0

    def typePoints(m) -> int:
        if m == 'A': return 1
        if m == 'B': return 2
        if m == 'C': return 3

    def calcShape(o, x):
        match o, x:
            case 'A', 'X':
                return 'C'
            case 'A', 'Y':
                return 'A'
            case 'A', 'Z':
                return 'B'
            case 'B', 'X':
                return 'A'
            case 'B', 'Y':
                return 'B'
            case 'B', 'Z':
                return 'C'
            case 'C', 'X':
                return 'B'
            case 'C', 'Y':
                return 'C'
            case 'C', 'Z':
                return 'A'
            case _:
                return 'B'

    total_score = 0
    for match in matches:
        o = match[0]
        m = calcShape(o, match[1])
        match_points = 0
        print(o, match[1], m, winningPoints(o, m), typePoints(m))
        total_score += winningPoints(o, m) + typePoints(m)

    print(total_score)
