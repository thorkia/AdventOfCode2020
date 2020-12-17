from typing import List, Tuple

def run_part1(nums: List[int], rounds:int):

    #initialize the list of spoken numbers
    spoken = dict()
    for num in nums:
        spoken[num] = 0

    #keep track of the last round a number was spoken
    lastspokenround = dict()
    for num in range(0,len(nums),1):
        lastspokenround[nums[num]] = [num+1]


    round  = len(nums) + 1
    
    while round <= rounds:
        lastnumber = nums[-1]
        #If the number has only been spoken once, then say 0
        if lastnumber in spoken and spoken[lastnumber] == 0:                                   
            nums.append(0)
            if 0 in lastspokenround:
                lastspokenround[0].append(round)
                spoken[0] = 1
            else:
                lastspokenround[0] = [round]
                spoken[0] = 0
        else:
            #get the diff and set it to that of the last 2 occurances
            lastitems = lastspokenround[lastnumber][-2:]
            newnumber = abs(lastitems[0]-lastitems[1])
            nums.append(newnumber)

            if newnumber in lastspokenround: #this number has been spoken before
                spoken[newnumber] = 1
                lastspokenround[newnumber].append(round)
            else: #first time this number has been spoken
                spoken[newnumber] = 0
                lastspokenround[newnumber] = [round]
        round+=1

    print(nums[-1])
    return 0


print("Part1 Test")
run_part1([0,3,6], 10)
run_part1([0,3,6], 2020)
run_part1([1,3,2], 2020)
run_part1([2,1,3], 2020)
run_part1([1,2,3], 2020)
run_part1([2,3,1], 2020)
run_part1([3,2,1], 2020)
run_part1([3,1,2], 2020)

#Puzzle Input
print("Part1 Answer")
run_part1([11,18,0,20,1,7,16], 2020)


#part2 is part 1 but with 30,000,000
print("Part2 Test")
run_part1([0,3,6], 30000000)
run_part1([1,3,2], 30000000)
run_part1([2,1,3], 30000000)
run_part1([1,2,3], 30000000)
run_part1([2,3,1], 30000000)
run_part1([3,2,1], 30000000)
run_part1([3,1,2], 30000000)

print("Part2 Answer")
run_part1([11,18,0,20,1,7,16], 30000000)