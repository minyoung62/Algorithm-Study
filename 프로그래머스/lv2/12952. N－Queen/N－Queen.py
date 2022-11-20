a = []
selected = []
nn = 0
ans = 0
chess = [ ]

def canBatch():
    if len(selected) < 2:
        return True

    x1, y1 = selected[-1]
    
    for x2, y2 in selected[:-1]:
        if abs(x1-x2) == abs(y1-y2) or x1==x2 or y1 == y2:
            return False
    return True
    

def choose(cnt):
    global ans, selected
    if cnt == nn:
        ans += 1
        return
    # for i in range(c, len(a)):
    #     selected.append(a[i])
    #     if canBatch():
    #         choose(cnt+1, i+1)
    #     selected.pop()
    for i in range(1,nn+1):
        selected.append(a[i+cnt*nn])
        if canBatch():
            choose(cnt + 1)
        selected.pop()
        
def solution(n):
    global a, nn, chess
    
    nn = n
    answer = 0
    a.append((0,0))
    for i in range(n):
        for j in range(n):
            a.append((i,j))
    
    
    choose(0)
    answer = ans
    return answer