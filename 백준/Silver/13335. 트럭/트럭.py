
n, l, w = tuple(map(int, input().split()))
a = list(map(int, input().split()))
dist = [-1] * n
t = 0
cnt = 0
def canGo():
  truckTotalWieght = 0

  for i in range(n):
    if dist[i] != -1:
      truckTotalWieght += a[i]

  return truckTotalWieght + a[cnt] <= w
truck_cnt = 0

def isDone():
  for i in range(n):
    if dist[i] != -1:
      return False
  return True

while cnt != n or not isDone():
  # 현재 있는 트럭들 다 한칸씩 앞으로 보내고
  # 끝나면 제거하고 답 +1
  for i in range(len(dist)):
    if dist[i] != -1:
      if dist[i] + 1 > l:
        dist[i] = -1

      else:
        dist[i] += 1

  # 다리 무게 하중을 버틸 수 있으면?
  if cnt != n and canGo():
    # 새로운 트럭 추가
    dist[cnt] = 1
    cnt += 1

  t += 1
print(t)
