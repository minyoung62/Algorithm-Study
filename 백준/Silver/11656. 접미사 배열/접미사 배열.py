n = input()

a = []
for i in range(len(n)):
  a.append(n[i:])
a.sort()

for i in a:
  print(i)
