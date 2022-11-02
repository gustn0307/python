## 문자열 재정렬
# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어지고 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
# EX) K1KA5B7 => ABKK13 을 출력

## 내 답안
#input_str="K1KA5B7"
input_str=input()
trans=[] # 문자를 숫자로 변환
result=[] # sort된 문자와 숫자 합을 담는 list
sum=0

for i in range(len(input_str)):
    if input_str[i].isupper():
        trans.append(ord(input_str[i]))
    else:
        sum+=int(input_str[i])

trans.sort()

for i in range(len(trans)):
    if 65 <= trans[i] <= 90 :
        result.append(chr(trans[i])) 
    else:
        break

if sum != 0: # 숫자가 존재하지 않는 경우도 생각
    result.append(sum)

for i in range(len(result)):
    print(result[i], end='')
print()

## 내 답안 ver2

input_str=input()
result=[] # sort된 문자와 숫자 합을 담는 list
sum=0

for i in range(len(input_str)):
    if input_str[i].isupper():
        result.append(input_str[i])
    else:
        sum+=int(input_str[i])

result.sort()

if sum != 0: # 숫자가 존재하지 않는 경우도 생각
    result.append(str(sum)) # 문자열로 변환해서 추가(join() 메소드 사용하기 위해)

print("".join(result))

## 동빈나 답안
# 문자열이 입력되었을 때 문자를 하나씩 확인하고 숫자인 경우 따로 합계를 계산, 알파벳인 경우 별도의 리스트에 저장
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력

data = input()
result=[]
value=0

# 문자를 하나씩 확인하며
for x in data:
    if x.isalpha(): # 알파벳인 경우 결과 리스트에 삽입, isalpha() 메소드 사용
        result.append(x)
    else: # 숫자는 따로 더하기
        value += int(x)

# 알파벳을 오름차순으로 정렬( 리스트 안의 원소가 문자여도 sort 가능 )
result.sort() 

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result)) # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
