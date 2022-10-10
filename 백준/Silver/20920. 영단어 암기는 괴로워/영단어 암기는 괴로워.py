
n, m = tuple(map(int, input().split()))

words = [
  input()
  for _ in range(n)
]

memo = []

cntDict = dict()
for i in range(n):
  if len(words[i]) < m:
    continue

  cntDict[words[i]] = cntDict.get(words[i], 0) + 1

for key, item in cntDict.items():
  memo.append((item, len(key), key))

memo.sort(key = lambda x:(-x[0],-x[1],x[2]))

for i in range(len(memo)):
  cnt, lenth, val = memo[i]
  print(val)
