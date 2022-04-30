# 자료구조의 변경
menu={"커피", "우유", "주스"} # set(집합) => 중괄호
print(menu, type(menu))

menu=list(menu)
print(menu, type(menu)) # list => 대괄호

menu=tuple(menu)
print(menu, type(menu)) # tuple => 소괄호


menu=set(menu)
print(menu, type(menu)) # set(집합) => 중괄호

# 퀴즈
"""
댓글 이벤트 추첨으로 1명은 치킨, 3명은 커피쿠폰
조건1) 편의상 댓글은 20명이 작성, 아이디는 1 ~ 20 이라고 가정
조건2) 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3) random 모듈의 shuffle 과 sample을 활용

출력예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

활용예제)
from random import *
lst=[1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
"""
# 내 답안
from random import *
id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : "+ str(sample(id,1))) # 처음 뽑은 한 명과 두 번째에 뽑은 3명이 겹칠 수 있기 때문에 한번에 4명을 뽑아야 함
print("커피 당첨자 : "+ str(sample(id,3)))
print("-- 축하합니다 --")

# 나도코딩 답안
from random import *
users=range(1,21) # 1부터 21 직전까지(1 이상 21 미만) 숫자를 생성, 큰 수도 생성 가능 
print(type(users)) # 타입이 range이기 때문에 list 관련 함수를 사용할 수 없기 때문에 
users = list(users) # list 로 형변환

shuffle(users)
print(users)

winners=sample(users,4) # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) # 처음 뽑은 한 명과 두 번째에 뽑은 3명이 겹칠 수 있기 때문에 한번에 4명을 뽑아야 함
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")


