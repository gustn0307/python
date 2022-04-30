# for문, 한 줄 for문
# 반복되는 동일한 작업을 수행 시 사용

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

starbucks=["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))

# 한 줄 for문
# 출석번호가 1,2,3,4가 있는데 앞에 100을 붙이기로함 -> 101, 102, 103, 104
students=[1,2,3,4]
print(students)
students=[i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students=["Iron man", "Thor", "Groot"]
print(students)
students=[len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students=["Iron man", "Thor", "Groot"]
print(students)
students=[i.upper() for i in students]
print(students)

# 퀴즈
"""
택시기사가 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성
조건1) 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해짐
조건2) 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 함

출력문예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 2번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
"""
# 내 답안
from random import *
cnt=0
for i in range(1,51):
    ride=" "
    time=randint(5,50)
    if 5<=time<=15:
        ride="O"
        cnt+=1
    print("[{0}] {1}번째 손님 (소요시간: {2}분)".format(ride,i,time))
print("총 탑승 승객: {0} 분".format(cnt))

# 나도코딩 답안
from random import *
cnt=0 # 총 탑승 승객 수
for i in range(1,51): # 1 ~ 50 의 승객 수
    time = randrange(5,51) # 5분 ~ 50분 랜덤 소요시간
    if 5 <= time <= 15: # 매칭성공(5분 ~ 15분 이내의 손님), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 : {0}".format(cnt))




