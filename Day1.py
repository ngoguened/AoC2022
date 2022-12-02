def Aoc1():
    Lines = open("day1Input.txt", 'r').readlines()
    T = []
    val = 0
    for line in Lines:
        if line == '\n':
            T.append(val)
            val = 0
        else:
            val = val + int(line[:-1])
    T.sort()
print(Aoc1)
