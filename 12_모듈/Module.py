# 모듈 (모듈 import 방식들, 패키지, __all__, 모듈 직접 실행, 패키지와 모듈 위치, pip install, 내장 함수, 외장 함수, 퀴즈)
# => 자동차의 부품과 같은 역할, 파이썬에서는 함수의 정의, 클래스 등의 파이썬 문자를 담고 있는 파일, 확장자가 .py임
# 모듈은 같은 경로에 있거나 파이썬 라이브러리 폴더 안에 있어야 사용가능

import theater_module
theater_module.price(3) # 3명이 영화보러 갔을 때
theater_module.price_morning(4) # 4명이 조조 영화보러 갔을 때
theater_module.price_soldier(5) # 군인 5명이 영화보러 갔을 때

import theater_module as mv # as 뒤에는 별명을 만든다고 생각하면 된다.
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # theater_module 필요없이 모듈 안의 모든 것을 사용하겠다
# from random import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 사용할 함수만 import할 수 있다.
price(3)
price_morning(4)
#price_soldier(5) # 에러발생

from theater_module import price_soldier as price # 한 개만 사용하므로 별명으로 짧게 만들어서 사용
price(5) # price_soldier를 price라고 별명을 만들어서 사용


## 패키지
# => 모듈들의 집합, ex) 패키지 여행(태국, 베트남)
import travel.thailand # import 할 때 맨 뒷부분은 모듈이나 패키지만 가능 ex)여기서는 thailand(모듈)
#import travel.thailand.ThailandPackage # class나 함수는 직접 import 불가
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from A import B 구문에서는 B에 클래스나 함수가 올 수 있다
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()


## __all__
from random import *
from travel import *
trip_to = vietnam.VietnamPackage() # vietnam이 정의 되지 않았다고 에러뜸, __init__.py에서 __all__ 설정을 해주면 사용 가능
trip_to = thailand.ThailandPackage() # __init__.py에서 __all__ 설정을 해주지 않으면 사용불가
trip_to.detail()


# 모듈 직접 실행
#if __name__ == "__main__": 을 사용해서 모듈 내부에서 실행하는 것인지 외부에서 실행하는 것인지 알 수 있다


# 패키지, 모듈 위치
import inspect
import random
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand)) # 패키지를 C:\Python39\lib\ 에 두면 다른 프로젝트에서도 사용 가능


## pip install => 이미 만들어진 패키지를 설치하는 방법(라이브러리 설치)
# => 구글에 pypi를 검색해서 https://pypi.org/ 에 들어가고 원하는 패키지 선택 후에 pip install beautifulsoup4 와 같은
# pip 명령어를 콘솔창에 입력해서 설치 후에 사용하면 된다
# 또한 콘솔창에 pip list를 입력하면 현재 설치되어 있는 패키지 목록을 볼 수 있다
# 콘솔창에 pip show 패키지명 을 입력하면 해당 패키지명을 가진 패키지의 정보를 볼 수 있다
# pip install --upgrade 패키지명 을 입력하면 해당 패키지명을 가진 패키지를 최신 버전으로 업데이트 할 수 있다
# pip uninstall 패키지명 을 입력하면 해당 패키지명을 가진 패키지를 삭제할 수 있다

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


## 내장 함수
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요? ")
print("{}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장함수
print(dir()) # random 추가
import pickle
print(dir()) # pickle 추가

print(dir(random)) # random 모듈 객체 내에서 사용가능한 변수와 함수들 표시

lst = [1,2,3]
print(dir(lst)) # lst list 객체 내에서 사용가능한 변수와 함수들 표시

name = "Jim"
print(dir(name)) # name 문자열 객체 내에서 사용가능한 변수와 함수들 표시

# list of python builtins 라고 검색해서 https://docs.python.org/ko/3/library/functions.html 에 접속하면
# 파이썬에서 사용할 수 있는 여러 내장 함수들의 정보들이 나옴


## 외장 함수 => 사용자가 직접 import 해서 사용해야 하는 함수들
# list of python modules 라고 검색해서 https://docs.python.org/3/py-modindex.html 에 접속하면
# 파이썬에서 사용할 수 있는 여러 외장 함수들의 정보들이 나옴
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 cmd에서 dir 명령어, 리눅스에서 ls 명령어)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시

folder = "simple_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
else:
    os.mkdir(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir()) # listdir(path) : path에 의해 주어진 디렉터리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 년-월-일 시:분:초

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 ", today+td) # 오늘 부터 100일 후


## 퀴즈
"""
프로젝트 내에 나만의 시그니쳐를 남기는 모듈을 만들기

조건) 모듈 파일명은 byme.py 로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtybe.com
이메일 : nadocoding@gmail.com
"""
# 내 답안
import byme
byme.sign()

# 나도코딩 답안
import byme
byme.sign()