n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))


def isHappySeq(arr):
    seqCount = 1

    if m == 1:
        return True

    for i in range(1, n):
        if arr[i] == arr[i-1]:
            seqCount += 1
            if seqCount == m:
                return True
        else:
            seqCount = 1

    return False


ans = 0
# 가로
for i in range(n):
    if isHappySeq(a[i]):
        ans += 1

# 세로
tmp = [0] * n
for i in range(n):

    for j in range(n):
        tmp[j] = a[j][i]

    if isHappySeq(tmp):
        ans += 1

print(ans)