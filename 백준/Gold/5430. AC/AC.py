import ast
from collections import deque
t = int(input())

for _ in range(t):
    cmds = list(input())
    n = int(input())
    a = input()
    a = deque(map(int, ast.literal_eval(a)))

    isReverse = False
    isError = False
    for cmd in cmds:
        if cmd == "R":
            if isReverse == True:
                isReverse = False
            else:
                isReverse = True
        else:
            if len(a) == 0:
                print('error')
                isError = True
                break
            else:
                if isReverse:
                    a.pop()
                else:
                    a.popleft()
    if not isError:
        if isReverse:
            a = list(reversed(list(a)))

        print("[" + ','.join(map(str, a)) + "]")

