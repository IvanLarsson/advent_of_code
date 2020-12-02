
total = 0
with open("input", "r") as file:
    for line in file:
        str = line.split()
        min_max = [int(x) for x in str[0].split("-")]
        letter = str[1][:-1]
        password = str[2]
        
        # Part 1
        # letterCount = 0
        # for i in str[2]: 
        #     if i == letter: 
        #         letterCount = letterCount + 1

        # if min_max[0] <= letterCount <= min_max[1]:
        #     total = total + 1

        # part 2
        ok1 = False
        ok2 = False
        index = [i for i, x in enumerate(password) if x == letter]
        if min_max[0]-1 in index:
            ok1 = True
        if min_max[1]-1 in index:
            ok2 = True
        
        if (ok1==False and ok2==True ) or (ok1==True and ok2==False):
             total = total + 1

print(total)