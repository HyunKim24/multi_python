# 모듈 가져오기 및 사용하기
# 기본형
# 파이썬으로 만들어진 파일 => *.py <= 모듈
# 파이썬 코드들이 들어있는 폴더 => a>b>*.py <= a나, b를 패키지라고 부름
# 모듈안에 존재하는 변수, 함수, 클래스 가져올 수 있다
# 왜 가져오는가? => 재사용성!! => 생산성 => 수익창출, 분석 등등
########################################################################
PI = 3.14
# if __name__ == '__main__': 
#     # 내가 주도적으로 구동
#     # 모듈의 테스트 코드를 위치시켜라
#     print(__name__)
# 파이값을 가져다가 출력하시오
from p15_mod import PI
print('PI=%s'%PI)
# 모듈을 가져오면 해당 모듈이 수행된다.
# => 원하지 않았지만, 코드가 수행되서 로그가 출력된다든지
# => 다른관점에서 보면 오동작을 한다.
# 단, p15_mod를 직접 구동하면 다 수행하고, 다른 모듈이 
# import 하면 구동 안되게 하고 싶다
# => if __name__ == '__main__': 직접구동시 코드를 위치


# PersonEx3를 사용하고 싶다. 전혀 다른 모듈에서 
# from  모듈명 import
# from p15_mod import PersonEx3