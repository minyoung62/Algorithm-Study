

def solution(skill, skill_trees):
    answer = 0
    print()
    for i in range(len(skill_trees)):
        tmp = "" 
        for k in skill_trees[i]:

            if k in skill :
                tmp+=k

        if len(tmp) == 0:
            answer += 1
            continue

        p = skill.index(tmp[0])
 
        if skill[p:len(tmp)] == tmp:
            answer += 1

    return answer

print(solution("ABCDE", ["BA","AB", "CBADF", "AECB", "BDA"]))
print(solution("BDC", ["AAAABACA"]),0)
print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]), 4)
print(solution("CBD", ["C", "D", "CB", "BDA"]), 2)