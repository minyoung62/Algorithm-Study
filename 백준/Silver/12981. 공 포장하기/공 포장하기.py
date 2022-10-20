
r, g, b = tuple(map(int, input().split()))
ans = 0
# 모두 다른 경우 제일 작은 것으로 빼주기
a = [r,g,b]
m = min(a)
ans += m

for i in range(len(a)):
  a[i] -= m

# 같은 공이 3개 남아 있는 경우
for i in range(3):
  if a[i] // 3 != 0:
    ans += a[i] // 3
    a[i] %= 3


# 같은 공이 2개가 남은 경우
for i in range(3):
  if a[i] == 2:
    ans += 1
    a[i] = 0

# 나머지  처리
if sum(a) > 0:
  ans += 1
  
print(ans)