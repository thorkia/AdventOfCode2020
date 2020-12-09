def checknumber(number, items):
    number = int(number)
    loc = 0
    for item in items:
        for subitem in items[loc:]:
            if item+subitem == number:
                return True    

    return False


with open('input.txt') as f:
    lines = f.readlines()

numbers = [int(l) for l in lines]
#For the test file, set the peramble to 5
preamble = 25
loc = 0

badnumber = -1

for number in numbers:
    if (loc >= preamble):
        isgood = checknumber(number, numbers[loc-preamble:loc])
        if isgood == False:
            print(number)
            badnumber = number
            break
    loc+=1

#Part 2 find the contiguous block that sums to the amount
loc = -1
end = -1
found = False

while loc < len(numbers) and found == False:
    loc +=1
    end = loc+1
    while end < len(numbers):
        total = sum(numbers[loc:end])
        if total == badnumber:
            found = True
            break
        else:
            end +=1
        
print(numbers[loc:end])
sum = min(numbers[loc:end]) + max(numbers[loc:end])
print(sum)
