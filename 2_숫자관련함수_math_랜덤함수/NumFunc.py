# 숫자 관련 함수(절댓값, 제곱, 최댓값, 최솟값, 반올림, 반내림), 
# math 라이브러리(올림, 내림, 제곱근), 랜덤함수(random(), randrange(), randint())

from random import *
from math import *  # math 라이브러리 안에 있는 모든 것을 이용
print(abs(-5))  # 5, 절댓값
print(pow(4, 2))  # 4^2 = 16, 제곱
print(max(5, 12))  # 12, 최댓값
print(min(5, 12))  # 5, 최솟값
print(round(3.14))  # 3, 반올림
print(round(4.99))  # 5, 반올림

# math 라이브러리 이용
print(floor(4.99))  # 4, 내림
print(floor(ceil(3.14)))  # 4, 올림
print(sqrt(16))  # 4, 제곱근(루트)

# 랜덤 함수
print(random())  # 0.0 이상 1.0 미만의 난수(실수) 생성
print(random()*10)  # 0.0 이상 10.0 미만의 난수(실수) 생성
print(int(random()*10))  # 0 이상 10 미만의 난수(정수) 생성
print(int(random()*10)+1)  # 1 이상 10 이하의 난수(정수) 생성

print(int(random()*45)+1)  # 1 이상 45 이하의 난수 생성
print(randrange(1, 46))  # 1 이상 46 미만의 난수 생성
print(randint(1, 45))  # 1 이상 45 이하의 난수 생성

#퀴즈
"""
매월 오프라인 스터디 모임 날짜 랜덤으로 정하기
매월 일수가 다르므로 28일 까지만 최대로 정하고
1~3 일은 준비기간으로 제외
"""
print("오프라인 스터디 모임 날짜는 매월 "+str(randint(4, 28))+" 일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월", randint(4, 28), "일로 선정되었습니다.")

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")