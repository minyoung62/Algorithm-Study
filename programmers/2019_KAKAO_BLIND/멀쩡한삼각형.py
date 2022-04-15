import math

# def solution(w,h):
#     answer = 0
    
#     if h<w:
#         w, h = h, w

#     delta = h/w
#     print(delta)
#     x1 = math.ceil(delta)
#     print(x1)
#     answer = ((w*h)) - ((x1 * w))
    
    
#     return answer
from math import ceil, floor

def solution(w, h):

    if w == h:
        return w*h - w
    elif w == 1 or h == 2:
        return 0

    c = 0
    delta = h/w
    for i in range(w):
        c += ceil(h*(i+1)/w) - floor(h*i/w)
    
    return w*h - c


print(solution(8,12))