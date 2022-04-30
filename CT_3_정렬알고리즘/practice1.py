## 두 배열의 원소 교체
## N개의 원소로 구성된 두 개의 배열 A와 B가 있고 배열의 원소는 모두 자연수
## 최대 K번의 바꿔치기 연산을 수행할 수 있음(배열 A와 배열 B의 원소를 바꾸는 것)
## 배열 A의 모든 원소의 합이 최대가 되도록 하는 것
## N, K, 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력

## 내 답안
n, k = map(int,input().split())
a = map(int, input().split())
b = map(int, input().split())

sa=sorted(a)
sb=sorted(b) # b는 내림차순 정렬하면 인덱스 접근하기 더 편함
result=0

for j in range(n):
    if sa[j] < sb[n-1-j]: # b의 원소가 a의 원소보다 작을수도 있는 경우를 생각해야함
        sa[j], sb[n-1-j] = sb[n-1-j], sa[j] 
    else: # b의 원소가 a의 원소보다 작을수도 있는 경우 break
        break

    if j == k-1:
        break

for i in range(n): # 그냥 sum(sa)하면 됨
    result+=sa[i]

print(result)

## 동빈나 답안
## 핵심 아이디어: 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체
## 가장 먼저 배열 A와 B가 주어지면 A에 대해 오름차순 정렬하고, B에 대해 내림차순 정렬
## 이후에 두 배열의 원소를 첫 번째 인덱스 부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때만 교체를 수행
## 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용

n, k = map(int,input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기

a.sort() # 배열 A는 오름차순 정렬
b.sort(reverse=True) # 배열 B는 내림차순 정렬

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력