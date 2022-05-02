from itertools import *
from collections import Counter
def solution(orders, course):
    answer = []
    
    for i in course:
        tmp = []
        for order in orders:
            for j in combinations(order, i):
                tmp.append("".join(sorted(j)))
        l = Counter(tmp).most_common()
        for i in l:
            if i[1] > 1 and i[1] == l[0][1]:
                answer.append(i[0])


    return sorted(answer)

o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
c = [2,3,4]
print(solution(o,c))