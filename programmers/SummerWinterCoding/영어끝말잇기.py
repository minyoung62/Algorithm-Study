import math
def solution(n, words):
    answer = []
    im = []
    first = words[0]
    if len(first) == 1:
        return [1, 1]
    im.append(first)
    count = 2
    for i, word in enumerate(words[1:]):
        i+=1
        if word in im or first[-1] != word[0] or len(word) == 1:

            answer.append(count)
            answer.append(math.ceil((i+1)/n))
            return answer
        count %= n
        count += 1
        first = word
        im.append(word)

    if len(answer) == 0:
        answer = [0, 0]

    return answer

print(solution(3, ["a", "a", "kaw", "sdfwheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,['land', 'dream', 'mom', 'mom', 'ror']))