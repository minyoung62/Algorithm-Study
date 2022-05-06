from collections import deque

def solution(people, limit):
    answer = 0

    people.sort()
    q = deque(people)
    while q:
        if len(q) == 1:
            q.pop()
            answer += 1
            break
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
        else:
            q.pop()
        answer += 1


    return answer