## 서로소 집합(Disjoint Sets)
# 서로소 집합: 공통 원소가 없는 두 집합
# ex) {1, 2}, {3, 4}는 서로소 집합, {1, 2}, {2, 3}은 서로소 집합이 아님

## 서로소 집합 자료구조
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 서로소 집합 자료구조는 두 종류의 연산을 지원
# 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합을 합치는 연산
# 찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# 서로소 집합 자료구조는 합치기 찾기(Union Find) 자료구조라고 불리기도 합니다

# 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같음
# 1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
#     1) A와 B의 루트 노드 A', B'를 각각 찾습니다.
#     2) A'를 B'의 부모 노드로 설정합니다.
# 2. 모든 합집합(Union) 연산을 처리할 때까지 1번의 과정을 반복

# 노드의 개수 크기의 부모 테이블(노드 번호, 부모)을 초기화(처음에는 자기 자신을 부모로 설정)
# 합집합 연산을 수행해서 더 큰 번호에 해당하는 루트노드의 부모를 낮은 번호의 루트노드로 설정
# 나머지 합집합 연산도 같은 방식으로 반복

# 서로소 집합 자료구조에서는 연결성을 통해 손쉽게 집합의 형태를 확인할 수 있음
# 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없음
# 루트 노드를 찾기 위해 부모 테이블을 계속해서 확인하며 거슬러 올라가야 함

## 서로소 집합 자료구조 기본적인 구현 방법 EX) v(6) e(4), Union(1,4), Union(2,3), Union(2,4), Union(5,6) => {1,2,3,4}  {5,6} 서로소 집합 
def find_parent(parent, x):  # 특정 원소가 속한 집합을 찾기
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0]*(v + 1)  # 부모 테이블 초기화하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기, 루트 노드가 같은 노드이면 같은 집합
print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력하기, 루트가 아닌 부모 정보를 담고 있음
print("부모 테이블: ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")


# 서로소 집합 자료구조 기본적인 구현 방법의 문제점
# 합집합(Union) 연산이 편향되게 이루어지는 경우 찾기(Find) 함수가 비효율적으로 동작 
#  ex) v(5) e(4), Union(4,5), Union(3,4), Union(2,3), Union(1,2) =>  1 <- 2 <- 3 <- 4 <- 5 
# 최악의 경우에는 찾기(Find) 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V) 입니다

# 찾기(Find) 함수를 최적화하기 위한 방법으로 경로 압축(Path Compression)을 이용할 수 있음
# - 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신
def find_parent(parent, x):  # 특정 원소가 속한 집합을 찾기
    #  루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 경로 압축 기법을 적용하면 각 노드에 대하여 찾기(Find) 함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모 노드가 됨
# 기본적인 방법에 비하여 시간 복잡도가 개선됨

## 서로소 집합 자료구조 경로압축
def find_parent(parent, x):  # 특정 원소가 속한 집합을 찾기
    #  루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0]*(v + 1)  # 부모 테이블 초기화하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기, 루트 노드가 같은 노드이면 같은 집합
print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력하기, 루트 정보를 담고 있음
print("부모 테이블: ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")


## 서로소 집합을 활용한 사이클 판별
# 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용 가능
# - 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있음
# 사이클 판별 알고리즘은 다음과 같음
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인(Find 함수)
#     1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(Union) 연산을 수행
#     2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것
# 2. 그래프에 포함되어있는 모든 간선에 대하여 1번 과정을 반복

def find_parent(parent, x):  # 특정 원소가 속한 집합을 찾기
    #  루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화하기

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    
    if find_parent(parent, a) == find_parent(parent, b): # 사이클이 발생한 경우(같은 집합에 있다면) 종료
        cycle = True
        break
    else: # 사이클이 발생하지 않았다면(같은 집합에 있지 않다면) 합집합(Union) 연산 수행
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
