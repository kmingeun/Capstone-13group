import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

base_model = None
base_gpt_cond_latent = None
base_speaker_embedding = None

fam_model = None
fam_gpt_cond_latent = None
fam_speaker_embedding = None

def model_load(config_path: str, checkpoint_path: str, checkpoint_dir: str, vocab_path: str, audio_path: str, model_type: str) -> tuple[Xtts, torch.Tensor, torch.Tensor]:
    global base_model, base_gpt_cond_latent, base_speaker_embedding
    global fam_model, fam_gpt_cond_latent, fam_speaker_embedding

    if model_type == "base":
        model, gpt_cond_latent, speaker_embedding = base_model, base_gpt_cond_latent, base_speaker_embedding
    else:
        model, gpt_cond_latent, speaker_embedding = fam_model, fam_gpt_cond_latent, fam_speaker_embedding

    if model is None or gpt_cond_latent is None or speaker_embedding is None:
        print(f"Loading {model_type} model...")
        config = XttsConfig()
        config.load_json(config_path)
        model = Xtts.init_from_config(config)
        model.load_checkpoint(
            config,
            checkpoint_path=checkpoint_path,
            checkpoint_dir=checkpoint_dir,
            vocab_path=vocab_path,
            use_deepspeed=False
        )
        model.cpu()
        
        print(f"Computing speaker latents for {model_type} model...")
        gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[audio_path])
        
        print(f"{model_type.capitalize()} model loaded successfully.")
    else:
        print(f"{model_type.capitalize()} model already loaded. Skipping loading step.")

    if model_type == "base":
        base_model, base_gpt_cond_latent, base_speaker_embedding = model, gpt_cond_latent, speaker_embedding
    else:
        fam_model, fam_gpt_cond_latent, fam_speaker_embedding = model, gpt_cond_latent, speaker_embedding

    return model, gpt_cond_latent, speaker_embedding

def increase_volume(tensor: torch.Tensor, factor: float) -> torch.Tensor:
    return tensor * factor

def generate_speech(model: torch.nn.Module, text: str, gpt_cond_latent: torch.Tensor, speaker_embedding: torch.Tensor, language: str, temperature: float = 0.7) -> torch.Tensor:
    print("Generating speech...")
    out = model.inference(text, language, gpt_cond_latent, speaker_embedding, temperature=temperature)
    wav_tensor = torch.tensor(out["wav"])
    return wav_tensor

def generate_and_save_speech(model: torch.nn.Module, text: str, gpt_cond_latent: torch.Tensor, speaker_embedding: torch.Tensor, output_path: str, language: str = "ko", temperature: float = 0.7, volume_factor: float = 5.0):
    wav_tensor = generate_speech(model, text, gpt_cond_latent, speaker_embedding, language, temperature)
    increased_volume_tensor = increase_volume(wav_tensor, volume_factor)
    torchaudio.save(output_path, increased_volume_tensor.unsqueeze(0), 24000)


