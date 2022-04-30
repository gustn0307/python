## 음료수 얼려먹기 : N x M 크기의 얼음 틀이 있고 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됨
## 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주함
## 이때 얼음틀의 모양이 주어졌을 때 총 아이스크림의 개수를 구하는 프로그램을 작성

## 내 답안
# n, m = map(int, input().split())
# ice=[[]]
# iceCream=0
# link=[[]]
# for i in range(n):
#     ice.append(input())

# for i in range(1, n+1):
#     for j in range(m):
#         if j < m-1:
#             if int(ice[i][j]) == 0 and int(ice[i][j+1]) == 0:
#                 link.append(ice[i][j])
#         if j > 0:
#             if int(ice[i][j]) == 0 and int(ice[i][j-1]) == 0: 
#                 link.append(ice[i][j])
#         if i < n:
#             if int(ice[i][j]) == 0 and int(ice[i+1][j]) == 0:
#                 link.append(ice[i][j])
#         if i > 1:
#             if int(ice[i][j]) == 0 and int(ice[i-1][j]) == 0:
#                 link.append(ice[i][j])
        
# print(link)
# print(ice)

## 동빈나 답안
## 이 문제는 DFS 혹은 BFS로 해결할 수 있음
## 일단  얼을을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 할 수 있음
## 값이 0일 때만 연결하고 방문처리
## DFS를 활용하는 알고리즘은 다음과 같음
## 1. 특정한 지점의 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
## 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
## 3. 모든 노드에 대하여 1 ~ 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 => 1로 바꾸면서 상하좌우가 모두 1로 둘러 쌓이면 result++
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False

# N, M을 공백을 기준으로 구분하여 int형으로 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result) # 정답 출력


