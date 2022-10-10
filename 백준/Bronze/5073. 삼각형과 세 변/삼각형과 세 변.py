

while True:
  a, b, c = tuple(map(int, input().split()))
  if a == 0 and b == 0 and c == 0:
    break
  tmp = [a,b,c]
  tmp.sort()
  maxNum = tmp[-1]
  minNum = tmp[0] + tmp[1]

  if maxNum >= minNum:
    print("Invalid")
    continue
  if a == b and b == c:
    print("Equilateral")
  elif (a == b or b == c or a == c):
    print("Isosceles")
  elif a != b and b != c:
    print("Scalene")


