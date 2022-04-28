

# def solution(sticker):
#     answer = 0
#     n = len(sticker)
#     d1 = [0] * (n)
#     d2 = [0] * (n)
              

#     if len(sticker) <= 3:
#         return max(sticker)


#     sticker1 = sticker[1:]
#     sticker1.insert(0, 0 )
#     sticker2 = sticker[:-1]
#     sticker2.insert(0, 0 )
#     d1[1] = sticker1[1]
#     d1[2] = sticker1[2]
#     d2[1] = sticker2[1]
#     d2[2] = sticker2[2]
#     for i in range(1, n):
#         d1[i] = max(sticker1[i] + d1[i - 2], d1[i - 1])
#         d2[i] = max(sticker2[i] + d2[i - 2], d2[i - 1])
    


#     answer = max(d1[-1], d2[-1])
    

#     return answer

def solution(sticker):
    answer = 0

    if len(sticker) <= 3:
        return max(sticker)
    
    dp1 = [0] * (len(sticker) -1)
    dp1[0], dp1[1] = sticker[0], sticker[1]
    
    dp2 = [0] * (len(sticker) -1)
    dp2[0], dp2[1] = sticker[1], sticker[2]
    
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i + 1])
    
    answer = max(dp1[-1], dp2[-1])
    
    return answer
# print(solution([1, 3, 2, 5, 4]))

print(solution([5, 1, 16, 17, 16] ))