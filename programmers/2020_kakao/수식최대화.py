

from itertools import permutations
import math
def solution(expression):
    answer = 0

    oper = ['+','-','*']

    tmpL = []
    tmp = ""
    operSet = []
    for i in range(len(expression)):
        
        if expression[i] not in oper:
            tmp += expression[i]
        else:
            tmpL.append(int(tmp))
            tmp = ""
            tmpL.append(expression[i])
            operSet.append(expression[i])
    tmpL.append(int(tmp))
    opers = set(operSet)

    result = []
    import copy

    for oper in permutations(opers, len(opers)): # 순열로 oper 순서 부여
        tmpList = copy.deepcopy(tmpL)
        tmp=[]
        print(oper)

        for o in oper: # 부여받은 순서대로 계산 

            oPositonList = []
            for i in range(len(tmpList)):
                if o == tmpList[i]:
                    oPositonList.append(i)
            print(oPositonList)
            while oPositonList:
                op=oPositonList.pop(0)
                oPositonList = [i-2 for i in oPositonList]
                print(op)
                print(tmpList)
                if o == "+":
                    tmpList[op-1] = tmpList[op-1] + tmpList[op+1]
                elif o == "-":
                    tmpList[op-1] = tmpList[op-1] - tmpList[op+1]
                elif o == "*":
                    tmpList[op-1] = tmpList[op-1] * tmpList[op+1]
                tmpList.pop(op)
                tmpList.pop(op)
        result.append(abs(tmpList[0]))
    print(result)


    answer = max(result)
    
    return answer

print(solution("100-200*300-500+20"))