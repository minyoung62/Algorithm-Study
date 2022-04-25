
from sys import stdin

n = int(stdin.readline().strip())

import heapq

arr = [
    int(stdin.readline().strip())
    for _ in range(n)
]

s = []
h = []
m = None
for i in range(len(arr)):

    if i == 0:
        heapq.heappush(s,-arr[i])
        m = -s[0]
        print(-s[0])
        continue
    
    if len(s) == len(h):
        if m < arr[i]:
            heapq.heappush(h, arr[i])
            heapq.heappush(s, -heapq.heappop(h))
        else:
            heapq.heappush(s, -arr[i])
    elif len(s) > len(h):
        heapq.heappush(s, -arr[i])
        heapq.heappush(h, -heapq.heappop(s))

    
    m = -s[0]
    print(m)