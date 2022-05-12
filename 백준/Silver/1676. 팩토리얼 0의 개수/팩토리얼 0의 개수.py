n = int(input())

s = 1
for i in range(n,0,-1):
    s *= i
s = str(s)[::-1]

answer = 0
for i in range(len(s)):
    if s[i] == '0':
        answer += 1
    else:
        break

print(answer)
