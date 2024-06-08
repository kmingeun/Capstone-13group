from flask import Flask, Blueprint, flash, session, render_template, request, redirect, jsonify
from flask_login import login_user, current_user, logout_user
from web_control.user_mgmt import User
from web_control.session_mgmt import WebSession
import datetime
import os

web_test = Blueprint('home', __name__)

@web_test.route('/') # 홈
def home():
    if current_user.is_authenticated: # 현재 유저가 로그인된 사용자라면 세션정보 저장
        webpage_name = WebSession.get_web_page()
        WebSession.save_session_info(current_user.user_id, session['client_id'], current_user.web_id, webpage_name)
        return render_template('after_login.html')
    else: # 현재 유저가 등록된 사용자가 아니라면   
        print('XXXXXXX')  
        return render_template('before_login.html')
       

@web_test.route('/sign-in') # 로그인
def sign_in():
    return render_template('sign-in.html')

@web_test.route('/logout') # 로그아웃
def logout():
    session.clear()
    # User.delete(current_user.user_id) # 유저 아이디 삭제
    logout_user()
    return render_template('before_login.html')

@web_test.route('/pricing')
def pricing():
    return render_template('pricing.html')

@web_test.route('/fairy_list')
def fairy_list():
    return render_template('fairy_list.html')

@web_test.route('/page_view')
def page_view():
    web_id = current_user.web_id
    return render_template('page_view.html', web_id=web_id)

@web_test.route('/before_page_view')
def before_page_view():
    return render_template('page_view.html')

@web_test.route('/dynamic_page_view')
def dynamic_page_view():
    web_id = current_user.web_id
    return render_template('dynamic_page_view.html', web_id=web_id)

@web_test.route('/create_page')
def create_page():
    return render_template('create_page.html')

@web_test.route('/check', methods=['POST']) # 유저정보 확인
def check():
    error = None
    print('set_id', request.form['web_id'])
    print('set_password', request.form['password'] )
    # user = User.create(request.form['web_id'], request.form['password'], 'A') # 유저 정보가 없다면 생성
    user = User.find(request.form['web_id'], request.form['password'])
    if user:
        login_user(user, remember=True, duration=datetime.timedelta(days=30)) # 세션 정보 할당, 30일 동안 유지
        return redirect('/home')
    else:
        error = '유저 정보가 없습니다.'
        return render_template('/sign-in.html', error=error)

@web_test.route('/api/get_user_info', methods=['GET'])
def get_user_info():
    web_id = current_user.web_id
    print(web_id)
    return jsonify({'web_id': web_id})

@web_test.route('/api/get_credit', methods=['GET'])
def get_credit():
    web_id = request.args.get('web_id')
    password = current_user.user_password
    user = User.find(web_id, password)
    if user:
        return jsonify({"credit": user.credit_data})
    else:
        return jsonify({"error": "No data"}), 404

@web_test.route('/api/charge_credit', methods=['POST'])
def charge_credit():
    password = current_user.user_password
    data = request.get_json()
    web_id = data.get('web_id')
    credits_to_add = data.get('credit') # 충전 credit 정보
    user = User.find(web_id, password) 
    current_credit = user.credit_data # 현재 credit 정보
    new_credit = current_credit + int(credits_to_add)
    User.update_credit(web_id, new_credit)

    return jsonify({'success': True})

@web_test.route('/api/get_subscription', methods=['GET'])
def get_subscription():
    web_id = request.args.get('web_id')
    password = current_user.user_password
    user = User.find(web_id, password)
    if user:
        return jsonify({"subscription": user.subscription})
    else:
        return jsonify({"error": "No data"}), 404

@web_test.route('/api/update_subscription', methods=['POST'])
def update_subscription():
    data = request.get_json()
    web_id = data.get('web_id') 
    subscription = data.get('subscription') # 클릭한 구독 정보
    User.update_subscribe(web_id, subscription)

    return jsonify({'success': True})

@web_test.route('api/image_setting/<folder_name>')
def image_setting(folder_name):
    folder_path = os.path.join(os.getcwd(), 'static', folder_name)
    
    if not os.path.exists(folder_path):
        return jsonify({"error": "Folder not found"}), 404

    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    image_files.sort()
    image_paths = [os.path.join('static', folder_name, img) for img in image_files]
    print(image_paths)

    return jsonify(image_paths=image_paths)

@web_test.route('/api/audio_setting/<folder_name>')
def audio_setting(folder_name):
    folder_path = os.path.join(os.getcwd(), 'static', folder_name)
    
    if not os.path.exists(folder_path):
        return jsonify({"error": "Folder not found"}), 404

    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    audio_files.sort()
    audio_paths = [os.path.join('static', folder_name, audio) for audio in audio_files]
    print(audio_paths)

    return jsonify(audio_paths=audio_paths)