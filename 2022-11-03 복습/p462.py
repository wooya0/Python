infile = open("input.txt", "r", encoding="utf-8")
line = infile.readline().rstrip()
while line != "" :
    print(line)
    line = infile.readline()