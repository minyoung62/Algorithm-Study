n = int(input())

meets = [
    []
    for _ in range(n)
]
for i in range(n):
    start, end = tuple(map(int, input().split()))
    meets[i] = (start, end)

meets = sorted(meets, key = lambda x : (x[1], -(x[1] - x[0])))

answer = 0
cur = 0
for start, end in meets:
    if start >= cur:
        cur = end
        answer += 1
print(answer)