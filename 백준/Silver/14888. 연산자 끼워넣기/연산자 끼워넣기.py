from itertools import *

n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))


operDict = {
    0:"+",
    1:"-",
    2:"*",
    3:"/"
}

answer = []
opers = []
for i in range(len(o)):
    if o[i] == 0:
        continue
    if i == 0:
        r = operDict[i]
    elif i == 1:
        r = operDict[i]
    elif i == 2:
        r = operDict[i]
    else:
        r = operDict[i]
    for i in range(o[i]):
        opers.append(r)

for oper in set(permutations(opers, n-1)):
  
    oper = list(oper)
    s = 0
    for i in range(len(oper)):
        if i == 0:
            s = str(int(eval(str(a[i]) + oper[i] + str(a[i+1]))))
        else:
            s = str(int(eval( s + oper[i] + str(a[i+1]))))
   
    answer.append(int(s))

print(max(answer))
print(min(answer))
