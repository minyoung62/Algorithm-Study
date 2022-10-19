
def getOne(a):
  rank = 1
  moneys = [0,500,300,200,50,30,10]
  for i in range(1, 7):
    for j in range(1,i+1):
      if rank == a:
        return moneys[i]
      rank += 1

  return 0
def getTwo(b):

  rank = 1
  moneys = [0,512,256,128,64,32]
  for i in range(0, 5):
    for j in range(1,2**i+1):

      if rank == b:
        return moneys[i+1]
      rank += 1

  return 0
t = int(input())
for _ in range(t):
  a, b = tuple(map(int, input().split()))
  print((getOne(a) + getTwo(b))* 10000)
