
from collections import Counter

def solution(str1, str2):
    answer = 0

    multiSet = [[],[]]

    str1 = str1.lower()
    str2 = str2.lower()

    for j, s in enumerate([str1, str2]):
        for i in range(len(s)-1):
            ss = "".join(s[i]+s[i+1])
            if ss.isalpha() == False:
                continue
            multiSet[j].append(ss)
    print(multiSet)

    multiIntersection = 0
    multiUnion = 0

    intersection = set(multiSet[0]) & set(multiSet[1])
    union = set(multiSet[0]) | set(multiSet[1])

    c1 = Counter(multiSet[0])
    c2 = Counter(multiSet[1])

    for s in intersection:
        multiIntersection += min(c1[s], c2[s])
    for s in union:
        multiUnion += max(c1[s], c2[s])

    if multiUnion == 0:
        return 65536

    answer = int((multiIntersection) / (multiUnion) * 65536)

    return answer

print(solution('aa1+aa2','AAAA12'))