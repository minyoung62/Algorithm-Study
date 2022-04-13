n = int(input())

meet = [0] * n

for i in range(n):
    s, e = map(int, input().split())
    meet[i] = (s, e)

sortedMeet = sorted(meet, key = lambda x : (x[1], -(x[1]-x[0])))
tmp = 0 
answer = 0
for s, e in sortedMeet:
    if s >= tmp :
        tmp = e
        answer += 1
print(answer)


#https://source-sc.tistory.com/59