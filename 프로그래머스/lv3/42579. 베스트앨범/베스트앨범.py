def solution(genres, plays):
    answer = []
    gSet = set(genres) # 장르 집합 ( 중복 제거 )
    gDic={} 
    for genre in gSet: # 장르별로 plays 담아줄 list만듦 
        gDic[genre]=[]
    
    for i,genre in enumerate(genres):  
        gDic[genre].append((plays[i],i)) #{'pop' : [ [600,1] ]} 장르별로 plays와 index를 같이 담아줌

    gSumDic={} # 각 장르별 plays의 합 
    for genre in gSet:
        gDic[genre]=sorted(gDic[genre],key=lambda x: x[0],reverse=True) #lambda식을 통해 각 장르(키)의 plays기준으로 정렬
        sum=0
        for i in gDic[genre]:
            sum+=i[0] 
        gSumDic[genre]=sum #각 장르별 plays 합
    print("t",gSumDic)

    t=sorted(gSumDic.items(),key=lambda x:x[1],reverse=True) 
    
    count=0
    for i in range(len(t)):
        t[i]=t[i][0]

    for genre in t:
        for i in gDic[genre][:2]:
            answer.append(i[1])
            count+=1

    
    return answer