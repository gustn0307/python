## 1<= s <=20 길이의 문자열을 받아서 왼쪽부터 + 혹은 * 연산으로 만들 수 있는 가장 큰 수를 출력

## 내 답안 => 0인 경우만 생각함, 1인 경우에도 더하기가 이득
import time

result = 1
s = input()
start_time = time.time()  # 측정 시작
for i in range(len(s)-1):
    #if(int(s[i]) != 0 and int(s[i+1]) != 0 and int(s[i]) != 1 and int(s[i+1]) != 1): #  1인 경우에도 더하기가 이득이므로 조건 추가
    if(int(s[i])<=1 and int(s[i+1])<=1): # 위의 조건식을 간단하게 변경 가능
        if(i == 0):
            result = int(s[i])*int(s[i+1])
        else:
            result = result*int(s[i+1])
    else:
        if(i == 0):
            result = result+int(s[i])+int(s[i+1])-1
        else:
            result = result+int(s[i])+int(s[i+1])

print(result)

end_time = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력


## 동빈나 답안
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1인 경우(1 이하인 경우), 곱하기 보다 더하기 연산이 이득
    num = int(data[i])
    if num <= 1 or result <= 1: # 더하기 연산
        result += num
    else:
        result *= num
print(result)