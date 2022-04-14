
ch={'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
def convert(n, q):
    rev_base = ''

    if n == 0:
        return '0'

    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10 :
            rev_base += ch[str(mod)]
        else:
            rev_base += str(mod)
    return rev_base[::-1]



def solution(n, t, m, p):

    answer = ''

    #  n진 리스트 만들기 

    nList = ""
    for i in range(t*m):
        nList +=  convert(i, n)
    print(nList)
    nList = nList[:t*m]
    nList = "0"+nList
    for i in range(p, len(nList), m):
        print(i)
        answer+=nList[i]

    print(answer)

    return answer

print(solution(16, 16, 2, 3))