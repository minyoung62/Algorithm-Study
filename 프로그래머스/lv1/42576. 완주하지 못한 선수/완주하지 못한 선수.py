def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("1")
    answer=""
    for i in range(0,len(completion)):
        if participant[i] != completion[i]:
            answer=participant[i]
            return answer