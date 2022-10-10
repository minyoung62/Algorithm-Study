
string = list(input())
boom = list(input())
stack = []

for char in string:
  stack.append(char)

  if stack[-1] == boom[-1] and len(stack) >= len(boom) and stack[-len(boom):] == boom:

    del stack[-len(boom):]

if stack:
  print("".join(stack))
else:
  print("FRULA")
