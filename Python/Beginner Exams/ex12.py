from urllib.request import Request, urlopen
import math

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
code = []
turn = str(data)
turn = turn[11:]
place = turn.find(",")
turn = int(turn[:place])
cloud = 'https://drand.cloudflare.com/public/{}'
for i in range(100):
    a = str(turn - i)
    req = Request(cloud.format(a), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    tmp = str(data)
    x = tmp.find("randomness")
    y = tmp.find('"',x+13)
    tmp = tmp[x+13:y]
    code.append(tmp)
#create binary list
for i in range(100):
    code[i] = bin(int(code[i], 16))
    code[i] = code[i][2:]
#Zero streaks
mark = []
max = maxtmp = 0
for i in range(100):
    obj = list(code[i])
    obj.append("stop")
    for j in range(len(obj)):
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
print("\nThe biggest streak of zeros is",max, ", located in round(s):")
for j in range(len(mark)):
    a = mark[j]
    print(turn - a)
#One streaks
mark = []
max = maxtmp = 0
for i in range(100):
    obj = list(code[i])
    obj.append("stop")
    for j in range(len(obj)):
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
print("\nThe biggest streak of ones is",max, ", located in round(s):")
for j in range(len(mark)):
    a = mark[j]
    print(turn - a)