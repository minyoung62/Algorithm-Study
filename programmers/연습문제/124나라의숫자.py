def solution(n):
    answer = 0
    tmp = ""
    
    while n:
        if n % 3 == 0:
            tmp += str(3)
            
            n = n//3 - 1
            
        else:
            tmp += str((n % 3))
        
            n = n//3
  
    tmp = list(tmp[::-1])

    for i in range(len(tmp)):
        if tmp[i] == '3':
            tmp[i] = '4'

    answer = "".join(map(str, tmp))


    return answer


print(solution(7))