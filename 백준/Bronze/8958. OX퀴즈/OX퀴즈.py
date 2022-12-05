n = int(input())

def getAnswer(a):
  seq = 0
  total = 0
  for i in range(len(a)):
    if a[i] == "O":
      seq += 1
      total += seq
    else:
      seq = 0
  return total

for i in range(n):
  a = list(input())

  ans = getAnswer(a)
  print(ans)
