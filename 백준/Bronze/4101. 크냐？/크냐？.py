while True:
  a, b = tuple(map(int, input().split()))
  if a == 0 and b == 0:
    break
  
  if a <= b:
    print("No")
  else:
    print("Yes")