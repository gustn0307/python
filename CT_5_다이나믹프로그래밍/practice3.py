## 효율적인 화폐 구성
# N가지 종류의 화폐가 있고 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록, 이때 각 종류의 화폐는 몇 개라도 사용 가능
# ex) 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수
# M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램 작성

## 내 답안 => 최소한의 개수를 구하는 법이 없음
# n, m = map(int, input().split())  # 화폐 종류(N), 만들려는 액수(M) 입력 받기
# array = []
# for i in range(n):  # 화폐의 가치들 입력 받기
#     array.append(int(input()))

# result = 0
# num = m
# array.sort(reverse=True)
# while num != 0:
#     for j in range(n):
#         if m < array[j]:
#             result = -1
#             num = 0
#             break

#         if num % array[j] == 0:
#             num -= array[j]
#             result += 1
#             break
#     if num == 0:
#         break

# print(result)

## 동빈나 답안
## a[i] = 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식: 각 화폐 단위인 k를 하나씩 확인하며
# a[i-k]를 만드는 방법이 존재하는 경우 a[i] = min(a[i], a[i-k]+1)
# a[i-k]를 만드는 방법이 존재하지 않는 경우, a[i] = INF

n, m = map(int, input().split())  # 화폐 종류(N), 만들려는 액수(M) 입력 받기
array = []
for i in range(n):  # 화폐의 가치들 입력 받기
    array.append(int(input()))

# 화폐의 단위 범위가 1 ~ 10000 이므로 10001은 INF(무한)의 의미로 사용해서 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 (바텀업)
d[0] = 0
for i in range(n): # i는 각각의 화폐의 종류
    for j in range(array[i], m+1): # j는 화페의 금액
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])