## 8 x 8 좌표평면 체스판에서 특정한 한 칸에 나이트가 서있고 L자 형태로만 이동할 수 있고 정원 밖으로는 나갈 수 없음
## 수평으로 두 칸 이동하고 수직으로 한칸 이동 or 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
## 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 출력

## 내 답안
loc = input()

col = loc[0:1] # 열 추출
row = loc[1:2] # 행 추출
result = 8 

if int(row) < 2:
    result -= 1
if int(row) < 3:
    result -= 2
if int(row) > 6:
    result -= 2
if int(row) > 7:
    result -= 1
if ord(col) < 98:
    result -= 1
if ord(col) < 99:
    result -= 2
if ord(col) > 102:
    result -= 2
if ord(col) > 103:
    result -= 1

print(result)

## 동빈나 답안
# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인
# 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의

# 현재 나이트의 위치 입력받기
input_data = input()

# 처음부터 행, 열을 숫자로 바꿔서 다루기 쉽게 만들기
row=int(input_data[1]) 
# ord(문자) : 아스키코드를 숫자로, chr(숫자) : 숫자를 아스키 코드로 , a ~ z: 97 ~ 122, A ~ Z : 65 ~ 90
column=int(ord(input_data[0])) - int(ord('a')) + 1 

# 나이트가 이동할 수 있는 8가지 방향 정의 => dx, dy로 나눠서 해도 되고, 아래와 같이 2차원으로 한번에 해도 됨
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1

print(result)
