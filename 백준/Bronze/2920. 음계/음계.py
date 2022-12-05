a = list(map(int, input().split()))

isAscending = True
isDescending = True

for i in range(len(a)):
  if i==0:
    continue
  elif a[i] -1 == a[i-1]:
    continue
  isAscending = False


for i in range(len(a)):
  if i==0:
    continue
  elif a[i] + 1 == a[i-1]:
    continue
  isDescending = False



if isAscending:
  print("ascending")
elif isDescending:
  print("descending")
else:
  print("mixed")
