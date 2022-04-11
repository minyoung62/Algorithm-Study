def solution(record):
    answer = []
    userId = dict()
    result = []
    for s in record:
        sList = tuple(s.split(" "))
        if len(sList) == 3:
            info, uid, nickname = sList
            userId[uid] = nickname
            if info == "Change":
                userId[uid] = nickname
            else:
                result.append([uid, info])
        else:
            leave, uid = sList
            result.append([uid, leave])

            
    for r in result:
        uid, info = tuple(r)
        if info == "Enter":
            info = "들어왔습니다."
        else:
            info = "나갔습니다."
        q = userId[uid]+"님이 "+info
        answer.append(q)




    return answer

a=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(a))