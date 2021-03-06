## 벨만 포드 최단 경로 알고리즘

## BOJ '타임머신' 문제: https://www.acmicpc.net/problem/11657
# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, 
# A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. 
# C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.
# 도시의 개수: N(1 <= N <= 500), 버스 노선의 개수: M(1 <= M <= 6,000)

# 모든 간선의 비용이 양수일 때는 다익스트라 최단 경로 알고리즘을 사용하면 됨
# 음수 간선이 포함된다면 최단 거리를 계산 할 수 있음
# 하지만 음수 간선의 순환이 포함된다면 최단 거리가 음의 무한인 노드가 발생


## 벨만 포드 최단 경로 알고리즘
# 음수 간선에 관하여 최단 경로 문제는 다음과 같이 분류 가능
#  1) 모든 간선이 양수인 경우
#  2) 음수 간선이 있는 경우
#     1) 음수 간선 순환은 없는 경우
#     2) 음수 간선 순환이 있는 경우
# 벨만 포드 최단 경로 알고리즘은 음의 간선이 포함된 상황에서도 사용할 수 있음
#  - 또한 음수 간선의 순환을 감지할 수 있음
#  - 벨만 포드의 기본 시간 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느립니다

# 벨만 포드 알고리즘은 다음과 같음
# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 다음의 과정을 N - 1번 반복
#  1) 전체 간선 E개를 하나씩 확인
#  2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행
#  - 이때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것
# 다익스트라 최단 거리 알고리즘은 3-1에서 전체 간선이 아닌 특정 노드에 붙어 있는 간선만 확인하는 것이 차이점


## 벨만 포드 알고리즘 VS 다익스트라 알고리즘
# 다익스트라 알고리즘
#  - 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
#  - 음수 간선이 없다면 최적의 해를 찾을 수 있음(음수 간선이 있다면 문제 발생 가능)
# 벨만 포드 알고리즘
#  - 매번 모든 간선을 전부 확인, 따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함
#  - 다익스트라 알고리즘에 비해서 시간이 오래 걸리지만 음수 간선 순환을 탐지할 수 있음


## 벨만 포드 알고리즘 소스코드
import sys
input = sys.stdin.readline
INF=int(1e9) # 무한을 의미하는 값으로 10억을 설정

def bf(start):
    dist[start] = 0 # 시작 노드에 대해 초기화

    for i in range(n): # 전체 n번의 라운드(round)를 반복
        for j in range(n): # 매 반복마다 모든 간선을 확인
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost

                if i == (n - 1):
                    return True
    return False

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수 입력받기
edges= [] # 모든 간선에 대한 정보를 담는 리스트 만들기
dist = [INF] * (n + 1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력받기
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1): # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
        if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
            print("-1")
        else: # 도달할 수 있는 경우 최단 거리 출력
            print(dist[i])

