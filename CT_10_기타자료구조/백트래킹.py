## 백트래킹과 n-Queens 문제 https://www.youtube.com/watch?v=HRwFgtiqHH0
# 되추적(backtracking): 임의의 집합(set)에서 주어진 기준대로 원소의 순서를 선택하는 문제를 푸는데 적합
# 트리 자료구조의 변형된 깊이우선탐색(DFS:depth-first-search)
# 모든 문제 사례에 대래서 효율적이지 않지만 많은 문제 사례에 대해서 효율적
#  ex) n-Queens, 부분집합의 합, 0-1 배낭문제, 미로찾기 등

# 상태공간트리(State Space Tree)
# 상태 공간: 해답을 탐색하기 위한 탐색 공간
# 상태공간트리: 탐색 공간을 트리 형태의 구조로 암묵적으로 해석

# 백트래킹 기법
# 상태공간트리를 깊이우선탐색으로 탐색
# 방문 중인 노드에서 더 하위 노드로 가면 해답이 없을 경우
#  - 해당 노드의 하위 트리를 방문하지 않고 부모 노드로 되돌아감(backtrack)

# 유망함(promising)
# 방문 중인 노드에서 하위 노드가 해답을 발견할 가능성이 있으면 유망(promising)
# 하위 노드에서 해답을 발견할 가능성이 없으면 유망하지 않음(nonpromising)

# 백트래킹과 가지치기(pruning)
# 백트래킹: 상태공간트리를 DFS로 탐색
# 방문 중인 노드가 유망한지 체크하고 만약 유망하지 않으면, 부모 노드로 되돌아감(backtrack)

# 가지치기(pruning)
# 유망하지 않으면 하위 트리를 가지치기함
# 가지치기한 상태: 방문한 노드의 방문하지 않는 하위 트리(pruned state)


## 일반적인 백트래킹 알고리즘(pseudo code)
# void checknode(v):
# {
#     node u;
#     if promising(v)
#         if v에 해답이 있으면:
#             해답을 출력;
#     else
#         for v의 모든 자식 노드 u에 대해서:
#             checknode(u);
# }

# 백트래킹 알고리즘의 구현
# 상태공간트리를 실제로 구현할 필요는 없음
# 현재 조사중인 가지의 값에 대해 추적만 하면 됨
# 상태공간트리는 암묵적으로 존재한다고 이해하면 됨

## n-Queens 문제: 백트래킹(backtracking)
# 백트래킹으로 문제 해결: 임의의 집합에서 기준에 따라 원소의 순서를 선택
# n-Queens 문제에 적용
#  - 임의의 집합(set): 체스보드에 있는 n^2개의 가능한 위치
#  - 기준(criterion): 새로 놓을 퀸이 다른 퀸을 위협할 수 없음
#  - 원소의 순서(sequence): 퀸을 놓을 수 있는 n개의 위치

# ex) 4-Queens문제(n=4)
# 4개의 퀸을 4 X 4 체스보드에 배치
#  - 일단 기본 가정으로 같은 행(row)에는 놓을 수 없음
# 후보 해답: 4 x 4 x 4 x 4 = 256 가지의 탐색 공간이 있음(4가지 행에서 4열에 각각 퀸을 놓을 수 있는 경우의 수는 4이므로)
#  - 상태공간트리의 리프 노드의 개수가 256개
#  - 부모 노드에 퀸이 놓였을 때, 자식 노드가 서로 공격할 수 있다면 해당 subtree는 promising하지 못해 prununing(가지 치기)


## 유망 함수(promising function)의 구현
# 같은 열(column)이나 같은 대각선(diagonal)에 놓이는 지를 확인
# 유망의 조건1: 같은 열 체크
# col[i]: i번째 행(row)에서 퀸이 놓여있는 열(column)의 위치
# col[k]: k번째 행(row)에서 퀸이 놓여있는 열(column)의 위치
# col[i] == col[k]: 같은 열에 놓이게 되므로, 유망하지 않다(non promising)
# 유망의 조건2: 대각선 체크
# 왼쪽에서 위협하는 퀸에 대해서 열에서의 차이는 행에서의 차이와 같다
# col[i] - col[k] == i - k
# 오른쪽에서 위협하는 퀸에 대해서 열에서의 차이는 행에서의 차이의 마이너스와 같다
# col[i] - col[k] == -(i - k)
# => col[i]와 col[k]의 절대값으로 대각선 위협 판단


## Backtracking Algorithm for the n-Queens Problem
def n_queens(i, col):
    n = len(col) - 1
    if promising(i, col): 
        if i == n: #  promising하고 마지막 행이면(퀸이 위치할 수 있는 자리이고 마지막 행까지 체크해봤을때)
            print(col[1 : (n + 1)]) # 해당하는 col 값의 row 번호를 출력
            # ex) [2, 4, 1, 3] 이면 1열은 row가 2, 2열에 row가 4 ...
        else:
            for j in range(1, n + 1): # 모든 행 체크
                col[i + 1] = j 
                n_queens(i + 1, col) # 재귀 호출

def promising(i, col):
    k = 1
    flag = True
    while k < i and flag: # 현재 열과 다른 열 비교, flag가 False이면 탈출
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k: # 같은 열(column) 체크, 같은 대각선(diagonal) 체크
            flag = False
        k += 1
    return flag

n = 1
col = [0] * (n + 1)
n_queens(0, col)