a, b = map(int, input().split())
n = int(input())
l = []
m = abs(b-a)
for i in range(n):
    m = min(abs(b-int(input())), m)
ans = 0

if m == abs(b-a):
    ans = abs(b-a)
else:
    ans = 1
    ans += abs(m)
print(ans)