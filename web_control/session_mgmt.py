from db_model.mysql import conn_mysqldb
from datetime import datetime

class WebSession():
    web_page = {'A' : 'before_login.html', 'B' : 'after_login.html'}
    session_count = 0

    @staticmethod
    def save_session_info(user_id, session_ip, web_id, webpage_name): # 세션 정보 저장
        now = datetime.now()
        now_time = now.strftime("%Y-%m-%d %H:%M:%S")

        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "INSERT INTO session_info (user_id, session_ip, web_id, page, access_time) VALUES (%s, %s, %s, %s, %s)"
        db_cursor.execute(sql, (user_id, session_ip, web_id, webpage_name, now_time))
        mysql_db.commit()

    @staticmethod
    def get_web_page(page_id=None): 
        if page_id == None:
            if WebSession.session_count == 0:
                WebSession.session_count = 1
                return WebSession.web_page['A']
            else:
                WebSession.session_count = 0
                return WebSession.web_page['B']
        else:
            return WebSession.web_page[page_id]