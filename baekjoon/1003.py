n = int(input())

testCase = [0] * n
for i in range(n):
    testCase[i] = int(input())

def fibo(n):
    if n == 0 :
        t[0] += 1
        return 0
    elif n == 1:
        t[1] += 1
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

for test in testCase:
    t = [0, 0]
    fibo(test)
    print(t[0], t[1])
