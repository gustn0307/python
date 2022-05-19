from math import *

def solution(alp, cop, problems):
    answer = 0
    n=len(problems)
    maxAlp=0
    maxCop=0
    subAlp=list()
    subCop=lsit()
    cost=0

    for i in range(n):
        maxAlp=max(problems[i][0], maxAlp)
        maxCop=max(problems[i][1], maxCop)
        subAlp.append(abs(problems[i][0] - alp))
        subCop.append(abs(problems[i][1] - cop)) 
        
        
    while alp < maxAlp and cop < maxCop:
        i = 0
        while i < n:
            subAlp.append(abs(problems[i][0] - alp))
            subCop.append(abs(problems[i][1] - cop))

            if alp >= maxAlp and cop >= maxCop:
                break

            if problems[i][0] <= alp and problems[i][1] <= cop:
                if ((problems[i][2] + problems[i][3]) // problems[i][4]) >= 1:
                    if min(subAlp) <= subAlp[i] and min(subCop) <= subCop[i]
                        alp += problems[i][2]
                        cop += problems[i][3]
                        cost += problems[i][4]
                        i=n
            elif problems[i][0] <= alp and problems[i][1] > cop:        
                cop += 1
                cost += 1
                i=n
            elif problems[i][0] > alp and problems[i][1] <= cop:  
                alp += 1
                cost += 1
                i=n         
            elif problems[i][0] > alp and problems[i][1] > cop:
                if problems[i][0] - alp > problems[i][1] > cop:
                    alp+=1
                    cost+=1
                    i=n
                elif problems[i][0] - alp <= problems[i][1] > cop:
                    cop+=1
                    cost+=1
                    i=n
            i+=1
        
    answer = cost
    return answer

print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
