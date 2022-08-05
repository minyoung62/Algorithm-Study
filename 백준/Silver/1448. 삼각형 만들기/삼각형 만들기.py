n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
ans = -1
a.sort(reverse=True)

for i in range(len(a)-2):
    if a[i] < a[i + 1] + a[i + 2]:
        ans = a[i] + a[i + 1] + a[i + 2]
        break
print(ans)
