

def binarySearch(stringQuery, target, dic):
    arr = dic[stringQuery]
    n = len(arr)
    l = 0
    r = n -1
    ans = 0
    tmp = n

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < target:
            
            l = mid + 1
        else:
            tmp = mid
            r = mid - 1
        
    ans = n - tmp

    return ans

def solution(info, query):
    answer = []

    langs = ["cpp", "java", "python", "-"]
    positions= ["backend", "frontend" ,"-"]
    careers = ["junior", "senior", "-"]
    soulFoods = ["chicken", "pizza", "-"]

    dic = {}
    for lang in langs:
        for position in positions:
            for career in careers:
                for soulFood in soulFoods:
                    dic[lang + position + career + soulFood] = []
    
    for i in info:
        i = i.split(' ')

        for lang in [i[0], '-']:
            for position in [i[1], '-']:
                for career in [i[2], '-']:
                    for soulFood in [i[3], '-']:
                        dic[lang+position+career+soulFood].append(int(i[-1]))

    for key in dic.keys():
        dic[key] = sorted(dic[key])

    for i in range(len(query)):
        q = query[i].split(" and ")
        tmp =  q[-1].split()
        q = q[:-1] + tmp
   

        stringQuery = "".join(q[:-1])
        numberQuery = int(q[-1])

        
        ans = binarySearch(stringQuery, numberQuery, dic)
        answer.append(ans)

    return answer




info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))