def solution(nums):
    answer = 0
    half = len(nums)//2
    
    s = set(nums)
    
    if half <= len(s):
        answer = half
    else:
        answer = len(s)
        
    return answer