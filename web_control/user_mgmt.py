from flask_login import UserMixin
from db_model.mysql import conn_mysqldb

class User(UserMixin):

    def __init__(self, user_id, web_id, user_password, page_id, credit_data, subscription):
        self.user_id = user_id
        self.web_id = web_id
        self.user_password = user_password
        self.page_id = page_id
        self.credit_data = credit_data
        self.subscription = subscription

    def get_id(self):
        return str(self.user_id)
    
    @staticmethod
    def get(user_id): # user_id로 찾기
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM User_info WHERE USER_ID = '" + str(user_id) + "'"
        print(sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user: # 해당 유저가 없다면
            db_cursor.close()
            return None
        
        user = User(user_id=user[0], web_id=user[1], user_password = user[2], page_id = user[3], credit_data = user[4], subscription = user[5])
        db_cursor.close()
        return user

    @staticmethod
    def find(web_id, user_password): # web_id로 찾기
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM User_info WHERE WEB_ID = '%s' AND Password = '%s'" % (str(web_id), str(user_password))
        print(sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user: # 해당 유저가 없다면
            db_cursor.close()
            return None
        
        user = User(user_id=user[0], web_id=user[1], user_password = user[2], page_id = user[3], credit_data=user[4], subscription = user[5])
        return user
    
    @staticmethod
    def create(web_id, user_password, page_id): # 아이디와 비밀번호, user_id로
        user = User.find(web_id, user_password) # 해당 유저정보가 있는지 db에서 확인
        if user == None: # 없다면 db에 넣기
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (Web_ID, Password, Page_ID) VALUES ('%s', '%s', '%s')" % (str(web_id), str(user_password), str(page_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(web_id, user_password)
        else: # 해당 유저 정보가 있다면 리턴
            return user
        
    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted
    
    @staticmethod
    def update_credit(web_id, new_credit):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "UPDATE user_info SET Credit = '%s' WHERE Web_ID = '%s'" % (new_credit, web_id)
        db_cursor.execute(sql)
        update = mysql_db.commit()
        return update
    
    @staticmethod
    def update_subscribe(web_id, subscribe):
        myslq_db = conn_mysqldb()
        db_cursor = myslq_db.cursor()
        sql = "UPDATE user_info SET Subscription_type = '%s', Subscription_Start_Date = CURDATE() WHERE Web_ID = '%s'" % (subscribe, web_id)
        db_cursor.execute(sql)
        update = myslq_db.commit()
        return update