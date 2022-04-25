n, m = map(int, input().split())

from itertools import *


l = [ i for i in range(1, n + 1)]

for i in product(l, repeat=m):
    print(" ".join(map(str, i)))