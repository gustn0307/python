## 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘
# 각 지점은 그래프에서 노드로 표현
# 지점 간 연결된 도로는 그래프에석 간선을 표현


## 다익스트라 최단 경로 알고리즘
# 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
# 음의 간선이 없을 때 정상적으로 동작(현실 세계의 도로는 음의 간선으로 표현되지 않음)
# 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됨(매 상황에서 가장 비용이 적은 노드를 선택해 과정을 반복)


## 다익스트라 최단 경로 알고리즘 동작과정
# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화(모든 노드까지 가는 비용을 무한대로 설정하고 자기 자신으로 가는 비용은 0으로 설정)
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 위 과정에서 3번과 4번을 반복

# 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있음
# 처리 과정에서 더 짧은 경로를 찾으면 특정 경로가 더 짧은 경로라고 갱신


## 다익스트라 알고리즘의 특징
# 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
# 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않음
# 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음
# 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됨
# 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 함


## 다익스트라 알고리즘 간단한 구현 방법
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든원소를 확인(순차 탐색)
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int,input().split()) # 노드의 개수, 간선의 개수를 입력받기
start = int(input()) # 시작 노드 번호를 입력받기
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
visited = [False] * (n+1) # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력 받기
    a, b, c = map(int, input().split()) 
    graph[a].append((b,c)) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미(a번쨰 리스트에 b와c를 하나의 튜플로 묶어서 넣어줌)

def get_smallest_node(): # 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호를 반환
    min_value = INF
    index = 0 # 최단 거리가 가장 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1): # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node() 
        visited[now] = True

        for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start) # 다익스트라 알고리즘을 수행

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    if distance[i] == INF: # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        print("INFINITY")
    else: # 도달할 수 있는 경우 거리를 출력
        print(distance[i])


## 다익스트라 간단한 구현 방법 성능
# 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 함
# 따라서 전체 시간 복잡도는 O(V^2)
# 일반적으로 코딩테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 코드로 문제를 해결할 수 있음
# 전체 노드의 개수가 5000개 이상이라면 우선순위 큐를 활용


## 우선순위 큐(Priority Queue)
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있음
# Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원


## 힙(Heap)
# 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
# 최소 힙(Min Heap)과 최대 힙(Max Heap)이 있음
# 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됨

# 우선순위 큐 구현 방식     삽입시간    삭제시간
# 리스트                    O(1)        O(N)
# 힙(Heap)                  O(logN)     O(logN)


## 힙 라이브러리 사용 예제: 최소 힙
# 파이썬은 힙 라이브러리가 default가 최소 힙으로 구현되어 있어 우선순위가 낮은 원소부터 나오기 때문에 그냥 넣었다가 꺼내면 오름차순 정렬됨
import heapq

def heapsort(iterable): # 전체 시간 복잡도는 O(NlogN)으로 기본 제공하는 sort()함수와 같은 복잡도
    h=[]
    result=[]

    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value)

    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h))

    return result

result= heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)


## 힙 라이브러리 사용 예제: 최대 힙
# 파이썬은 힙 라이브러리가 default가 최소 힙으로 구현되어 있어 우선순위가 낮은 원소부터 나오기 때문에
# - 기호를 이용해서 넣었다가 꺼내면 오름차순 정렬됨
import heapq

# 내림차순 힙정렬
def heapsort(iterable): # 전체 시간 복잡도는 O(NlogN)으로 기본 제공하는 sort()함수와 같은 복잡도
    h=[]
    result=[]

    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, -value)

    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(-heapq.heappop(h))

    return result

result= heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용
# 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용


##우선순위큐 사용 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int,input().split()) # 노드의 개수, 간선의 개수를 입력받기
start = int(input()) # 시작 노드 번호를 입력받기
graph = [[] for i in range(n + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력 받기
    a, b, c = map(int, input().split()) 
    graph[a].append((b,c)) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미(a번쨰 리스트에 b와c를 하나의 튜플로 묶어서 넣어줌)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start)) 
    distance[start] = 0

    while q: # 큐가 비어 있지 않다면
        dist, now = heapq.heappop(q) # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1] # 현재 확인한 노드까지의 거리 값에 그 노드에 인접한 노드까지의 거리값을 더함

            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start) # 다익스트라 알고리즘을 수행

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    if distance[i] == INF: # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        print("INFINITY")
    else: # 도달할 수 있는 경우 거리를 출력
        print(distance[i])


# 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)
# 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않음
# 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있음
# 직관적으로 전체과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사함
# 시간 복잡도를 O(ElogE)로 판단할 수 있음
# 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있음
# O(ElogE) -> O(ElogV^2) -> O(2Elogv) -> O(ElogV)