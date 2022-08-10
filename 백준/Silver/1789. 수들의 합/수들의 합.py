n = int(input())
tmp = n
ans = 1
for i in range(1, n+1):
    tmp -= i

    if tmp < 0:
        ans = i-1
        break
print(ans)