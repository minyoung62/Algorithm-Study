a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    tmp = a/(c-b)
    print(int(tmp + 1))