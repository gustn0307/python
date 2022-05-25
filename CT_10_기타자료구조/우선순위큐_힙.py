## 우선순위 큐(Priority Queue): 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용
#  - 예) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

#  자료구조                       추출되는 데이터
#  스택(Stack)                    가장 나중에 삽입된 데이터
#  큐(Queue)                      가장 먼저 삽입된 데이터
#  우선순위 큐(Priority Queue)    가장 우선순위가 높은 데이터

# 우선순위 큐를 구현하는 방법은 다양
#  1) 단순히 리스트를 이용하여 구현
#  2) 힙(heap)을 이용하여 구현
# 데이터의 개수가 N개일 때, 구현 방식에 따른 시간 복잡도
#  우선순위 큐 구현 방식      삽입 시간   삭제 시간
#  리스트                     O(1)        O(N)
#  힙(Heap)                  O(logN)      O(logN)
# 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일(힙 정렬)
# 이 경우 시간 복잡도는 O(NlogN)


## 힙(Heap)의 특징
# 힙은 완전 이진 트리 자료구조의 일종
# 힙에서는 항상 루트 노드(root node)를 제거
# 최소 힙(min heap)
#  - 루트 노드가 가장 작은 값을 가짐
#  - 따라서 값이 작은 데이터가 우선적으로 제거됨
# 최대 힙(max heap)
#  - 루트 노드가 가장 큰 값을 가짐
#  - 따라서 값이 큰 데이터가 우선적으로 제거됨


## 완전 이진 트리(Complete Binary Tree)
# 완전 이진 트리란 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로
# 데이터가 차례대로 삽입되는 트리를 의미


## 최소 힙 구성 함수 Min-heapify()
# (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체
# 힙에 새로운 원소가 삽입될 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있음
# 힙에서 원소가 제거될 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있음
#  - 원소를 제거할 때는 가장 마지막 노드가 루트 노드의 위치에 오도록 함
# 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있음
#  - 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행


## 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
import sys
import heapq # 파이썬에서 기본적으로 min heap으로 구현되어 있음, 정렬시 오름차순 정렬

input = sys.stdin.readline

def heapsort(iterable): # max heap으로 내림차순 정렬하려면 - 를 추가하여 구현
    h = []
    result = []

    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, -value) # 오름차순
        # heapq.heappush(h, -value) # 내림차순

    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h)) # 오름차순
        # result.append(-heapq.heappop(h)) # 내림차순

    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i], end=" ") 
    

    