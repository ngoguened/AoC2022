import math
def Aoc3_1():
    Lines = open("aoc3Input.txt", 'r').readlines()
    score = 0
    for line in Lines:
        half = int(math.floor(len(line))/2)
        sack1 = line[:half]
        sack2 = line[half:]
        
        for i in sack1:
            for j in sack2:
                if i == j:
                    sack2 = [value for value in sack2 if value != i]
                    if i.isupper():
                        score += ord(i)-38
                    else:
                        score += ord(i)-96
                    break
    return score
                

def Aoc3_2():
    Lines = open("aoc3Input.txt", 'r').readlines()
    score = 0
    breakflag = False
    for i in range(0, len(Lines), 3):
        
        elf1 = Lines[i]
        elf2 = Lines[i+1]
        elf3 = Lines[i+2]
        
        for i in elf1:
            for j in elf2:
                for k in elf3:
                    if i == j and j == k:
                        if i.isupper():
                            score += ord(i)-38
                        else:
                            score += ord(i)-96
                        breakflag = True
                        break
                if breakflag:
                    break
            if breakflag:
                breakflag = False
                break
    return score
