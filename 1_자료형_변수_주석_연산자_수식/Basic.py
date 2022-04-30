# 자료형(정수, 실수, 계산식, 문자열, Boolean), 변수, 주석, 연산자, 수식 
# 정수, 실수, 계산식
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자열
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*5)

#boolean 
print(5 > 10)
print(5 < 10)
print(True)  # 첫 글자 대문자로 해야 한다
print(False)
print(not True)
print(not(5 > 10))

#애완동물 소개(변수)
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3  # bool 변수

print("우리집" + animal + "의 이름은 " + name + "에요")
# +를 사용하는 문자열로 쓰이기 위해서는 형변환 해주어야 함
print(name+"는 " + str(age)+"살이며 "+hobby+"을 아주 좋아해요")
# ,를 사용하는 문자열로 쓰이기 위해서는 형변환 안해도 되고 공백이 한칸 들어감
print(name, "는 ", age, "살이며 ", hobby, "을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))

#주석
#으로 시작하면 한줄 주석
'''
작은 따옴표 세 개로 시작하면
여러 줄을 주석 처리 할 수 있다
'''

#퀴즈
'''
변수명 : station
변수값 : 사당, 신도림, 인천공항 순서대로 입력
출력 문장: **행 열차가 들어오고 있습니다.
'''
station = "사당"
print(station+"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")

#연산자
print(1+1)  # 2
print(3-2)  # 1
print(5*2)  # 10
print(6/2)  # 1.5

print(2**3)  # 2^3 = 8
print(5 % 3)  # 나머지 구하기 => 2
print(10 % 3)  # 1
print(5//3)  # 몫 구하기 => 1
print(10//3)  # 3

print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True

print(3 == 3)  # True
print(4 == 2)  # False
print(3+4 == 7)  # True

print(1 != 3)  # True
print(not(1 != 3))  # False

print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5>4>3) # True
print(5 > 4 > 7) #False

#수식
print(2+3*4) # 14
print((2+3)*4) # 20
num = 2+3*4 # 14
print(num)

num+=2 # 16
print(num)

num*=2 # 32
print(num)

num//=2 # 16
print(num)

num/=2 # 8.0
print(num)

num-=2 # 6.0
print(num)

num%=2 # 0
print(0)



