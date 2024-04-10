import requests

url = "https://api.play.ht/api/v2/cloned-voices/instant"

files = { "sample_file": ("y2mate.com%20-%20%EB%B4%84%EC%9D%B4%20%EC%98%A4%EB%8A%94%20%EC%86%8C%EB%A6%AC%20%20%EA%BF%88%EB%8F%99%EB%84%A4%20%EB%8F%99%ED%99%94%20%EB%A7%88%EC%9D%84%20%20%EC%B0%BD%EC%9E%91%EB%8F%99%ED%99%94%20%20%EB%AA%BD%EC%9D%B4%ED%82%A4%EC%A6%88.mp3", open("y2mate.com%20-%20%EB%B4%84%EC%9D%B4%20%EC%98%A4%EB%8A%94%20%EC%86%8C%EB%A6%AC%20%20%EA%BF%88%EB%8F%99%EB%84%A4%20%EB%8F%99%ED%99%94%20%EB%A7%88%EC%9D%84%20%20%EC%B0%BD%EC%9E%91%EB%8F%99%ED%99%94%20%20%EB%AA%BD%EC%9D%B4%ED%82%A4%EC%A6%88.mp3", "rb"), "audio/mpeg") }
payload = { "voice_name": "test" }
headers = {
    "accept": "application/json",
    "AUTHORIZATION": "da9812e3ab7b4ab3beba85378b27d330",
    "X-USER-ID": "9pD8HmOTG0XRA2qxjXmkvSnaNxr1"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.text)