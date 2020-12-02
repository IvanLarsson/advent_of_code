inputfile = open('input', 'r') 
lines = inputfile.readlines()

for line in lines: 
    line = line.strip()

    for line2 in lines:
        line2 = line2.strip()

        for line3 in lines:
            line3 = line3.strip()

            if int(line) + int(line2) + int(line3) == 2020:
                print("Line ", line, "line2 ", line2, "line3 ", line3, "value ",int(line) * int(line2) * int(line3) )
