# 문자열, 문자열 처리 함수 ( lower(), upper(), isupper(), islower(), len(), replace(), index(), find(), count() ), 
# 문자열 포맷, 탈출문자, 문자열 뒤집기

# 문자열

sentence = '나는 소년입니다'
print(sentence)
print(sentence[::-1]) # 문자열 뒤집기 https://velog.io/@dmsql698/Python-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0


sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

# 문자열 처리 함수 ( lower(), upper(), isupper(), islower(), len(), replace(), index(), find(), count() )
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # 내가 찾는 값의 위치
print(index)
index = python.index("n", index+1)  # 내가 찾은 위치 다음부터에서 찾는 값을 다시 찾음
print(index)
print(python.find("Java"))  # 내가 찾는 값이 없으면 -1 반환
# print(python,index("Java")) # 내가 찾는 값이 없으면 오류 반환하고 프로그램 종료

print(python.count("n"))  # python이라는 변수에서 n이 총 몇번 들어가있는지를 반환
print("Hello World".find("W"))  # 변수가 아닌 문자열 자체로도 가능
print("Hello World".index("W"))  # 변수가 아닌 문자열 자체로도 가능
print("Hello World".count("o"))  # 변수가 아닌 문자열 자체로도 가능

# 문자열 포맷
print("a"+"b") # 붙여서 출력됨
print("a", "b") # 띄어서 출력됨

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요" % "A")

# %s
print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))  # 괄호안에 있는 값이 순서대로 들어감

# 방법 2
print("나는 {}살 입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))  # 중괄호만 사용하면 format안의 순서대로 들어가고
# 중괄호 안에 숫자를 적으면 숫자 순서에 맞는 순서대로 들어간다
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4 (파이썬 v3.6 이상에서 사용 가능)
age = 20
color = "빨간"
# 앞에 f를 붙이고 중괄호에 변수명을 사용하면 방법 3과 동일하게 변수의 값을 사용 가능
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자
print("백문이 불여일견, \n백견이 불여일타")  # \n 줄바꿈
# 저는 "강현수"입니다. 라는 문자열을 출력하고 싶을때
print("저는 '강현수'입니다.")  # 큰 따옴표 안의 작은 따옴표는 그냥 출력가능
print('저는 "강현수"입니다.')  # 작은 따옴표 안의 큰 따옴표는 그냥 출력가능
print("저는 \"강현수\"입니다")  # \"  => 큰 따옴표 안의 큰 따옴표 출력가능
print('저는 \'강현수\'입니다')  # \'  => 작은 따옴표 안의 작은 따옴표 출력가능

# \\  => 문장내에서 역슬래쉬(\) 하나로 변환
print("C:\\Users\\Kang HyeonSu\\Desktop\\WorkSpace\\PythonWorkSpace>")

# \r  => 커서를 맨앞으로 이동 => Red Apple을 적은 다음에 \r 때문에 커서가 맨앞으로 이동되어서 "Red "가 Pine으로 덧씌여짐
print("Red Apple\rPine")

print("Redd\bApple")  # \b  => 백스페이스 (한 글자 삭제)

print("Red\tApple")  # \t  => 탭

#퀴즈
"""
사이트별로 비밀번호를 만들어주는 프로그램을 작성
예) http://naver.com
규칙1) http:// 부분은 제외 => naver.com
규칙2) 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3) 남은 글자 중에서 처음 세자리 + 글자 갯수 + 글자 내 'e'의 갯수 + "!" 로 구성
=>      nav                         5           1                   !
예) 생성된 비밀번호: nav51!
"""
# 내 답안
addr = "http://daum.net"
pw = addr[7:]  # 규칙 1
pw = pw[:pw.index(".")]  # 규칙 2
pw = pw[:3]+str(len(pw))+str(pw.count("e"))+"!"  # 규칙 3
print("생성된 비밀번호:", pw)  # dau40!

# 나도코딩 답안
url = "http://youtube.com"
my_str = url.replace("http://", "")  # 규칙 1
my_str = my_str[:my_str.index(".")]  # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
print(f"{url} 의 비밀번호는 {password} 입니다.")
