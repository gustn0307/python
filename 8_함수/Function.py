# 함수(함수 생성, 호출, 함수 기본값, 키워드값을 이용한 함수호출, 지역변수와 전역변수, 퀴즈)

def open_account():  # 계좌 생성
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance+money


balance = 0  # 잔액
balance = deposit(balance, 1000)
print(balance)


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance


balance = 0  # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    # 수수료와 잔액에서 출금액과 수수료를 뺀 금액을 튜플 형식으로 반환
    return commission, balance-money-commission


balance = 0  # 잔액
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다".format(commission, balance))

# 함수 기본값


def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))  # 역슬래쉬(\) 하고 다음 줄에 쓰면 같은 줄에 있는걸로 인식


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업(나이, 언어를 기본값으로)

# 기본값 있는 인자가 기본값 없는 인자 앞에 있으면 안됨(호출 시 섞여 있으면 어떤 인자인지 구분이 안되므로)
# 참고: https://velog.io/@minho/SyntaxError-non-default-argument-follows-default-argument
def profile(name, age=17, main_lang="파이썬"): 
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
profile("정형돈", 18) # 기본값이 있어도 인자 전달해서 변경 가능ㄴ
profile("박명수", "자바") #기본값이 있는 인자가 2개 이상일 때는 정의된 인자 순서대로 넣어야함
profile("하하", main_lang="자바") # 기본값이 있는 인자가 2개 이상일 때는 뒤에 있는 값만 지정해서 바꾸고 싶을 때는 키워드값을 이용해 변경

# 키워드 값을 이용한 함수 호출
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석",20,"파이썬")
profile(main_lang="java",age=25,name="김태호") # 함수 호출 시에 매개변수의 값을 키워드를 이용해 호출하면 순서 바꿔서 넣어 줄 수 있다

# 가변인자를 이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # print문 안에 end를 사용하면 끝에 줄바꿈을 하지않고 지정한 문자로 끝남
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#") 
profile("김태호", 25, "코틀린", "스위프트", "", "", "") # 인자의 개수가 다르거나 추가될 수 있으므로 가변인자가 필요

def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # print문 안에 end를 사용하면 끝에 줄바꿈을 하지않고 지정한 문자로 끝남
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#", "자바스크립트") 
profile("김태호", 25, "코틀린", "스위프트", "", "", "") 

# 지역변수와 전역변수
gun=10 # 전역변수
def checkPoint(soldiers): # 경계근무
    gun=20 # 지역변수
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) # 전역변수 gun
checkPoint(2) # 2명이 경계근무 나감, 지역 변수 gun이 출력
print("남은 총: {0}".format(gun)) # 전역변수 gun

gun=10
def checkPoint(soldiers): # 경계근무
    global gun # 전역변수 gun을 함수 내에서 사용하겠다는 의미
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) # 전역변수 gun
checkPoint(2) # 2명이 경계근무 나감, 전역 변수 gun이 출력
print("남은 총: {0}".format(gun)) # 전역변수 gun

gun=10
def checkPoint_ret(gun, soldiers): # 경계근무
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun)) # 전역변수 gun
gun=checkPoint_ret(gun, 2) # 2명이 경계근무 나감, 전역 변수 gun이 출력
print("남은 총: {0}".format(gun)) # 전역변수 gun

# 퀴즈
"""
표준 체중을 구하는 프로그램을 작성, 표준체중: 각 개인의 키에 적당한 체중

    (성별에 따른 공식)
    남자: 키(m) * 키(m) * 22
    여자: 키(m) * 키(m) * 22

    조건1: 표준 체중은 별도의 함수 내에서 계산
        * 함수명: std_weight
        * 전달값: 키(height), 성별(gender)
    조건2: 표준 체중은 소수점 둘째 자리까지 표시

    (출력예제)
    키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""
# 내 답안
def std_Weight(height, gender):
    if gender=="남자":
        weight=(height/100)*(height/100)*22
    elif gender=="여자":
        weight=(height/100)*(height/100)*21
    else:
        print("성별을 제대로 입력해주세요")
    print("키 {} {}의 표준 체중은 {}입니다".format(height, gender, round(weight,2)))
    #round(실수, n) => n번째 자리수까지 표시(n+1 자리에서 반올림)
    #round(정수, n) => n을 음수로 사용하면 반올림 사용가능

std_Weight(175, "남자")
std_Weight(168, "여자")

# 나도코딩 답안
def std_Weight(height, gender): # 키는 m 단위(실수), 성별 "남자"/"여자"
    if gender=="남자":
        return height * height * 22
    else:
        return height * height * 21

height=175 # cm단위
gender="남자"
weight=round(std_Weight(height/100, gender), 2)
print("키 {0} {1}의 표준 체중은 {2}입니다".format(height, gender, round(weight,2)))








