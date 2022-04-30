# 사전(Dictionary) => get, key in 사전, 

# Key와 Value의 쌍을 가지는 집합, Key는 중복 불가
# ex) 목욕탕 키와 사물함
cabinet={3:"유재석", 100:"김태호"} # 키(key) : 밸류(value)
print(cabinet)
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # [] 사용시 존재하지 않는 키값 입력시 에러, 프로그램 종료
print(cabinet.get(5)) # get은 존재하지 않는 키 값 입력 시 None 반환
print(cabinet.get(5, "사용 가능")) # 존재하지 않는 키 값 입력 시 get의 두 번째 인자(사용 가능) 반환

print(3 in cabinet) # 3 이라는 key가 cabinet에 있는지 확인(True or False)
print(5 in cabinet)

cabinet={"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"]="김종국" # 갱신
cabinet["C-20"]="조세호" # 추가
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet) # 삭제

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items()) # 괄호로 (key, value) 묶어서 출력

# 목욕탕 폐점
cabinet.clear() # 모든 값 삭제
print(cabinet)
