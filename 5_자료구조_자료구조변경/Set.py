# 세트(set) => 집합(교집합, 합집합, 차집합), 중복 안되고 순서가 없음


my_set={1,2,3,3,3}
print(my_set) # 중복이 안되므로 1, 2, 3 만 출력됨

# set의 정의
java={"유재석", "김태호", "양세형"}
python=set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 또는 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 하지 못하는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)

