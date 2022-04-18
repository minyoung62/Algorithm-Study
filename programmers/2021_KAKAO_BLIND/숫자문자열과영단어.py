def solution(s):
    answer = ""
    
    en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dic = dict((x, str(y)) for y, x in enumerate(en))

    # print(dic)

    tmp = ""
    for i in s:
        tmp += i
        if tmp.isdigit():
            answer += tmp
            tmp = ""
            continue
        if tmp in dic.keys():
            answer += dic[tmp]
            tmp = ""


    return int(answer)


print(solution("one4seveneight"))