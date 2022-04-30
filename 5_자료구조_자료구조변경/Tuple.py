# 튜플(Tuple) 
# 내용 변경이나, 추가를 할 수 없음
# 속도가 list보다 빠름
# 값의 변경이 없는 목록들을 다룰 때 사용

# ex)돈까스집
menu=("돈까스", "치즈까스") # 괄호안에 쉼표로 구분
print(menu)
print(menu[0])
print(menu[1])

name="김종국"
age=20
hobby="코딩"
print(name,age, hobby)

name, age, hobby = "김종국", 20, "코딩" # 튜플로 여러 변수를 동시에 선언 가능
(name, age, hobby) = ("김종국", 20, "코딩") 
print(name, age, hobby)

