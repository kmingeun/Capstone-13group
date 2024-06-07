import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

# 서버 및 모델 로딩
print("Loading model...")
config = XttsConfig()
config.load_json("C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint_pororo/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-May-09-2024_02+29AM-0000000/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(
    config,
    checkpoint_path="C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint_pororo/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-May-09-2024_02+29AM-0000000/checkpoint_6006-003.pth",
    checkpoint_dir="C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint_pororo/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-May-09-2024_02+29AM-0000000",
    vocab_path="C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint_pororo/checkpoint/run/training/XTTS_v2.0_original_model_files/vocab.json",
    use_deepspeed=False
)

model.cuda()

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/content_pororo/content/wavs/audio2.wav"])

print("모델 로딩 완료")

    # 음성 파일 생성
print("Inference...")
out = model.inference('옛날 옛적에, 푸른 숲 속 깊은 곳에 마법의 왕국이 있었습니다.', "ko", gpt_cond_latent, speaker_embedding, temperature=0.7)

torchaudio.save("output.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)