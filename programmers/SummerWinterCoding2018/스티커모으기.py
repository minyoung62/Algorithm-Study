

def solution(sticker):
    answer = 0
    n = len(sticker)
    d1 = [0] * (n)
    d2 = [0] * (n)


    if len(sticker) <= 3:
        return max(sticker)


    sticker1 = sticker[1:]
    sticker1.insert(0, 0 )
    sticker2 = sticker[:-1]
    sticker2.insert(0, 0 )
    d1[1] = sticker1[1]
    d1[2] = sticker1[2]
    d2[1] = sticker2[1]
    d2[2] = sticker2[2]
    for i in range(1, n):
        d1[i] = max(sticker1[i] + d1[i - 2], d1[i - 1])
        d2[i] = max(sticker2[i] + d2[i - 2], d2[i - 1])
    


    answer = max(d1[-1], d2[-1])
    

    return answer

print(solution([1, 3, 2, 5, 4]))