## 전보
# 어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우,
# 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
# 예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다
# 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
# 어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다.
# 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보내 메시지를 받게 되는 도시의 개수는 총 몇 개이며
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성
# 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.(1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N)
# 둘째 줄부터 M + 1 번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는
# 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미임(1 <= X, Y <= N, 1 <= Z <= 1,000)
# 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력


## 내 답안
import heapq

INF = int(1e9)

n, m, c = map(int, input().split())  # 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화
tot_time = 0 # 도달할 수 있는 노드(도시)중에서 가장 멀리 있는 노드와의 최단 거리
received_c = 0 # 도달할 수 있는 노드(도시)의 개수

for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미(x번째 리스트에 y와 z를 하나의 튜플로 묶어서 넣어줌)
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어 있지 않다면
        dist, now = heapq.heappop(q)  # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]  # 현재 확인한 노드까지의 거리 값에 그 노드에 인접한 노드까지의 거리값을 더함

            if cost < distance[i[0]]:  # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)  # 다익스트라 알고리즘을 수행

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF or distance[i] == 0:
        continue
    else:  # 도달할 수 있는 경우 거리를 출력
        tot_time = max(tot_time, distance[i])
        received_c += 1

print(received_c, tot_time)


## 동빈나 답안
# 핵심 아이디어: 한 도시에서 다른 도시까지의 최단 거리 문제로 치환 가능
# N과 M의 범위가 충분히 크기 때문에 우선순위 큐를 활용한 다익스트라 알고리즘을 구현
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어 있지 않다면
        dist, now = heapq.heappop(q)  # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]  # 현재 확인한 노드까지의 거리 값에 그 노드에 인접한 노드까지의 거리값을 더함

            if cost < distance[i[0]]:  # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, start = map(int, input().split())  # 노드(도시)의 개수 N, 간선(통로)의 개수 M, 메시지를 보내고자 하는 도시(시작 노드) start
graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
distance = [INF] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미(x번째 리스트에 y와 z를 하나의 튜플로 묶어서 넣어줌)
    graph[x].append((y, z))

dijkstra(start)  # 다익스트라 알고리즘을 수행

max_distance = 0 # 도달할 수 있는 노드(도시)중에서 가장 멀리 있는 노드와의 최단 거리
count = 0 # 도달할 수 있는 노드(도시)의 개수

# 모든 노드로 가기 위한 최단 거리를 출력
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance) # 시작 노드는 제외해야 하므로 count -1을 출력
