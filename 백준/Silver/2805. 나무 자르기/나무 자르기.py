import sys

n,m = map(int,input().split())
input_data = list(map(int,sys.stdin.readline().rstrip().split()))


# 10 , 15 ,17 20
ans = 0
def binary_search(array,target,start,end):
  global ans
  if start > end:
      return ans-1
  total = 0
  mid = (start + end)//2
  for i in array:
      if i > mid:
          total += i - mid

  if total >= target:
      ans = mid
      return binary_search(array,target,mid+1,end)
  else:
      return binary_search(array,target,start,mid-1)

binary_search(input_data,m,0,max(input_data))
print(ans)