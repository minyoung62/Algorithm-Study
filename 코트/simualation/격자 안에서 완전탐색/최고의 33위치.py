n = int(input())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))


def sumMoney(x, y):
    totalMoney = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if a[i][j] == 1:
                totalMoney += 1
    return totalMoney
ans = 0
for i in range(n-2):
    for j in range(n-2):
        ans = max(sumMoney(i, j), ans)
print(ans)