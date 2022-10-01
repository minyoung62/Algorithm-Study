# N = 10
# a = [0] * N
#
#
# def key2hash_value(key):
#   return hash(key)
#
#
# def save(key, value):
#   hash_value = key2hash_value(key)
#   idx = hash_value % 10
#   a[idx] = value
#
#
# def get_value(key):
#   hash_value = key2hash_value(key)
#   idx = hash_value % 10
#   return a[idx]
# key = "10"
# value = 10
# save(key, 10)
# print(a)
# print(get_value(key))


# s = ['a', 'e', 'i', 'o', 'u']
# s = set(s)
#
# l, c = map(int,input().split())
# a = list(input().split())
#
# selected = []
#
# choose
#
# choose(cnt)

#
# n = int(input())
# a = [
#   list(map(int, input().split()))
#   for _ in range(n)
# ]
# selected = [0] * n
# used = [0] * n
# import sys
# ans = sys.maxsize
# def choose(cnt, cntsum):
#   global ans
#   if cnt == n:
#     start = 0
#     link = 0
#
#     for i in range(n):
#       for j in range(i+1, n):
#         if selected[i] and selected[j]:
#           start += a[i][j] + a[j][i]
#         elif not  selected[i] and not selected[j]:
#           link += a[i][j] + a[j][i]
#     ans = min(ans, abs(start-link))
#     return
#
#   selected[cnt] = 1
#   choose(cnt+1,cntsum + 1)
#   selected[cnt] = 0
#
#   choose(cnt+1,cntsum)
#
#
# choose(0, 0)
# print(ans)
#
#
# def solution(arr):
#   R = - 1
#   s = set()
#   n = len(arr)
#   for i in range(n):
#     tmp = str(arr[i])
#     tmpLen = len(tmp)
#
#     val = sum(map(int, list(tmp)))
#     if (val, tmpLen) not in s:
#       s.add((val, tmpLen))
#
#   answer = len(s)
#
#   return answer
#
#
# def solution(compressed):
#   answer = ''
#
#   s = []
#   num = ""
#   alpha = ""
#   z = ""
#   for i in range(len(compressed)):
#     if compressed[i].isdigit():
#       num += compressed[i]
#       if len(s) == 0 and alpha != "":
#         answer += alpha
#         alpha = ""
#       elif len(s) != 0 and alpha != "":
#         z = alpha
#         alpha = ""
#     elif compressed[i] == '(':
#       s.append(int(str(num)))
#       num = ""
#     elif compressed[i] == ')':
#       if len(s) > 1:
#         multi = s.pop()
#         z += alpha * multi
#         alpha = ""
#       elif len(s) == 1:
#
#         if z != "":
#           z += alpha
#           multi = s.pop()
#           answer += z * multi
#           alpha = ""
#           z = ""
#         else:
#           multi = s.pop()
#
#           answer += alpha * multi
#           alpha = ""
#
#     elif compressed[i].isalpha:
#       alpha += compressed[i]
#
#   answer += alpha
#
#   return answer
selected = []

n = 0

a = []
def choose(cnt):
  if cnt == n:
    if len(selected) == 6:
      print(*selected)
    return

  selected.append(a[cnt])
  choose(cnt + 1)
  selected.pop()

  choose(cnt + 1)

while True:

  k = list(map(int, input().split()))
  if k[0] == 0:
    break

  a = k[1:]
  n = len(a)
  choose(0)
  print()

