

# def solution(skill, skill_trees):
#     answer = 0
#     print()
#     for i in range(len(skill_trees)):
#         tmp = "" 
#         for k in skill_trees[i]:

#             if k in skill :
#                 tmp+=k

#         if len(tmp) == 0:
#             answer += 1
#             continue

#         p = skill.index(tmp[0])
 
#         if skill[p:len(tmp)] == tmp:
#             answer += 1

#     return answer

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        
        pre_skill = ""
        flag = 1
        for i in range(len(skill_tree)):
            
            if skill_tree[i] in skill:
                pre_skill += skill_tree[i]
                if pre_skill != skill[:skill.index(skill_tree[i])+1]:
                    flag = 0
                    break
   
        if flag == 1:
            answer += 1
                

    return answer

print(solution("CBD", [ "CBADF"]))
print(solution("BDC", ["AAAABACA"]),0)
print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]), 4)
print(solution("CBD", ["C", "D", "CB", "BDA"]), 2)