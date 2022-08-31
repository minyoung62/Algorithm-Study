n = int(input())

newArr = []
def is_prime_num(n):
  arr = [True] * (n + 1)  # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
  arr[0] = False
  arr[1] = False

  for i in range(2, n + 1):
    if arr[i] == True:  # 특정 수가 지워지지 않았다면 (소수여서)
      j = 2
      newArr.append(i)

      while (i * j) <= n:
        arr[i * j] = False  # i의 배수의 값을 False로 지워준다.
        j += 1

  return arr

maxNum = 4000000
arr = is_prime_num(maxNum)  # 0 ~ 50중 소수를 구하기 위한 함수
ans = 0
cnt = 0
R = -1
for L in range(len(newArr)):
  while R + 1 < len(newArr) and cnt < n:
    R += 1
    cnt += newArr[R]
  
  if cnt == n:

    ans += 1

  cnt -= newArr[L]


print(ans)
