def solution(s):
    answer = []

    print(bin(int("0011"))[2:])
    
    count = 0
    removeCount = 0
    while s != '1':

        removeCount += s.count('0')
        s = s.replace("0", "")

        s = str(bin(len(s))[2:])
        print(s)
        count += 1 
    
    answer = [count, removeCount]

    return answer

print(solution("110010101001"))