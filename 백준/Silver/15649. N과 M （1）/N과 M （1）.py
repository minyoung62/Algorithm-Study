n, m = map(int, input().split())

from itertools import permutations
l = []
for i in range(1, n + 1):
    l.append(i)


for i in permutations(l, m):
    print(" ".join(map(str, i)))