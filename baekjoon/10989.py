from sys import stdin

input = stdin.readline().strip

n = int(input())

h = [0] * 10001
for i in range(n):
    c = int(stdin.readline().strip())
    h[c] += 1

for i in range(1,10001):
    if h[i] != 0:
        for j in range(h[i]):
            print(i)
