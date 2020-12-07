
with open('input.txt') as f:
    lines = f.readlines()

#Part 1: 3 right, 1 down until the end
lineWidth = len(lines[0].strip())
hillLength = len(lines)

loc = 0
treesHit = 0


for x in range(1,hillLength,1):
    loc += 3
    loc = loc % lineWidth
    if x<hillLength and lines[x][loc] == "#":
        treesHit += 1

print(treesHit)

#Part 2: do the defined steps to find the trees.  Tuple is (right, down)
steps = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
combined = 1

for r,d in steps:
    #reset the variables for every count set
    treesHit = 0
    loc = 0

    for x in range(d,hillLength,d):
        loc += r
        loc = loc % lineWidth
        if x<hillLength and lines[x][loc] == "#":
            treesHit += 1
    combined *= treesHit
    print(treesHit)    

print(combined)