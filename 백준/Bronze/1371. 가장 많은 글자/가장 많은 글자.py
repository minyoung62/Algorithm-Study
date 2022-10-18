
import sys
a = ""

alphaCntDict = dict()
for i in range(ord('a'), ord('z') + 1):
  alphaCntDict[chr(i)] = 0

a = sys.stdin.read().replace('\n', '').replace(' ','')


for i in range(len(a)):
  if a[i] in alphaCntDict:
    alphaCntDict[a[i]] += 1

alphaCntDictItem = sorted(alphaCntDict.items(), key = lambda x:(-x[1],x[0]))

firstCnt = alphaCntDictItem[0][1]
ans = alphaCntDictItem[0][0]

for alpha, cnt in alphaCntDictItem[1:]:
  if cnt == firstCnt:
    ans += alpha
  else:
    break
print(ans)


