n, m = map(int, input().split())

dkey = dict()
dval = dict()
for i in range(1,n + 1):
    val = input()
    dkey[str(i)] = val
    dval[val] = i

for i in range(m):
    q = input()
    if q.isdigit():
        print(dkey[q])
    else:
        print(dval[q])