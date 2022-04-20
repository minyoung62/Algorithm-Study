def measure(num):
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1

    return c

def solution(n, r):
    answer = 0

    l = [i for i in range(n, r + 1)]

    for i in l:
        
        sum = measure(i)

        if sum % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

print(solution(13, 17))