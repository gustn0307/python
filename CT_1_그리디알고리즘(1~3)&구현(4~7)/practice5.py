## 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

## 내 답안
n=int(input())

start=[0,0,0,0,0,0]

cnt=0
end=n*3600 + 59*60 + 59
for i in range(end):
    start[5]+=1
    if(start.count(3)>0):
        cnt+=1

    if start[5]==10:
        start[5]=0
        start[4]+=1
        if start[4]==6:
            start[4]=0
            start[3]+=1
    
    if start[3]==10:
        start[3]=0
        start[2]+=1
        if start[2]==6:
            start[2]=0
            start[1]+=1
    
    if start[1]==10:
        start[1]=0
        start[0]+=1

print(cnt)
    

## 동빈나 답안
## 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
## 하루는 86,400초 이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400가지
## 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됨
## 이러한 유형을 완전 탐색(Brute Forcing) 문제 유형이라도 불림( 가능한 모든 경우의 수를 모두 검사해보는 탐색 방법)

h = int(input())

count = 0

for i in range(h + 1): # 시간
    for j in range(60): # 분
        for k in range(60): # 초 
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
    