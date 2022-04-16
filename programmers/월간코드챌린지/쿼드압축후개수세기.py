
answer = [0, 0]
def solution(arr):
    n =  len(arr)

    tmp = []
    for i in range(n):
        for j in range(n):
            tmp.append(arr[i][j])
    if 1 == len(set(tmp)): # 압축가능 and 원소일 때 
        if tmp[0] == 1:
            answer[1] += 1
        else:
            answer[0] += 1
        return answer
    
    nHalf = int(n/2)
    tmps = None

    for i in range(4):
        if i==0:
            tmps = Parsing(arr, 0, 0, nHalf, nHalf)
        
            solution(tmps)
        elif i==1:
            tmps =  Parsing(arr,nHalf, 0, n, nHalf)
            solution(tmps)
        elif i== 2:
            tmps =  Parsing(arr, 0,nHalf, nHalf,n)
            solution(tmps)
        elif i==3:
            tmps =  Parsing(arr, nHalf,nHalf, n,n)
            solution(tmps)

    return answer

def Parsing(arr, x1, y1, x2, y2):
    tmp = []

    for i in range(x1, x2):
        for j in range(y1, y2):
            tmp.append(arr[i][j])

    nn = y2-y1
    count = 0
    tmps = [[0]*nn for i in range(nn)]    

    for i in range(1, len(tmp) + 1):
        tmps[count][(i-1)%nn] = tmp[i-1] 
     
        if i % nn == 0:
            count += 1
 
    return tmps


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[0,0],[0,0]]))