
n = int(input())

tmp = [0] * n
for i in range(n):
    tmp[i] = int(input())



d = [0] * (max(tmp) + 1)

d[1], d[2], d[3] = 1, 2, 4

for i in range(4, max(tmp) + 1):
    d[i] = ( d[i - 1] + d[i -2] + d[i - 3] ) % 1000000009

for i in tmp:
    print(d[i] % 1000000009)