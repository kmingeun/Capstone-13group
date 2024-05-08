import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

# 서버 및 모델 로딩
print("Loading model...")
config = XttsConfig()
config.load_json("C:/Users/ens95/Desktop/fairy_tail/fairy_tail/xtts_v2/recipes/ljspeech/xtts_v2/checkpoint/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(
    config,
    checkpoint_path="C:/Users/ens95/Desktop/fairy_tail/fairy_tail/xtts_v2/recipes/ljspeech/xtts_v2/checkpoint/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000/checkpoint_3000-005.pth",
    checkpoint_dir="C:/Users/ens95/Desktop/fairy_tail/fairy_tail/xtts_v2/recipes/ljspeech/xtts_v2/checkpoint/checkpoint/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000",
    vocab_path="C:/Users/ens95/Desktop/fairy_tail/fairy_tail/xtts_v2/recipes/ljspeech/xtts_v2/checkpoint/checkpoint/run/training/XTTS_v2.0_original_model_files/vocab.json",
    use_deepspeed=False
)

model.cpu()

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["C:/Users/ens95/Desktop/fairy_tail/fairy_tail/xtts_v2/recipes/ljspeech/xtts_v2/content/wavs/audio2.wav"])

print("모델 로딩 완료")

    # 음성 파일 생성
print("Inference...")
out = model.inference('꽁꽁 얼어붙은 한강위를 고양이가 걸어다닙니다.', "ko", gpt_cond_latent, speaker_embedding, temperature=0.7)

torchaudio.save("output.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)