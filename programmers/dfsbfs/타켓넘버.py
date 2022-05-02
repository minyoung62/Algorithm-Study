from itertools import *

def solution(numbers, target):
    answer = 0
    n = len(numbers)

    for i in product(["+","-"], repeat=n):
        tmp = 0
        for j in range(n):
            t = numbers[j]
            if i[j] == "-":
                t *= -1
            tmp += t
        if tmp == target:
            answer += 1
    return answer
print(solution([1, 1, 1, 1, 1],3))