# 주소 : ~/users/...
# ~/users/login, ~/users/logout, ~/users/signup
# app라는 실제가 바뀌면(블루프린트로) 주소의 시작방식이 변경
from flask_ex.service.controller import bp_users as app
from flask_ex.service.model import db_session
from flask_ex.service.model import dao
from flask_ex.service.model.member import Member


# 세션 없이 갈 수 있는 유일한 페이지(가정)
# ~/users/login
@app.route('/login')
def login():
    print('로그인',db_session.login_sql('m','1'))
    return "로그인 홈"

#  ~/users/logout
@app.route('/logout')
def logout():
    return "로그아웃 홈"

# ~/users/signup
# 회원 가입 : insert
@app.route('/signup')
def signup():
    # ORM을 이용한 회원가입
    # 객체 1개 = row 1개와 1대 1로 대응한다.
    newUser = Member('multi','1234')
    dao.add(newUser)
    dao.commit()
    return "회원가입 홈"

# 회원 정보 수정 : update ~
@app.route('/update')
def update():
    user = dao.query(Member).filter_by(uid='multi',upw='1234').first()
    # 비번 변경
    user.upw = '12345'
    dao.commit()
    return 'update'

# 회원 로그인 : select ~
@app.route('/select')
def select():
    user = dao.query(Member).filter_by(uid='multi',upw='12345').first()
    if user: # 회원이면
        print(user)
    else:
        print(user,'회원아님')
    return 'select' 

# 회원 삭제 : delete ~
@app.route('/delete')
def delete():
    user = dao.query(Member).filter_by(id= '2').first()
    if user:
        # 삭제
        dao.delete(user)
        dao.commit()
        # print(user)
    return 'delete'
