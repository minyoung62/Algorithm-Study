n, m = tuple(map(int, input().split()))
ll = [0] * n
for i in range(n):
    ll[i] = int(input())



r = max(ll) * m

def bisect_left(l, r):
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        target = 0
        for i in ll:
            target += mid // i
        # print(target, mid)
        if m <= target:
            
            r = mid - 1
        else :
            ans = mid
            l = mid + 1
    return ans

print(bisect_left(1, r)+1)
