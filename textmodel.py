import torch
import transformers
from transformers import AutoModelWithLMHead, PreTrainedTokenizerFast
from fastai.text.all import *
import fastai
import re
from transformers import GPT2LMHeadModel, GPT2Tokenizer

#로컬모델 사용
model_path = "C:/Users/ens95/Desktop/Capstone-13group/model/Textmodel/tale"
tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')

model = GPT2LMHeadModel.from_pretrained(model_path)

def generate_story_with_custom_model(tokenizer, model, prompt):
    try:
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(
            inputs,
            max_length=200,# 생성할 텍스트의 최대 길이
            num_return_sequences=1,
            repetition_penalty=2.0, # 반복 단어에 대한 패널티 적용
            temperature=0.7,# 생성 다양성 조절 (어린이 이야기에 맞게 조정)
            top_k=50, # 가장 가능성 높은 k개의 단어를 고려
            top_p=0.95,# 누적 확률 p의 가장 가능성 높은 단어 선택 (높여서 긍정적인 이야기 생성)
            do_sample=True
        )
        story = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story
    except Exception as e:
        print(f"이야기 생성 중 오류가 발생했습니다: {e}")
        return "이야기를 생성하는 데 실패했습니다."


def post_process_story(story):
    sentences = story.split('. ')
    unique_sentences = []
    for sentence in sentences:
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)
    story = '. '.join(unique_sentences)
    if not story.endswith("행복하게 살았습니다."):
        story += " 그 후로 그들은 오래오래 행복하게 살았습니다."
    return story


def evaluate_story(story):
    return len(story), "일관성 있음" if "모험" in story else "일관성 없음"

def create_story(first, second, third):
    # 주인공 선택
    main_character = first['title'].strip('<>')
    second_character = second['title'].strip('<>')
    third_character = third['title'].strip('<>')
    companions = [second_character, third_character]

    # 이야기 생성에 필요한 프롬프트 작성
    prompt = (
        f"옛날 옛날에 {main_character}가 살고 있었습니다. "
        f"그 {main_character}는 {', '.join(companions)}라는 친구들과 함께 살고 있었습니다. "
        f"그들은 어느 날 모험을 떠나기로 결심했습니다. 먼저 그들은 숲 속에서 신기한 물건을 발견했고, "
        f"그 후에는 무서운 괴물과 맞서 싸웠으며, 마지막에는 행복하게 집으로 돌아왔습니다. "
        f"그들의 모험은 이렇게 시작됩니다. "
        f"그 모험 속에서 {main_character}와 친구들은 큰 교훈을 얻었어요. "
        f"그들은 서로를 돕고, 어려운 상황을 극복하면서 진정한 우정의 의미를 깨달았습니다."
    )

    story = generate_story_with_custom_model(tokenizer, model, prompt)
    story = post_process_story(story)
    evaluation = evaluate_story(story)

    print("\n생성된 이야기:")
    print(story)
    print("\n평가 결과:", evaluation)

    return story