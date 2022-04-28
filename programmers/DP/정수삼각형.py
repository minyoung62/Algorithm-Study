def solution(triangle):
    answer = 0
    
    n = len(triangle[-1])
    
    table = [
        [0] * n 
        for _ in range(n)
    ]

    table[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(len(triangle[i])):   
            table[i-j][j] = triangle[i][j]

    dp = [
        [0] * n
        for _ in range(n)
    ]
    dp[0][0] = table[0][0]
    for i in range(1, n):
        dp[0][i] += dp[0][i-1] + table[0][i]
    for i in range(1, n):
        dp[i][0] += dp[i-1][0] + table[i][0]


    for i in range(1, n):
        for j in range(1, n-i + 1):
            dp[i][j] = max(dp[i-1][j]+table[i][j], dp[i][j-1]+table[i][j])
    
    for i in range(n):
        answer = max(answer, dp[i][n-i-1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))