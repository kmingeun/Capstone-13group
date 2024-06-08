import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

def increase_volume(tensor: torch.Tensor, factor: float) -> torch.Tensor:
    return tensor * factor

# 서버 및 모델 로딩
print("Loading model...")
config = XttsConfig()
config.load_json("C:/Users/ens95/Desktop/Capstone-13group/model/TTS/recipes/ljspeech/xtts_v2/checkpoint-base/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(
    config,
    checkpoint_path="C:/Users/ens95/Desktop/Capstone-13group/model/TTS/recipes/ljspeech/xtts_v2/checkpoint-base/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000/checkpoint_3000-006.pth",
    checkpoint_dir="C:/Users/ens95/Desktop/Capstone-13group/model/TTS/recipes/ljspeech/xtts_v2/checkpoint-base/run/training/GPT_XTTS_v2.0_BBANGHYONG_FT-April-15-2024_11+22PM-0000000",
    vocab_path="C:/Users/ens95/Desktop/Capstone-13group/model/TTS/recipes/ljspeech/xtts_v2\checkpoint-base/run/training/XTTS_v2.0_original_model_files/vocab.json",
    use_deepspeed=False
)

model.cpu()

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["C:/Users/ens95/Desktop/Capstone-13group/model/TTS/recipes/ljspeech/xtts_v2/content-base/wavs/audio2.wav"])

print("모델 로딩 완료")

    # 음성 파일 생성
print("Inference...")
out = model.inference('옛날 옛적에, 푸른 숲 속 깊은 곳에 마법의 왕국이 있었습니다.', "ko", gpt_cond_latent, speaker_embedding, temperature=0.7)

# 볼륨 증가
wav_tensor = torch.tensor(out["wav"])
increased_volume_tensor = increase_volume(wav_tensor, 5.0)  # 볼륨을 n배로 증가

torchaudio.save("output-base.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)