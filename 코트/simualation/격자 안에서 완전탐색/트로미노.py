n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

blocks = [
    [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ],
    [
        [1, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ],
    [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ],
    [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    ],
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
    ],
    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ],
]


def sumMoney(x, y, block):
    totalMoney = 0
    tmp = []
    c = 0
    for i in range(x, x + 3):
        tmp.append([])
        for j in range(y, y + 3):
            if i < n and j < m:
                tmp[c].append(a[i][j])
            else:
                tmp[c].append(0)
        c += 1
    for i in range(3):
        for j in range(3):
            if block[i][j] == 1:
                totalMoney += tmp[i][j]

    return totalMoney

ans = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            ans = max(sumMoney(i, j, block), ans)

print(ans)