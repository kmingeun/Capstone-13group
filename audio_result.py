import requests

# API 요청을 설정합니다.
url = "https://api.play.ht/api/v2/tts/KoCCZq5Vd52egdo21X"
headers = {
    "accept": "audio/mpeg",
    "AUTHORIZATION": "da9812e3ab7b4ab3beba85378b27d330",
    "X-USER-ID": "9pD8HmOTG0XRA2qxjXmkvSnaNxr1"
}

# 요청을 보내고 응답을 받습니다.
response = requests.get(url, headers=headers)

# 받은 오디오 데이터(MP3)를 'output.mp3' 파일로 저장합니다.
with open("output.mp3", "wb") as out_file:
    out_file.write(response.content)
