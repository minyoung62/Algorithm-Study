n = int(input())
copyN = n
ans = 1e9
if n % 5 == 0:
    ans = n // 5
    n = 0

elif n // 5 != 0:
    c = n // 5

    flag = False
    for i in range(c, 0, -1):
        fiveNum = 5 * i
        if (n-fiveNum) % 3 == 0:
            flag = True
            ans = min(ans,i + (n-fiveNum) // 3)
    if flag:
        n = 0
if n!= 0 and  n % 3 == 0:
    ans = n // 3
    n = 0

if n != 0:
    ans = -1

print(ans)