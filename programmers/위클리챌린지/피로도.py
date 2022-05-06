from itertools import *

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for dungeon in permutations(dungeons, n):
        count = 0 
        piro = k
        for i in dungeon:
            if piro >= i[0]:
                piro -= i[1]
                count += 1

        answer = max(answer, count)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))