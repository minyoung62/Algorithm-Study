
# 3번
import math
def isPar(string, l , r):
  global dif_left, dif_right

  for i in range(math.ceil(len(string) / 2)):

    if string[l] != string[r]:
      dif_left = l
      dif_right = r
      return False
    l -= 1
    r += 1
  return True

def isPalindrome(string):
  n = len(string)
  if n % 2 == 0:
    if isPar(string, n//2 - 1, n//2):
      return True
  else:
    if isPar(string, n // 2 , n // 2):
      return True
  return False


def outPar(string, l, r):

  while l < r:
    if string[l] != string[r]:
      return l, r

    l += 1
    r -= 1

def isSimiPar(string):
  global dif_left, dif_right
  # in
  leftRemoveString = string.copy()
  leftRemoveString.pop(dif_left)
  rightRemoveString = string.copy()
  rightRemoveString.pop(dif_right)

  for removedString in [leftRemoveString, rightRemoveString]:

    if isPalindrome(removedString):
      return True

  # out
  dif_left, dif_right = outPar(string, 0, len(string)-1)

  leftRemoveString = string.copy()
  leftRemoveString.pop(dif_left)
  rightRemoveString = string.copy()
  rightRemoveString.pop(dif_right)

  for removedString in [leftRemoveString, rightRemoveString]:

    if isPalindrome(removedString):
      return True



  return False

t = int(input())
for _ in range(t):
  string = list(input())
  n = len(string)
  dif_left, dif_right = None, None

  # 회문인지 검사

  if isPalindrome(string):
    print(0)
    continue

  # # # 회문이 아니면 유사 회문인지 검사 (회문에서 달랐던 부분만 하나씩 빼서 검사)
  if isSimiPar(string):
    print(1)
    continue
  # 유사 회문도 아니면 끝
  else:
    print(2)
