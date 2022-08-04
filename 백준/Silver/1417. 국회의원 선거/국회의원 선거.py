n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

dasom = a.pop(0)

a.sort(key= lambda  x:-x)

def isWin():
    for i in range(len(a)):
        if dasom <= a[i]:
            return False
    return True
i = 0
ans = 0
while not isWin():
    a[a.index(max(a))] -= 1
    dasom += 1
    ans += 1



print(ans)