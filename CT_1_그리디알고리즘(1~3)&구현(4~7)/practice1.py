## 시간계산할 때는 1초에 2천만번정도의 연산을 한다고 가정하고 풀면됨
import time
# start_time = time.time() # 측정 시작

# # 프로그램 소스코드
# end_time = time.time() # 측정 종료
# print("time:", end_time - start_time) # 수행 시간 출력

## n, k 입력 받아서 n을 k로 나누어 떨어지면 나누고 아니면 n에서 1씩 빼서 n이 1이 될 때까지 최소 연산의 수

## 내 답안 => 나눠지지 않을때는 반복문이 빼기 연산만 진행하고 다음 반복문으로 넘어가므로 동빈나 알고리즘보다 느림
# n=0
# k=0
# cnt=0
# while(True):
#     n=int(input("n? (1 <= n <= 100,000) "))
#     k=int(input("k? (2 <= k <= 100,000) "))
#     if((1 <= n <= 100,000) and (2 <= k <= 100,000)):
#         break
#     else:
#         print("범위에 맞게 입력해주세요.")
# start_time = time.time() # 측정 시작
# while n!=1:
#     if(n%k!=0):
#         n-=1
#         cnt+=1
#     else:
#         n/=k
#         cnt+=1
# print(cnt)
# end_time = time.time() # 측정 종료
# print("time:", end_time - start_time) # 수행 시간 출력

## 동빈나 답안 => 반복문이 한번 반복될 때마다 무조건 나누는 연산이 들어가서 더 빨라짐(로그 시간 복잡도)
# 그리디 알고리즘 관점에서 볼 때 1을 빼주는 것 보다 2로 나누는 것이 항상 최선이므로 나누는 연산을 진행하는 것을 선택하도록 풀이
n, k = map(int, input().split())

result = 0
start_time = time.time()  # 측정 시작
while True:
    # N이 K로 나누어 떨어지는 수가 될 때 까지 빼기
    target = (n//k)*k  # 나누는게 1 빼는 것보다 더 효율적이니까 k로 나누어 떨어지는 가장 큰 수를 구하고
    # n에서 k로 나누어 떨어지는 가장 큰 수를 빼면 1을 빼는 연산을 몇 번 해야되는지 나오니 1을 빼는 연산의 횟수를 result에 더해주고
    result += (n-target)
    n = target  # n을 k로 나누어 떨어지는 가장 큰 수인 target으로 바꿔주고
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1  # k로 나누는 연산을 진행하므로 연산 횟수를 1만큼 더해주고
    n //= k  # n을 k로 나눈 몫으로 바꿔준다(n이 나누어 떨어지는 가장 큰 수이므로 몫으로 바꿔줘도 됨)

# 마지막으로 남은 수에 대하여 1씩 빼기
# n이 1보다 큰 경우가 있을 수 있으므로 n이 1이 될 때까지 n에서 1을 빼주는 연산의 횟수를 result에 더해줌
result += (n-1)
print(result)
end_time = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력
