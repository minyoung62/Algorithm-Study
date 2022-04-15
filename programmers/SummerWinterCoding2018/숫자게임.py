
def solution(A, B):
    answer = 0

    A = sorted(A, key = lambda x : -x)
    B = sorted(B, key = lambda x:  -x)

    for i in range(len(A)):
        if A[i] < B[i]:
            answer += 1


    return answer

print(solution([5,1,3,7], [2,2,6,8]))