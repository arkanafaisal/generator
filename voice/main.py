"""Main entrypoint for content generation tasks (Voice TTS Demo)."""

import argparse
import sys
from pathlib import Path

# Ensure voice package is in python path
voice_root = Path(__file__).resolve().parent
if str(voice_root) not in sys.path:
    sys.path.insert(0, str(voice_root))

from utils.voice_generator import KokoroVoiceGenerator


def main() -> None:
    default_output = voice_root / "outputs" / "sample.wav"
    default_blend_output = voice_root / "outputs" / "blended_sample.wav"

    parser = argparse.ArgumentParser(description="Kokoro ONNX TTS Content Generator")
    parser.add_argument(
        "--text",
        type=str,
        default="Halo! Ini adalah pengujian sintesis suara menggunakan model Kokoro ONNX di laptop lokal.",
        help="Text to synthesize",
    )
    parser.add_argument(
        "--voice",
        type=str,
        default="af_bella",
        help="Voice preset name (e.g. af_bella, af_sarah, am_michael)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=str(default_output),
        help="Output audio WAV path",
    )
    parser.add_argument(
        "--blend",
        action="store_true",
        help="Demonstrate custom blended voice profile (70% Bella + 30% Sarah)",
    )
    args = parser.parse_args()

    print("Menginisialisasi generator suara Kokoro...")
    generator = KokoroVoiceGenerator()

    if args.blend:
        print("Membuat profil suara kustom (Blending: 70% af_bella + 30% af_sarah)...")
        custom_voice = generator.blend_voices({"af_bella": 0.7, "af_sarah": 0.3})
        output_path = default_blend_output
        _, sample_rate, saved_path = generator.generate(
            text=args.text,
            voice=custom_voice,
            output_path=output_path,
        )
        print(f"Berhasil! Profil suara kustom tersimpan di: {saved_path} ({sample_rate} Hz)")
    else:
        print(f"Menghasilkan audio dengan preset '{args.voice}'...")
        _, sample_rate, saved_path = generator.generate(
            text=args.text,
            voice=args.voice,
            output_path=args.output,
        )
        print(f"Berhasil! Audio tersimpan di: {saved_path} ({sample_rate} Hz)")



if __name__ == "__main__":
    main()

