from itertools import *

n, m = map(int, input().split())

l = [i for i in range(1, n + 1)]

al = combinations(l, m)

for i in al:
    print(" ".join(map(str, i)))