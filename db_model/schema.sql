use fairy_tail;

-- 사용자 테이블 생성
CREATE TABLE User_info (
    User_ID INT AUTO_INCREMENT PRIMARY KEY, -- 사용자 구분을 위한 고유 ID --
    Web_ID VARCHAR(255) UNIQUE NOT NULL, -- 실제 웹에서 사용하는 ID --
    Password VARCHAR(255) NOT NULL,
    Page_ID CHAR(4),
    Credit INT DEFAULT 0,
    Subscription_type ENUM('basic', 'pro', 'pro+') DEFAULT NULL,
    Subscription_Start_Date DATE
);

-- 동화 테이블 생성
CREATE TABLE Stories (
    Story_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT NOT NULL,
    Title VARCHAR(255) NOT NULL,
    Text_Content TEXT NOT NULL,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (User_ID) REFERENCES User_info(User_ID)
);

-- 삽화 테이블 생성
CREATE TABLE Illustrations (
    Illustration_ID INT AUTO_INCREMENT PRIMARY KEY,
    Story_ID INT NOT NULL,
    Image_URL VARCHAR(255) NOT NULL,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Story_ID) REFERENCES Stories(Story_ID)
);

-- 음성 파일 테이블 생성
CREATE TABLE Audios (
    Audio_ID INT AUTO_INCREMENT PRIMARY KEY,
    Story_ID INT NOT NULL,
    Audio_URL VARCHAR(255) NOT NULL,
    Duration INT,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Story_ID) REFERENCES Stories(Story_ID)
);

CREATE TABLE session_info (
    user_id INT,
    session_ip VARCHAR(255),
    web_id VARCHAR(255),
    page VARCHAR(50),
    access_time DATETIME,
    PRIMARY KEY (user_id, access_time), -- 복합 키
    FOREIGN KEY (user_id) REFERENCES User_info(User_ID)
);