## 계수 정렬: 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
## 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능
## 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K 일때 최악의 경우에도 수행시간 O(N + K)를 보장

# 모든 원소 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1) # 0을 포함하므로 +1 해줌

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for _ in range(count[i]):
        print(i, end=' ')

## 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N + K)
## 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있음 ex) 데이터가 0과 굉장히 큰 수 2가지만 있는 경우
## 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용됨 ex) 성적