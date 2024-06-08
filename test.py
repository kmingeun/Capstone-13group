import torch
import torchaudio

def increase_volume(waveform: torch.Tensor, factor: float) -> torch.Tensor:
    return waveform * factor

# 기존 음성 파일 불러오기
input_file = "output-base.wav"
waveform, sample_rate = torchaudio.load(input_file)

# 볼륨 증가
factor = 4.0  # 볼륨을 2배로 증가
increased_volume_waveform = increase_volume(waveform, factor)

# 볼륨이 증가된 음성 파일 저장
output_file = "output-base-louder.wav"
torchaudio.save(output_file, increased_volume_waveform, sample_rate)

print(f"볼륨이 증가된 음성 파일이 {output_file}에 저장되었습니다.")
