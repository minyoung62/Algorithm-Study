import sys

M = int(sys.stdin.readline())
ans=[]
S = [0]*21

for _ in range(M):
    order = sys.stdin.readline().strip()

    try:
        command, num = order.split()
        num = int(num)

        if command == 'add': 
            S[num] = 1

        elif command == 'remove':
            S[num] = 0

        elif command == 'check':
            if S[num]==1:
                print(1)
            else: 
                print(0)

        elif command == 'toggle':
            if S[num] == 1:
                S[num] = 0
            else:
                S[num] = 1

    except:
        if order == 'all':
            S = [1]*21

        elif order == 'empty':
            S = [0]*21