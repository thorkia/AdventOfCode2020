

with open('input.txt') as f:
    lines = f.readlines()

numbers =[int(e.strip()) for e in lines]
numbers.sort()

#Part 1: Find the numbers that add up 2020
for num in numbers:
    diff = 2020-num
    i = len(numbers)-1;
    
    while i >= 0 and numbers[i]>diff:
        i-=1

    if numbers[i] == diff:
        print(num*diff)
        break

#Part 2: Horrible way to find 3 numbers that add up to 2020 and the product
found = False
for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1+num2+num3 == 2020:
                print(num1*num2*num3)
                found = True
                break
        if found:
            break
    if found:
        break


x = input("Done")