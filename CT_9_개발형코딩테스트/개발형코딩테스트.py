## 개발형 코딩 테스트: 정해진 목적에 따라서 동작하는 완성된 프로그램을 개발하는 것을 요구하는 코테 유형
# 일부 기업은 해커톤을 통해 채용을 진행
#  - 해커톤(Hackathon)이란 단기간에 아이디어를 제품화하는 프로젝트 이벤트
#  - 대개 1 ~ 2일 정도 진행되며 다수의 해커톤이 대회 형식을 빌려 해커톤이 끝나면 만든 프로그램을 시연하고 발표 후 채점 진행

# 알고리즘 코딩 테스트: 요구 사항에 맞는 하나의 모듈 개발
#  - 시간 복잡도 분석
#  - 공간 복잡도 분석

# 개발형 코딩 테스트
#  - 완성도 높은 하나의 프로그램을 개발
#  - 모듈을 적절히 조합하는 능력 요구

# 개발형 코딩 테스트는 분야에 따라 상세 요구사항이 다를 수 있음
#  - 예시 1) 모바일 클라이언트 개발: 안드로이드, iOS 앱 개발
#  - 예시 2) 웹 서버 개발: 스프링(Spring), 장고(django)등의 서버 개발 프레임워크 활용
# 하지만 분야에 상관없이 꼭 알아야 하는 개념과 도구에 대해 학습할 필요가 있음
#  - 서버, 클라이언트, JSON, REST API, ...


## 서버와 클라이언트
# 클라이언트가 요청(Request)하면 서버가 응답(Response)
# 웹 클라이언트: PC, 노트북, 스마트폰 등
# 웹 서버: 워크스테이션 등


## 클라이언트(Client) = 고객
# 서버로 요청(Request)을 보내고 응답(Response)이 도착할 때까지 기다림
# 서버로부터 응답을 받은 뒤에는 서버의 응답을 화면에 출력
#  - 예시 1) 웹 브라우저: 서버로부터 받은 HTML, CSS 코드를 화면에 적절한 형태로 출력
#  - 예시 2) 게임 앱: 서버로부터 받은 경험치, 친구 귓속말 정보 등을 화면에 적절한 형태로 출력


## 서버(Server) = 서비스 제공자
# 클라이언트로부터 받은 요청(Request)을 처리해 응답(Response)을 전송
#  - 예시) 웹 서버: 로그인 요청을 받아 아이디와 비밀번호가 정확한지 검사하고 그 결과를 응답


## HTTP 개요
# HTTP(Hyper Text Transfer Protocol)는 웹상에서 데이터를 주고받기 위한 프로토콜을 의미
#  - 보통은 웹 문서(HTML 파일)를 주고받는 데 사용됨
#  - 모바일 앱 및 게임 개발 등에서 특정 형식의 데이터를 주고받는 용도로도 사용됨
# 클라이언트는 요청의 목적에 따라서 적절한 HTTP 메서드를 이용해 통신을 진행
#  - 대표적인 HTTP 메서드
#  HTTP 메서드    설명                            사용 예시
#  GET            특정한 데이터의 조회를 요청     특정 페이지 접속, 정보 검색
#  POST           특정한 데이터의 생성을 요청     회원가입, 글쓰기
#  PUT            특정한 데이터의 수정을 요청     회원 정보 수정
#  DELETE         특정한 데이터의 삭제를 요청     회원 정보 삭제


## 파이썬 웹 요청 예제: GET 방식
# import 되지 않으면 파이썬 버전이 여러 개 설치되어 있어 pip가 다른 버전에 설정 된 것이므로 오른쪽 아래의 파이썬 버전 부분을 클릭하고 
# 다른 파이썬 버전의 인터프리터를 선택해 확인해보기(https://www.inflearn.com/questions/388018)
import requests 

target = "http://google.com" 
response = requests.get(url=target)
print(response.text)


## REST의 등장 배경
# HTTP는 GET, POST, PUT, DELETE 등의 다양한 HTTP 메서드를 지원
#  - 실제로는 서버가 각메서드의 기본 설명을 따르지 않아도 프로그램을 개발 가능
#  - 하지만 저마다 다른 방식으로 개발하면 문제가 될 수 있어 기준이 되는 아키텍처가 핗요


## REST 개요
# REST(Representational State Transfer)는 각 자원(Resource)에 대하여 자원의 상태에 대한 정보를 주고받는 개발 방식을 의미
# REST의 구성요소
#  - 자원(Resource): URI를 이용
#  - 행위(Verb): HTTP 메서드를 이용
#  - 표현(Representations): 페이로드를 이용(페이로드: 전송되는 데이터)


## REST API란?
# API(Application Programming Interface): 프로그램이 상호작용하기 위한 인터페이스를 의미
# REST API: REST 아키텍쳐를 따르는 API를 의미
# REST API 호출: REST 방식을 따르고 있는 서버에 특정한 요청을 전송하는 것을 의미


## JSON
# JSON(JavaScript Object Notation): 데이터를 주고받는 데 사용하는 경량의 데이터 형식
# JSON 데이터는 키와 값의 쌍으로 이루어진 데이터 객체를 저장(파이썬의 튜플과 비슷)


## JSON 객체 사용 예제
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}

# 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent=4) # indent는 공백을 의미
print(json_data)


## JSON 객체 파일 저장 예제
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4) # file로 쓰고자 하는 사전 객체를 첫 번째 인자로, file 객체를 두 번째 인자로 넣어줌 


## REST API 연습용 서비스
# 목킹(Mocking)이란 어떠한 기능이 있는 것처럼 흉내내어 구현한 것을 의미
# 가상의 REST API 제공 서비스: https://jsonplaceholder.typicode.com/
# 사용자, 게시물 등 다양한 가상의 API를 클라이언트 쪽으로부터 호출해서 사용가능


## REST API 호출 실습해보기
# API 호출 경로: https://jsonplaceholder.typicode.com/users/1  -> URI에 원하는 데이터인 /사용자/ID 정보를 추가
# HTTP 메서드: GET
# API 호출 경로: https://jsonplaceholder.typicode.com/users/  -> URI에 원하는 데이터인 /사용자 정보를 추가
# HTTP 메서드: GET


## REST API를 호출하여 회원 정보를 처리하는 예제
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = response.json()

# 모든 사용자(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)