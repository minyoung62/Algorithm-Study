n = int(input())
l = [
    list(map(str, input().split()))
    for _ in range(n)
]

l = [ 
    [x[0], int(x[1]), int(x[2]), int(x[3])] for x in l
]

l.sort(key = lambda x: (-x[1], x[2],-x[3], x[0]))
for i in l:
    print(i[0])