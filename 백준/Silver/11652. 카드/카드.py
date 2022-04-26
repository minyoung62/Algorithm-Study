n = int(input())

a = [
    int(input())
    for _ in range(n)
]

from collections import Counter

a = list(Counter(a).items())

a = sorted(a, key = lambda x:(-x[1],x[0]))

print(a[0][0])
