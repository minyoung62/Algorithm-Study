n = int(input())

testCase = [0] * n
for i in range(n):
    testCase[i] = int(input())


def fibo(n):
    for i in range(2, n + 1):

        t[i][0] = t[i-1][0] + t[i-2][0]
        t[i][1] = t[i-1][1] + t[i-2][1]
    

for test in testCase:
    t = [[0, 0] for _ in range(test + 1)]
    t[0][0] = 1
    if test > 0:
        t[1][1] = 1

    fibo(test)
    print(t[-1][0], t[-1][1])

