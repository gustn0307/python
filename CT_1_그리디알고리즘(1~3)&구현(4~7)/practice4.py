## 구현 - 상하좌우
## N x N 크기의 1 x 1 크기의 정사각형으로 나누어져 있는 정사각형 공간에서 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)일 때 
## 시작좌표는 (1, 1)이고 L, R, U, D(왼 오 위 아래) 문자가 적혀있는 계획서를 보고 이동 (정사각형 공간을 벗어나는 움직임은 무시)

## 내 답안
n=int(input())
mv = input().split()
result = [1,1] # 궅이 리스트로 안하고 x, y 두 변수를 활용해도 됨
cnt = len(mv)

for i in range(cnt):
    if(mv[i]=="U"): # 위로
        if(result[0]==1):
            continue
        result[1]-=1
    elif(mv[i]=="D"): # 아래로
        if(result[1]==n):
            continue
        result[0]+=1
    elif(mv[i]=="R"): # 오른쪽으로
        if(result[1]==n):
            continue
        result[1]+=1
    else: # 왼쪽으로
        if(result[1]==1):
            continue
        result[1]-=1
        
print(result[0],result[1],sep=" ")

## 동빈나 답안 => dx, dy 리스트를 이용해 각 이동 방향에 따른 증감을 이동 방향에 따른 증감과 i로 접근 할 수 있도록 순서를 맞추고 간단하게 구현
n=int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types=['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)): # L R U D 중 무엇인지 확인
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx,ny

print(x, y)