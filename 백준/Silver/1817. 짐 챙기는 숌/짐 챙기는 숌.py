n, m = map(int, input().split())
from collections import deque
if n != 0:
    a = deque(list(map(int, input().split())))
ans = 0
if n != 0:
    tmp = 0

    item = 0
    while a:
        item = a.popleft()
        if tmp + item <= m:
            tmp += item
        else:
            a.insert(0, item)
            tmp = 0
            ans += 1
    if tmp != 0:
        ans += 1

print(ans)