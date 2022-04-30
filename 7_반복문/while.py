# while문

customer="토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
    index-=1
    if index == 0:
        print("커피는 폐기 처분되었습니다.")

# 무한루프 => ctrl + c 를 누르면 멈춤
# customer="아이언맨"
# index = 1
# while True:
#      print("{0}, 커피가 준비되었습니다. 호출 {1}번".format(customer,index))
#      index += 1

customer="토르"
person="Unknown"

while person!=customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person=input("이름이 어떻게 되세요? ")
    print()
print("{0}님, 맛있게 드세요~".format(customer))

