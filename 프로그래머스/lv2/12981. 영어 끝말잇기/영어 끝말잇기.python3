# import math
# def solution(n, words):
#     answer = []
#     im = []
#     first = words[0]
#     if len(first) == 1:
#         return [1, 1]
#     im.append(first)
#     count = 2
#     for i, word in enumerate(words[1:]):
#         i+=1
#         if word in im or first[-1] != word[0] or len(word) == 1:

#             answer.append(count)
#             answer.append(math.ceil((i+1)/n))
#             return answer
#         count %= n
#         count += 1
#         first = word
#         im.append(word)

#     if len(answer) == 0:
#         answer = [0, 0]

#     return answer

def solution(n, words):
    answer = [0, 0]
    
    cicle = len(words) // n
    r = len(words) % n
    

    first=None
    count = 0
    wordList = []
    for i in range(cicle):
        for j in range(n):
            if count == 0 :
                first = words[count]
                
                wordList.append(words[count])
                count += 1
                continue
     
            now = words[count]
            
            if first[-1] != now[0]:
                
                return [j + 1, i + 1]
            elif now in wordList:
               
                return [j + 1, i + 1]
           
            first = now

            wordList.append(words[count])
            count += 1

    for i in range(r):
        now = words[count]
        if first[-1] != now[0]:
            return [i+1, cicle ]
        elif now in wordList:
            return [i+1, cicle ]
        first = now
        wordList.append(words[count])
        count += 1
        
    
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, 	["hello", "one", "even", "never", "now", "world", "draw"]))