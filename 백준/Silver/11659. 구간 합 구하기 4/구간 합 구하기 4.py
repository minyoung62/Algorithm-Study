n, m = map(int, input().split())
a = list(map(int, input().split()))
aa = []
aa.append(a[0])
for i in range(1, len(a)):
    aa.append(a[i] + aa[i-1])
aa = [0] + aa
ss = []
for i in range(m):
    ss.append((map(int, input().split())))
for s, e in ss:
    print(aa[e] - aa[s-1])