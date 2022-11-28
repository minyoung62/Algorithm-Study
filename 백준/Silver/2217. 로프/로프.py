
n = int(input())

a = [
  int(input())
  for _ in range(n)
]

a.sort(reverse=True)

weight = [a[i] * (i + 1) for i in range(n)]
print(max(weight))
