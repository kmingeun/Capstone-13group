import requests

url = "https://api.play.ht/api/v2/tts"

payload = {
    "text": "그는 괜찮은 척 하려고 애쓰는 것 같았다.",
    "voice": "s3://voice-cloning-zero-shot/11f747eb-26a5-4630-83c5-f5cc80f7fbf1/test/manifest.json",
    "output_format": "mp3",
    "voice_engine": "PlayHT1.0",
    "speed": 1,
    "sample_rate": 24000,
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "AUTHORIZATION": "da9812e3ab7b4ab3beba85378b27d330",
    "X-USER-ID": "9pD8HmOTG0XRA2qxjXmkvSnaNxr1"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)