n = int(input())

import heapq

q = []

l = []

for i in range(n):
    l.append(int(input()))

for num in l:
    if num == 0:
        if len(q) == 0:
            print("0")
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)
    