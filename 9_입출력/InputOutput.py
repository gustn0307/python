# 표준 입출력(sep, end, sys.stdout, sys.stderr, ljust(), rjust(), zfill(), 표준입력, 다양한 출력 포맷, 파일입출력, 퀴즈)

print("파이썬", "자바",sep=",") # default는 띄어쓰기인데 sep를 쓰면 구분문자를 지정한 별도의 문자로 대체 가능
print("파이썬", "자바", "자바스크립트",sep=" vs ") 

print("파이썬", "자바", sep=",", end="?") # default는 줄바꿈인데 end를 사용하면 지정문자로 대체가능
print("무엇이 더 재밌을까요?")

import sys
print("파이썬", "자바", file=sys.stdout) # 표준 출력
print("파이썬", "자바", file=sys.stderr) # 표준 에러(에러메시지 로깅 시 사용)

# 시험 성적(출력 서식)
scores={"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # items()를 사용하면 키와 밸류로 나오는데 이를 각각 subject와 score로 튜플로 보내줌
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4), sep=":") # ljust(n) => n 만큼의 공간안에서 왼쪽 정렬, 문자열에 사용가능

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호: "+str(num).zfill(3)) # zfill(n) => n 만큼의 공간에서 남는 공간을 0으로 채움, 문자열에만 사용가능

# 표준 입력
# answer=input("아무 값이나 입력하세요: ") 
# print(type(answer)) # 숫자를 입력해도, 문자열을 입력해도 input으로 받은 값은 문자열로 저장
# print("입력하신 값은 "+ answer + "입니다.") 

## 다양한 출력포맷 

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
print("{0: >10}".format(-500))

# 양수일 때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _ 로 채움
print("{0:*<+10}".format(500))

# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하고, 빈자리는 ^ 로 채워주고, 왼쪽 정렬하고, 총 30자리 공간확보
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3)) # 소수점 3째 자리에서 반올림(2째 자리까지 출력)

# 파일입출력
# score_file=open("9_입출력/score.txt","w",encoding="utf8") # w는 쓰기 용도, 덮어쓰기(write)
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close() # open() 했으면 close() 해주어야함

# score_file=open("9_입출력/score.txt","a",encoding="utf8") # a는 추가, 이어쓰기(append)
# score_file.write("과학: 80") # write 함수는 자동 줄바꿈이 안되므로 직접 줄바꿈 해줘야함
# score_file.write("\n코딩: 100")
# score_file.close()

# scroe_file=open("9_입출력/score.txt", "r",encoding="utf8")
# print(scroe_file.read()) # 전부 읽기
# scroe_file.close()

# scroe_file=open("9_입출력/score.txt", "r",encoding="utf8")
# print(scroe_file.readline(),end="") # 한 줄 읽고 커서를 다음 줄로 이동
# print(scroe_file.readline(),end="") # print는 자동 줄바꿈 되므로 end로 줄바꿈 없애기
# print(scroe_file.readline(),end="") 
# print(scroe_file.readline(),end="") 
# scroe_file.close()

# 몇 줄인지 모를 때 1
# scroe_file=open("9_입출력/score.txt", "r",encoding="utf8") 
# while True:
#     line=scroe_file.readline()
#     if not line:
#         break
#     print(line,end="")
# scroe_file.close

# 몇 줄인지 모를 때 2
# scroe_file=open("9_입출력/score.txt", "r",encoding="utf8")
# lines=scroe_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line,end="")
# scroe_file.close()

# pickle => 프로그램에서 사용하고 있는 데이터를 파일 형태로 저장하고 불러와서 사용가능하도록 해주는 라이브러리
import pickle
# profile_file=open("9_입출력/profile.pickle", "wb") # w는 쓰기, b는 binary 파일, pickle을 쓰려면 항상 b를 적용해야 함, 인코딩은 필요없음
# profile={"이름":"박명수","나이":30,"취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
# profile_file.close()

# profile_file=open("9_입출력/profile.pickle", "rb")
# profile=pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with문 => 파일입출력을 더 간단하게 할 수 있다.
# import pickle
# with open("9_입출력/profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file)) # close() 필요없이 with문 나오면서 자동으로 종료됨

# with open("9_입출력/study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("9_입출력/study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 퀴즈
"""
매주 1회 작성해야 하는 보고서

양식)
- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오
조건) 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다
"""
# 내 답안
for i in range(1,51):
    report_file=open("9_입출력/{0}주차.txt".format(i),"w",encoding="utf8")
    report_file.write("- {} 주차 주간보고 -".format(i))
    report_file.write("\n부서 : ")
    report_file.write("\n이름 : ")
    report_file.write("\n업무 요약 : ")
report_file.close()

for i in range(1,51):   
    with open("9_입출력/{0}주차.txt".format(i),"r", encoding="utf8") as report_file:
        print(report_file.read())

# 나도코딩 답안
for i in range(1,51):
    with open(str(i)+"주차.txt","w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")