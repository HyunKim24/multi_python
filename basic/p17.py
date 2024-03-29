####################################################################
# 패키지 생성 및 가져오기, 모듈 가져오기
####################################################################
from p16 import PI
# 패키지는 같은 계열이나 의미를 가진 모듈들을 모아둔 디렉토리(폴더)
# 하위호환(3.3 이하)을 위해서 패키지를 만들면 반드시(생략가능)
# __init__.py을 생성해 둔다. 이 파일의 의미는 패키지 자체를 의미
# a 밑에 b 밑에 mode.py 안에 sum 함수를 가져다가 내것처럼 사용한다.
from a.b.mod import sum
from a.b import sum2
from a.make import sum3
# 함수, 클래스, 변수 등 다 import 할 수 있고
# 다 별칭을 줄 수 있다.
from a import sum4 as s4

print(sum(1,2))
print(sum2(1,2))
print(sum3(1,2))
print(s4(1,2))
# as => 별칭, 이름이 길거나, 대체 이름(별칭)으로 사용할 경우
import a.b.mod as m
print(m.sum(10,11))
import a.b as m2
print(m2.sum2(10,11))

