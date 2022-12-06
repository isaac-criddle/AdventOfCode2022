input = []

with open('input.txt') as f:
    for line in f:
        input.append(line.strip())

f.close()

split_input = []

for line in input:
    first_half = line[0:int(len(line)/2)]
    second_half = line[int(len(line)/2):]
    split_input.append((first_half, second_half))

def char_set(string) -> {}:
    s = set()
    for char in string:
        s.add(char)
    return s

intersection = []
for one, two in split_input:
    intersection.append(
        (char_set(one)).intersection(char_set(two)).pop()
    )

def intVal(character) -> int:
    if(str.islower(character)):
        return ord(character) - 96
    else:
        return ord(character) - 65 + 27

values = []
for character in intersection:
    values.append(intVal(character))

sum(values)

triples = []
for i in range(0, 100):
    set1 = char_set(input[3*i])
    set2 = char_set(input[3*i + 1])
    set3 = char_set(input[3*i + 2])
    triples.append((set1, set2, set3))

val = 0
for triple in triples:
    val += intVal(set.intersection(*triple).pop())

print(val)