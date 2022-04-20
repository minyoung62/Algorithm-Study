import math

def solution(numbers, hand):
    answer = ''

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    maps = [[1, 2, 3]
        ,[4, 5,6]
        ,[7, 8, 9]
        ,["*", 0, "*"]]

    pos = dict()
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            pos[maps[i][j]] = (j, i)

    print(pos)
    L = (0, 3)
    R = (2, 3)
    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            L = pos[number]
        elif number in [3, 6, 9]:
            answer  += "R"
            R = pos[number]
        else:
            p = pos[number]
            l_p = abs(L[0] - p[0]) + abs(L[1] - p[1])
            r_p = abs(R[0] - p[0]) + abs(R[1] - p[1])
    
            if l_p > r_p:
                answer += "R"
                R = pos[number]
            elif r_p > l_p:
                answer += "L"
                L = pos[number]
            else:
                if hand == "right":
                    answer += "R"
                    R = pos[number]
                else:
                    answer += "L"
                    L = pos[number]

            



    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))