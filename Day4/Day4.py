def check_day1_passport(passport):    
    return all( s in passport for s in mandatory)    

def check_day2_passport(passport):
    kvp = [ (key, get_value_for_key(passport, key)) for key in mandatory ]
    valid_items=[]
    for k,p in kvp:
        func = passport_key_validation.get(k)
        isvalid = func(p)
        valid_items.append(isvalid)

    return all(valid_items)


def byr(value):
    try:
        year =  int(value)
        return year >= 1920 and year <= 2002
    except ValueError:
        return False

    return True

def iyr(value):
    try:
        year =  int(value)
        return year >= 2010 and year <= 2020
    except ValueError:
        return False

    return True

def eyr(value):
    try:
        year = int(value)
        return year >= 2020 and year <= 2030
    except ValueError:
        return False

    return True

def hgt(value):
    try:        
        system = value[-2:];
        size =  int(value[:-2])        
        return (system == 'cm' and size >= 150 and size <= 193) or (system == 'in' and size >= 59 and size <= 76)
    except ValueError:
        return False

    return False

def hcl(value):
    validValues = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    value = str(value)
    cleanedValue = value.translate( { ord(i):None for i in validValues})
    return len(value) == 7 and value[0] == "#" and len(cleanedValue) == 1

def ecl(value):
    validValues = ['amb','blu','brn','gry','grn','hzl','oth']
    value = str(value)    
    return any( eye == value for eye in validValues )

def pid(value):    
    value = str(value)    
    return value.isnumeric() and len(value) == 9


passport_key_validation = {
    'byr:' : byr,
    'iyr:' : iyr,
    'eyr:' : eyr,
    'hgt:' : hgt,
    'hcl:' : hcl,
    'ecl:' : ecl,
    'pid:' : pid,
    }



def get_value_for_key(passport, key):
    passport = str(passport)
    key = str(key)
    keyLoc = passport.find(key)
    endLoc = passport.find(' ', keyLoc)

    if endLoc == -1:
        endLoc = len(passport)

    return passport[keyLoc+4:endLoc].strip()
    


with open('input.txt') as f:
    lines = f.readlines()

#Part 1: Check all mandatory fields are present
mandatory = [ 'byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
optional = ['cid:']

#build a passport object
passports = []
passport = ''
for line in lines:    
    if line.strip() == '':
        passports.append(passport.strip())
        passport = ''

    passport =  ' '.join([passport, line.strip()])

    
#Add the last found passport to the list
passports.append(passport.strip())
#Remove potentially empty items
passports = [p for p in passports if p.strip() != '']

validDay1Passports = [p for p in passports if check_day1_passport(p)]
print(len(validDay1Passports))

#check day 2 rules for passports
validDay2Passports = [p for p in validDay1Passports if check_day2_passport(p)]
print(len(validDay2Passports))
