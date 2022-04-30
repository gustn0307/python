## 정렬된 배열에서 특정 수의 개수 구하기
## N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음, 이때 수열에서 x가 등장하는 횟수를 계산
## 예를 들어 {1,1,2,2,2,2,3}이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력
## 단 이 문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과판정

## 내답안 
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

if count_by_range(array, x, x) == 0: # 이러면 if else 문에서 각각 한번씩 총 두번 함수가 실행되므로 변수에 값을 넣어서 비교하자
    print(-1)
else:
    print(count_by_range(array, x, x))


## 동빈나 답안
## 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하므로 일반적인 선형 탐색(Linear Search)로는 시간 초과 판정을 받음
## 하지만 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있음
## 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결할 수 있음
## 이진 탐색을 두 번 활용해 첫 번째 위치와 마지막 위치를 각각 찾거나 라이브러리 활용

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array,x,x)

if count == 0: # 값이 x인 원소가 존재하지 않는다면
    print(-1)
else: # 값이 x인 원소가 존재한다면
    print(count)