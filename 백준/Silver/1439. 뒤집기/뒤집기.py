a = input()
s = set(a)
if s == 0:
    print(0)
else:
    n = 1
    for i in range(1, len(a)):
        if a[i-1] == a[i]:
            continue
        else:
            n += 1
    print(n//2)
