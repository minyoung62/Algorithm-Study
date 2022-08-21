n = int(input())

a = set()
for i in range(n):
    a.add(input())
a = list(a)
for i in sorted(a, key = lambda x:(len(x),x)):
    print(i)