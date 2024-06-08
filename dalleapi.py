import openai
import requests
import os

def gen(prompt, folder_name1):

    folder_name = os.path.join('static', folder_name1)

        # 폴더가 없으면 생성
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 폴더 내 파일 카운트
    file_count = len([name for name in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, name))])
    file_name = f'image{file_count + 1}.png'

    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response['data'][0]['url']

    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        with open(os.path.join(folder_name, file_name), 'wb') as file:
            file.write(image_response.content)
            print(f"Image saved successfully as {file_name}")
    else:
        print("Failed to download image")

gen("화내는 고양이",  "user_abc123")