
with open('input.txt') as f:
    lines = f.readlines()

answered = set()
answeredCount = 0
answered2 = dict()
answered2Count = 0;
peopleInGroup = 0;

#Part 1: Get a count of all the unique questions answered
#Part 2: Get the questions answered by everyone
for line in lines:
    line = line.strip()
    if line == '':
        answeredCount += len(answered)
        answered.clear()

        answered2Count += sum(a >= peopleInGroup for a in answered2.values())
        peopleInGroup = 0
        answered2.clear()
    else:
        peopleInGroup += 1
        for c in line:
            answered.add(c)            
            if c in answered2:
                answered2[c] = answered2[c] + 1
            else:
                answered2[c] = 1;


#Add last item to the list
answeredCount += len(answered)
answered2Count += sum(a >= peopleInGroup for a in answered2.values())

print(answeredCount)
print(answered2Count)