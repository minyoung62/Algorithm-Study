import sys
input = sys.stdin.readline
n = int(input())
childs = [[-1, -1] for i in range(n)]

for i in range(n):
    x, l, r = input().strip().split()

    if l != '.': 
        childs[ord(x) - ord('A')][0] = ord(l) - ord('A')
    if r != '.':
        childs[ord(x) - ord('A')][1] = ord(r) - ord('A')

def in_order(x):
    if x== -1:
        return 
    in_order(childs[x][0])
    print(chr(x + 65), end = '')
    in_order(childs[x][1])

def pre_order(x):
    if x== -1:
        return 
        
    print(chr(x + 65), end = '')
    pre_order(childs[x][0])
    pre_order(childs[x][1])

def post_order(x):
    if x== -1:
        return 
    post_order(childs[x][0])
    post_order(childs[x][1])
    print(chr(x + 65), end = '')


pre_order(0)
print()
in_order(0)
print()
post_order(0)