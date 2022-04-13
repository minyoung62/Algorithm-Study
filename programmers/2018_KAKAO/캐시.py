from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    firstCache = 0
    cur = 0

    for i in range(len(cities)): # Upper 처리 
        cities[i] = cities[i].upper()

    if cacheSize <= 0 : # 캐시 공간이 0일 때 
        return len(cities) * 5
    


    for city in cities: # 도시들 

        if city not in cache: # 캐시안에 없을 때 
            if len(cache) >= cacheSize: # 캐시가 꽉 찰때
                cache.popleft()
                cache.append(city)
            else: # 공간이 있을 때
                cache.append(city)
            answer += 5

        else: # 캐시안에 있을 때
            cache.remove(city) 
            cache.append(city)
            answer += 1


    return answer

c = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
c = ['c','c','c']
print(solution(1,c))
