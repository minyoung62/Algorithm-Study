


def solution(s):
    answer = 0
    n = len(s)


    rotateS = list(s)
    for i in range(n):
        stack = []
        for j in rotateS:
            if j == "(" or j == "{" or j == "[":
                stack.append(j)
            else:
                if len(stack) == 0:
                    stack.append(j)
                    break
                else:
                    jj = stack[-1]

                if jj == "(" and j ==')':
                    stack.pop()
                
                elif jj == "[" and j ==']':
                    stack.pop()
                    
                elif jj == "{" and j =='}':
                    stack.pop()
                    
        if len(stack) == 0:
            answer += 1

        rotateS.append(rotateS.pop(0))

    return answer

print(solution("[](){}"))