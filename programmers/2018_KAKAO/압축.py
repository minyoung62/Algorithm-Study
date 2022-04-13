


def solution(msg):
    answer = []

    dic = dict((chr(ord('A')+i),i+1) for i in range(26))
    
    c = 27
    index = 0
    nindex = 0
    
    while 1:
        w = msg[index : nindex + 1]

        if w in dic.keys(): # 현재 입력(w)가 사전에 있다면 nindex ++           
            nindex += 1
        
        else : # 현재 입력이 사전에 없다면 사전에 추가
            dic[w] = c
            c += 1
            answer.append(dic[msg[index:nindex]])
            index = nindex
        

        if nindex >= len(msg): # 남은 값 추가
            answer.append(dic[msg[index:nindex]])
            break

    return answer

print(solution("KAKAO"))