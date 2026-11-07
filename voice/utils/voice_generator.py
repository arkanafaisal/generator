from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro


class KokoroVoiceGenerator:
    """Modular wrapper for Kokoro TTS using ONNX Runtime.

    Supports synthesis with preset voices and custom voice blending.
    """

    DEFAULT_VOICES = [
        "af_bella", "af_heart", "af_nicole", "af_sarah", "af_sky",
        "am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam",
        "am_michael", "am_onyx", "am_puck", "am_santa",
        "bf_alice", "bf_emma", "bf_isabella", "bf_lily",
        "bm_daniel", "bm_fable", "bm_george", "bm_lewis"
    ]

    def __init__(
        self,
        model_path: Optional[Union[str, Path]] = None,
        voices_path: Optional[Union[str, Path]] = None,
    ) -> None:
        project_root = Path(__file__).resolve().parent.parent
        self.model_path = Path(
            model_path or project_root / "models" / "kokoro" / "kokoro-v1.0.onnx"
        )
        self.voices_path = Path(
            voices_path or project_root / "models" / "kokoro" / "voices-v1.0.bin"
        )

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Kokoro model file not found at: {self.model_path}"
            )
        if not self.voices_path.exists():
            raise FileNotFoundError(
                f"Voices embedding file not found at: {self.voices_path}"
            )

        self._kokoro = Kokoro(str(self.model_path), str(self.voices_path))

    def get_available_voices(self) -> List[str]:
        """Return list of common pre-configured voices."""
        return list(self.DEFAULT_VOICES)

    def get_voice_style(self, voice_name: str) -> np.ndarray:
        """Fetch style vector for a given voice name."""
        return self._kokoro.get_voice_style(voice_name)

    def blend_voices(self, voice_weights: Dict[str, float]) -> np.ndarray:
        """Blend multiple voice embeddings based on provided weights.

        Args:
            voice_weights: Mapping of voice names to relative weights,
                           e.g., {"af_bella": 0.7, "af_sarah": 0.3}.

        Returns:
            np.ndarray: Blended voice embedding vector.
        """
        if not voice_weights:
            raise ValueError("voice_weights dictionary cannot be empty.")

        total_weight = sum(voice_weights.values())
        if total_weight <= 0:
            raise ValueError("Sum of voice weights must be greater than zero.")

        blended = None
        for voice_name, weight in voice_weights.items():
            normalized_weight = weight / total_weight
            style = self.get_voice_style(voice_name)
            if blended is None:
                blended = style * normalized_weight
            else:
                blended += style * normalized_weight

        return blended

    def save_voice_profile(
        self, voice_style: np.ndarray, file_path: Union[str, Path]
    ) -> Path:
        """Save a custom voice embedding to a .npy file."""
        target_path = Path(file_path)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(str(target_path), voice_style)
        return target_path

    def load_voice_profile(self, file_path: Union[str, Path]) -> np.ndarray:
        """Load a custom voice embedding from a .npy file."""
        target_path = Path(file_path)
        if not target_path.exists():
            raise FileNotFoundError(f"Voice profile not found at: {target_path}")
        return np.load(str(target_path))

    def generate(
        self,
        text: str,
        voice: Union[str, np.ndarray] = "af_sarah",
        speed: float = 1.0,
        lang: str = "en-us",
        output_path: Optional[Union[str, Path]] = None,
    ) -> Tuple[np.ndarray, int, Optional[Path]]:
        """Synthesize text to speech audio samples.

        Args:
            text: Input text to speak.
            voice: Name of voice string or custom numpy embedding array.
            speed: Speech rate multiplier (1.0 default).
            lang: Target language code ('en-us', 'en-gb', etc.).
            output_path: Optional path to save WAV file.

        Returns:
            Tuple of (audio_samples, sample_rate, saved_file_path).
        """
        samples, sample_rate = self._kokoro.create(
            text=text,
            voice=voice,
            speed=speed,
            lang=lang,
        )

        saved_path = None
        if output_path is not None:
            saved_path = Path(output_path)
            saved_path.parent.mkdir(parents=True, exist_ok=True)
            sf.write(str(saved_path), samples, sample_rate)

        return samples, sample_rate, saved_path

