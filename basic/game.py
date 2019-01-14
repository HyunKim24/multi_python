############################################################################
# 자료형, 조건문, 반복문만 이용하여
# 게임을 구현한다 
# => 함수지향적X 객체지향적X 오직 절차적프로그램 사용
############################################################################
# 숫자 맞추기 게임, 0~99까지 나오는 AI의 랜덤값을 찾는
# 머드게임(텍스트로 주고 받으면서 숫자를 맞춘다)
############################################################################
'''
step 1
"게임의 제목을 입력하세요" 프럼프트 출력
"적당한 제목(영문)" 입력하면 다음 단계 진행

step 2
===========================
=     게임제목(중앙정렬)   = 
=     v 1.0.0             =
===========================
이렇게 출력

step 3
게이머의 이름을 입력하세요?
-> 이름을 넣지 않으면 "뭐라뭐라 하고" 다시 입력

step 4
AI의 숫자를 입력하세요?
-> 숫자를 안넣으면 "경고 메세지" 다시 입력
-> 숫자가 아닌 값을 넣으면 "경고 메세지" 다시 입력
-> 0보다 작거나 100이상을 입력해도 "경고 메세지" 다시 입력
-> 정상 범위에 정수값을 입력하면 다음  단계 진행

step 5
AI는 숫자를 하나 생성한다.(랜덤) -> 1회만 생성되어야함
즉 게임 한번이 종료될때가지 유지되어야 한다

step 6
판단 
1) 입력값이 정답보다 작으면  => 작다고 코멘트
2) 입력값이 정답보다 크면    => 크다고 코멘트
3) 입력값이 정답과 동일하면  => 축하메시지를 뿌려준다.

step 7
결과 표시
총 시도 횟수 표시
점수 = (10-총시도횟수)*10 를 표시
다시 게임을 하시겠습니까?
YES(대소문자 구분 안함) => 다시 게임 시작(step 4부터 진행)
No(대소문자 구분 안함) => 게임 종료 => 프로그램 종료
아무것도 안넣고 엔터 => 경고 메시지
입력값이 틀려도 경고

'''