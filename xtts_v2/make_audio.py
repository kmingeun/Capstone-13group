import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

# 서버 및 모델 로딩
print("Loading model...")
config = XttsConfig()
config.load_json("C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(
    config,
    checkpoint_path="C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000/checkpoint_3000-001.pth",
    checkpoint_dir="C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000",
    vocab_path="C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/checkpoint/run/training/XTTS_v2.0_original_model_files/vocab.json",
    use_deepspeed=False
)

model.cuda()

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["C:/Users/ens95/Desktop/TTS/TTS/recipes/ljspeech/xtts_v2/content/wavs/audio2.wav"])

print("모델 로딩 완료")

    # 음성 파일 생성
print("Inference...")
out = model.inference('옛날 어느 고을에 흥부와 놀부라는 형제가 살았어요', "ko", gpt_cond_latent, speaker_embedding, temperature=0.7)

torchaudio.save("output.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)