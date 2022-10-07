

from sys import stdin
n, m = map(int, stdin.readline().split())

memo = set()
for _ in range(n):
  memo.add(input())

for i in range(m):
  keywords = stdin.readline()[:-1].split(',')
  
  for keyword in keywords:
    if keyword in memo:
      memo.remove(keyword)
      n -= 1
  print(n)
