
n = int(input())

testList = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    testList.append((x1, y1, r1, x2, y2, r2))

for test in testList:
    x1, y1, r1, x2, y2, r2 = test

    cicles_dis = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2),1/2)

    sumR = r1 + r2

    if cicles_dis == 0 and r1 == r2:
        print(-1)
    elif cicles_dis == sumR or (cicles_dis + min(r1, r2) == max(r1, r2)):
        print(1)
    elif cicles_dis > sumR or cicles_dis + min(r1, r2) < max(r1, r2):
        print(0)
    else:
        print(2)
    