# 예외처리(예외처리, 에러 발생시키기, 사용자 정의 예외처리, finally, 퀴즈) 
# => 프로그램이 강제 종료되는 것을 막음으로 프로그램의 완성도를 높일 수 있다

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
# except ValueError:  # try문을 실행하다가 ValueError 에러 발생하면 except문 실행 ex)문자열 입력
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # try문을 실행하다가 ZeroDivisionError 에러 발생하면 except문 실행
#     print(err)
# except Exception as err: # try문을 실행하다가 나머지 에러 발생하면 except문 실행하고 에러 메시지 출력
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


## 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # 에러 발생
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


## 사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg=msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력 값 : {}, {}".format(num1, num2)) # 인자로 준 문자열을 BigNumberError 에 msg로 전달
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
#     print(err) # BigNumberError에 전달된 문자열 인자를 __str__()에서 반환하여 출력


## finally : 예외처리 구문에서 정상적으로 수행하던 에러가 발생하던 마지막에 무조건 실행하는 구문
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg=msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력 값 : {}, {}".format(num1, num2)) # 인자로 준 문자열을 BigNumberError 에 msg로 전달
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
#     print(err) # BigNumberError에 전달된 문자열 인자를 __str__()에서 반환하여 출력
# finally: # except 문에서 정의하지 않은 에러가 발생하더라도 실행됨
#     print("계산기를 이용해 주셔서 감사합니다.")


## 퀴즈
"""
자동 주문 시스템을 코드를 활용해 예외처리 구문을 추가

조건1) 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건2) 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

[코드]
chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
while(True):
    print("[남은 치킨 : {}]".format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {}] {} 마리 주문이 완료되었습니다".format(waiting, order))
        waiting +=1
        chicken -= order
"""
# 내 답안
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg=msg

    def __str__(self):
        return self.msg
        
try: # try문을 while문 안에 넣어야 오류 발생해도 다시 주문 물어봄 아니면 그냥 에러 메시지 뜨고 종료됨
    chicken = 10
    waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
    while(True):
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1:
            raise ValueError
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.") # 여기 넣으면 order와 chicken이 같은 경우를 커버하지 못함
        else:
            print("[대기번호 {}] {} 마리 주문이 완료되었습니다".format(waiting, order))
            waiting +=1
            chicken -= order
except ValueError:
    print("잘못된 값을 입력하였습니다")
except SoldOutError as err:
    print(err)

# 나도코딩 답안
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))

#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {}] {} 마리 주문이 완료되었습니다".format(waiting, order))
#             waiting +=1
#             chicken -= order
        
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다")
#     except SoldOutError:
#         print(("재고가 소진되어 더 이상 주문을 받지 않습니다."))
#         break