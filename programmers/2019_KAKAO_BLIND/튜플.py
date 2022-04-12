def solution(s):
    answer = []
    
    s = s.replace("{{","")
    s = s.replace("}}","")
    s = s.replace("'","")
    s = s.split("},{")
    s = sorted(s, key = lambda x:len(x))

    s = [list(map(int, i.split(","))) for i in s]

    tmp = tuple()
    for i in range(len(s)):
        tmp += tuple(s[i])
    
    for i in tmp:
        if i not in answer:
            answer.append(i)
    return answer



print(solution('{{4,2,3},{3},{2,3,4,1},{2,3}}'))