def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 != 0:
            n = (n - 1) / 2
            ans += 1
        else:
            n /= 2

    return ans

print(solution(6))

print(solution(5))

print(solution(5000))



def solution(n):
    ans = 0
    
    while n>0:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n - 1) // 2
            ans += 1

    return ans