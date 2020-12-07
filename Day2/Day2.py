

with open('input.txt') as f:
    lines = f.readlines()


#Part 1: Count all the passwords that match
#Part 2: The number is index to check, not count
part1 = 0
part2 = 0
for line in lines:
    start=line.find("-")
    end=line.find(" ")
    policyEnd = line.find(":")

    password = line[policyEnd+1:].strip()
    passLow = int(line[:start])
    passHigh = int(line[start+1:end])
    passLetter = line[end:policyEnd].strip()

    letterCount = password.count(passLetter)
    if letterCount >= passLow and letterCount <= passHigh:
        part1+=1

    if (password[passLow-1] == passLetter) != (password[passHigh-1] == passLetter):
        part2+=1;



print(part1)
print(part2)
input("Hello")
