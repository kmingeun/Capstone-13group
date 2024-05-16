1. mysql에서 fairy_tail 데이터베이스 생성

    CREATE DATABASE fairy_tail

2. db_model의 schema.sql 파일 복사하여 db에 테이블 생성

3. db_model의 mysql.py 에서 user와 passwd를 자신의 DB에 맞게 수정

4. web_test.py 실행하여 플라스크 서버 실행

5. 주소창에 localhost:8080/home 입력하여 기본 홈 페이지 접속

// 회원 가입 기능은 구현하지 안음
로그인을 하려면 web_view의 web.py에서 check 함수에서 주석처리를 지우고, 아래를 주석 처리해야 함

user = User.create(request.form['web_id'], request.form['password'], 'A') => 주석처리 지우기
user = User.find(request.form['web_id']) -> 주석 처리

로그인화면에서 원하는 ID와 비밀번호를 입력하고 로그인하면 DB에 저장됨
이후 다시 위에서 했던 주석처리 부분을 원래대로 돌려두면 
해당 ID와 비밀번호로 로그인 시 DB에서 유저 정보를 찾아 로그인이 됨
해당 ID와 비밀번호가 아닐경우 등록되지 않은 유저라는 메세지를 남기며 로그인이 되지 않음