## 바이너리 인덱스 트리(Binary Indexed Tree, BIT, 펜윅 트리)

# 데이터 업데이트가 가능한 상황에서의 구간 합(Interval Sum) 문제
# BOJ '구간 합 구하기' 문제: https://www.acmicpc.net/problem/2042
# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 
# 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 
# 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.
# 데이터의 개수: N(1 <= N <= 1,000,000)
# 데이터 변경 횟수: M(1 <= M <= 10,000)
# 구간 하 계산 횟수: K(1 <= K <= 10,000)


## 바이너리 인덱스 트리(Binary Indexed Tree)
# 바이너리 인덱스 트리는 2진법 인덱스 구조를 활용해 구간 합 문제를 효과적으로 해결 가능한 자료구조
#  - 펜윅 트리(fenwick tree)라고도 함
# 0이 아닌 마지막 비트를 찾는 방법
#  - 특정한 숫자 K의 0이 아닌 마지막 비트를 찾기 위해서 K & -K를 계산하면 됨(비트 연산자 &)

# 파이썬에서 0이 아닌 마지막 비트를 찾는 법
# K & -K 계산 결과 예시
n=8
for i in range(n + 1):
    print(i, "의 마지막 비트: ", (i & -i))

# 트리 구조 만들기: 0이 아닌 마지막 비트 = 해당 인덱스가 저장하고 있는 값들의 개수
# 특정 값을 변경할 때: 0이 아닌 마지막 비트만큼 더하면서 구간들의 값을 변경
# _______________________________________________________________________
# | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
# |                             1 ~ 16                                   |
# |             1 ~ 8             |                9 ~ 16                |
# |     1 ~ 4     |               |      9 ~ 12      |                   |
# | 1 ~ 2 |       | 5 ~ 6 |       | 9 ~ 10 |         | 13 ~ 14 |         |
# | 1 |   | 3 |   | 5 |   | 7 |   | 9 |    | 11 |    | 13 |    | 15 |    |
# ------------------------------------------------------------------------


## 바이너이 인덱스 트리 - 누적 합(Prefix Sum)
# 1부터 N까지의 합(누적 합) 구하기: 0이 아닌 마지막 비트만큼 빼면서 구간들의 값의 합 계산
#  - 최악의 경우에도 O(logN)의 시간 복잡도를 가짐


## 바이너리 인덱스 트리 구현, O(logN) 시간 복잡도를 가짐
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 데이터의 개수, 변경 횟수, 구간 합 계산 횟수 입력받기

# 전체 데이터의 개수는 최대 1,000,000개
arr = [0] * (n + 1) # 각각의 데이터에 대한 값
tree = [0] * (n + 1) # 바이너리 인덱스 트리에 대한 정보

def prefix_sum(i): # i번째 수까지의 누적 합을 계산하는 함수
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i) # 0이 아닌 마지막 비트만큼 빼가면서 이동
    return result

def update(i, dif): # i번째 수를 dif만큼 더하는 함수
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start, end): # start부터 end까지의 구간 합을 계산하는 함수
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1: # 업데이트(update) 연산인 경우
        update(b, c - arr[b]) # 바뀐 크기(dif)만큼 적용
        arr[b] = c
    else: # 구간 합(interval sum) 연산인 경우
        print(interval_sum(b, c))