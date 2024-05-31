from flask import Flask, jsonify, request, make_response, session
from flask_login import LoginManager
from flask_cors import CORS
from web_view import web
from web_control.user_mgmt import User


app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'fairy_tail' # 세션 정보를 할당받을 수 있게 하기 위한 키

app.register_blueprint(web.web_test, url_prefix='/home')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong' # 세션 생성 강도

@login_manager.user_loader # db에서 로그인한 유저 정보 로드
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler # 로그인이 안 된 유저가 접속할 경우 
def unauthorized():
    return make_response(jsonify(success=False), 401)

@app.before_request
def app_before_request():
    if 'client_id' not in session: # 모든 요청에 대한 세션 정보 할당
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
