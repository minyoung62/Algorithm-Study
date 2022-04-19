
INF = float('inf')
def binary_search(l, r, n, times):

    answer = INF
    while l <= r :

        mid = (l + r) // 2
        sum = 0
        for i in range(len(times)):
            sum += mid // times[i]
        
        if sum >= n:
            answer = min(answer, mid)

            r = mid - 1
        else:
            l = mid + 1

    return answer



def solution(n, times):
    answer = 0
    l = 0
    r = max(times) * n
    answer = binary_search(l, r, n, times)


    return answer

print(solution(6, [7, 10]))