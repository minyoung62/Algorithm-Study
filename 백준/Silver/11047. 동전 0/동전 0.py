n, m = map(int, input().split())

a = [0] * n
for i in range(n):
    a[i] = int(input())

ans = 0
for i in range(n-1, -1, -1):
    if m // a[i] !=0 :
        ans += m//a[i]
        m -= m//a[i] * a[i]


print(ans)