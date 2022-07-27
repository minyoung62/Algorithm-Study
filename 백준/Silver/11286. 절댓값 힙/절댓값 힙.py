import heapq
import sys
n = int(input())
h = []
for i in range(n):
    q = int(sys.stdin.readline())
    if q == 0:
        if len(h) == 0:
            print('0')
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(q),q))