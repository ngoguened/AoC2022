def Aoc2_1():
    Lines = open("aoc2Input.txt", 'r').readlines()
    score = 0

    for line in Lines:
        opp, me = ord(line[0])-65, ord(line[2])-88 #Rock:0, Paper:1, Scissors:2.
        score += (me+1)
        if me == opp:
            score += 3
        elif (me+2)%3 == opp:
            score += 6
    return score

def Aoc2_2():
    Lines = open("aoc2Input.txt", 'r').readlines()
    score = 0
    
    for line in Lines:
        opp = ord(line[0])-65 #See above
        outcome = line[2]
        if outcome == "X":
            score += (opp+2)%3+1
        elif outcome == "Z":
            score += (opp+1)%3 + 7
        else:
            score += opp + 4
    return score
        
print(Aoc2_1())
print(Aoc2_2())
