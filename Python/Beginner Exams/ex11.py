from urllib.request import Request, urlopen
import math

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
code = []
turn = str(data)
turn = turn[11:]
place = turn.find(",")
turn = turn[:place]
cloud = 'https://drand.cloudflare.com/public/{}'
for i in range(20):
    a = str(int(turn) - i)
    req = Request(cloud.format(a), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    tmp = str(data)
    x = tmp.find("randomness")
    y = tmp.find('"',x+13)
    tmp = tmp[x+13:y]
    code.append(tmp)
#Next i try to interpret "Μετατρέψτε αυτές τις τιμές σε ένα δεκαεξαδικό κείμενο"
print("Hexadecimal numbers:\n",code)
for i in range(20):
    code[i] = "0x" + code[i]
print("\nHexadecimal-er numbers:\n", code)
intcode = []
for i in range(20):
    intcode.append(int(code[i], 16))
print("\nHexadecimal number's value in the decimal system:\n", intcode)
hextext = ""
for i in range(20):
    hextext += code[i] + " "
print("\nHexadecimal numbers in ONE text:\n", hextext)
hextext = 0
for i in range(20):
    hextext += intcode[i]
print("\nHexadecimal number's sum total in ONE text, in the decimal system:\n", hextext)
hextext = hex(hextext)
print("\nHexadecimal number's sum total in ONE text, in the hexidecimal system:\n", hextext)
#Next i calculate the entropy in which i COULD NOT figure out how to involve the requested 20 numbers
length = len(tmp)
p = 1/(16)
S = 0
for i in range(64):
    S += p 
entropy = -S*math.log2(p)
print("\n\nThe entropy is:", entropy)
#Additionally i was not aware of 'entropy' before this exercise and do not understand it today