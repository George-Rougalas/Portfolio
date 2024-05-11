file = open("characters.txt", "r")
text = file.read()
file.close()
#turn characters into binary
char = list(text)
repeats = len(char)
binchar = []
for i in range(repeats):
    tmp = ""
    binfull = bin(ord(char[i]))
    binfull=binfull[2:]
    length=len(binfull)
    for j in range(7-length):
        tmp += "0"
    tmp += binfull
    binchar.append(tmp)
print(char, "\n\nThe binary value for each character is:\n", binchar)
#finding zero streaks
mark = []
max = maxtmp = 0
for i in range(repeats):
    obj = list(binchar[i])
    obj.append("stop")
    for j in range(8):
        if obj[j] == "0":
            maxtmp += 1
        elif maxtmp < max:
            maxtmp = 0
        elif maxtmp == max:
            mark.append(i)
            maxtmp = 0
        elif maxtmp > max:
            mark = [i]
            max = maxtmp
            maxtmp = 0
print("\nThe biggest streak of zeros is",max, "found in:")
for j in range(len(mark)):
    a = mark[j]
    print(" ", binchar[a],"->", char[a] )
#finding one streaks
mark = []
max = maxtmp = 0
for i in range(repeats):
    obj = list(binchar[i])
    obj.append("stop")
    for j in range(8):
        if obj[j] == "1":
            maxtmp += 1
        elif maxtmp < max:
            maxtmp = 0
        elif maxtmp == max:
            mark.append(i)
            maxtmp = 0
        elif maxtmp > max:
            mark = [i]
            max = maxtmp
            maxtmp = 0
print("\nThe biggest streak of ones is",max, "found in:")
for j in range(len(mark)):
    a = mark[j]
    print(" ", binchar[a],"->", char[a] )