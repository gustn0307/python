## 공포도가 X인 모험가는 X 명 이상으로 그룹을 짜서 모험을 떠나야 하는데 여행을 떠날 수 있는 그룹 수의 최댓값
## ex) n=5 이고 각 모험가의 공포도가 2 3 1 2 2 일 때, 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고, 
## 그룹 2에 공포도가 2인 남은 두명을 넣게 되면 총 2개의 그룹을 만들수 있음
## 또한 몇 명의 모험가는 마을에 남아있어도 되기 때문에, 모든 모험가를 그룹에 참여시킬 필요는 없다

## 내 답안
# import time

# n=input()
# h=input().split()
# result=0
# s=sorted(h, reverse=True)

# start_time = time.time() # 측정 시작

# i=0
# while i<int(n): 
#     if(int(s[i])!=1):
#         i=i+(int(s[i])-1)
#         result+=1
#     else:
#         result+=1
#     i+=1  
        
# print(result)
# end_time = time.time() # 측정 종료
# print("time:", end_time - start_time) # 수행 시간 출력


## 동빈나 답안
# 오름차순 정렬 이후에 공포도가 낮은 모험가부터 하나씩 확인
# 앞에서부터 공포도를 하나씩 확인하며 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 설정
# 이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점에서 항상 최소한의 모험가의 수만 포함하여 그룹을 결성함

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    cnt += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if cnt >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1 # 총 그룹의 수 증가
        cnt=0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력

## 직사각형의 세 점을 알 때 나머지 한 점 찾기
# def solution(v):
#     answer = []

#     if(v[0][0]==v[1][0]):
#         answer.append(v[2][0]) 
#     elif(v[1][0]==v[2][0]):
#         answer.append(v[0][0])
#     else:
#         answer.append(v[1][0])

#     if(v[0][1]==v[1][1]):
#         answer.append(v[2][1])
#     elif(v[0][1]==v[2][1]):
#         answer.append(v[1][1])
#     else:
#         answer.append(v[0][1])
    
#     print(answer)
 
#     return answer
# v=[[1, 4], [3, 4], [3, 10]]
# solution(v)
