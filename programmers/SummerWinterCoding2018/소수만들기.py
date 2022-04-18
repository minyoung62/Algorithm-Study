from itertools import combinations
import math

def elatonic(n):
    array = [True for i in range(n + 1)]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

def solution(nums):
    answer = 0

    cList = combinations(nums, 3)

    sumcList =  [sum(i) for i in cList]

    maxC = max(sumcList)

    array = elatonic(maxC)

    for sums in sumcList:
        
        if array[sums]:
            answer += 1

    return answer

print(solution([1,2,3,4]))