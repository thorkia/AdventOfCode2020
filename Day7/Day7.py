
class Bag:
    def __init__(self, color, *args, **kwargs):
        self.color = color
        self.holds = dict() #dict of bag:number
        self.isIn = list(); #list of bag
        return super().__init__(*args, **kwargs)
    
    def getisin(self):
        items = set()
        for item in self.isIn:            
            items.add(item.color)
            for sub in item.getisin():
                items.add(sub)
        return items

    def getholdcount(self):
        count = 0
        for b in self.holds:
            count+=self.holds[b]
            count+= (self.holds[b] * b.getholdcount())
        return count



def addBag(newbagcolor):
    newbagcolor = str(newbagcolor)
    if newbagcolor in baglist:
        return
    else:
        bag = Bag(newbagcolor)
        baglist[newbagcolor] = bag


with open('input.txt') as f:
    lines = f.readlines()

#Part 1: Determine which bags can hold a gold bag
baglist = dict()

for line in lines:
    line = line.strip()
    containsloc = line.find("contain")
    bagcolor = line[:containsloc - 6]
    print(bagcolor)
    addBag(bagcolor)

    # now check the contains
    holdinglines = line[containsloc + len('contain '):].split(',')
    for holdingline in holdinglines:        
        holdingline = holdingline.strip().strip('.')
        
        if holdingline.startswith('no'):
            continue

        if holdingline[-1] == 's':
            holdingline = holdingline[:-1]
        numberloc = holdingline.find(' ');
        subbagcolor = holdingline[numberloc+1:-4]
        subbagamount = int(holdingline[:numberloc])
        addBag(subbagcolor)

        baglist[subbagcolor].isIn.append(baglist[bagcolor])
        baglist[bagcolor].holds[baglist[subbagcolor]] = subbagamount        
    
#With fully generated baglist, now we can check which bags can hold a shiny gold bag
mybag = baglist['shiny gold']
holdmybag = mybag.getisin()
holdcount = mybag.getholdcount();

print(len(holdmybag))
print(holdcount)



