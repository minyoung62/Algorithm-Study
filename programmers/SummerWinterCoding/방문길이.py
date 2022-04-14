def solution(dirs):
    answer = 0

    
    dic = {
        "U":(-1, 0),
        "L":(0, -1),
        "R":(0, 1),
        "D":(1, 0)
    }
    
    x = 5
    y = 5
    tmp = []
    for i in list(dirs):
        dx, dy = dic[i]

        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11:
            continue

        goto = "".join([str(x), str(y), str(nx), str(ny)])
        back = "".join([str(nx), str(ny), str(x), str(y)])
        if goto not in tmp:
            tmp.append(goto)
            tmp.append(back)
            print(goto)
            answer += 1



        x = nx
        y = ny
        

    
    return answer

print(solution("ULURRDLLU"))
#print(solution("LLLLLLLLLLLLRRRRRRRRRRRRRRRR"))
print(solution("LRLRL"))