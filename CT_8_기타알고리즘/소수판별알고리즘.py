## 소수: 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수
# 어떠한 자연수가 소수인지 아닌지 판별해야 하는 문제가 자주 출제됨

## 소수의 판별 기본적인 알고리즘
def is_prime_number(x): # 소수 판별 함수(2 이상의 자연수에 대하여)
    for i in range(2, x): # 2부터 (x-1)까지의 모든 수를 확인
        if x % i == 0: # x가 해당 수(본인이 아닌 수)로 나누어 떨어진다면
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

# 기본 알고리즘 성능 분석
# 2부터 X - 1 까지의 모든 자연수에 대해서 연산을 수행해야 함
#  - 모든 수를 하나씩 확인한다는 점에서 시간 복잡도는 O(X)

## 약수의 성질
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있음
#  - 예를 들어 16의 약수는 1, 2, 4, 8, 16
#  - 이때 2 X 8 = 16은 8 X 2 = 16과 대칭
# 따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됨
#  - 예를 들어 16이 2로 나누어 떨어진다는 것을 8로도 나누어떨어진다는 것을 의미

## 소수의 판별 개선된 알고리즘
import math

def is_prime_number(x): # 소수 판별 함수(2 이상의 자연수에 대하여)
    for i in range(2, int(math.sqrt(x) + 1)): # 2부터 x의 제곱근 까지의 모든 수를 확인
        if x % i == 0: # x가 해당 수(본인이 아닌 수)로 나누어 떨어진다면
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

# 개선된 알고리즘 성능 분석
# 2부터 X의 제곱근(소수점 이하 무시)까지의 모든 자연수에 대해서 연산을 수행해야 함
#  - 시간 복잡도는 O(N^1/2)