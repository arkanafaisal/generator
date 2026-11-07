# Generator

Proyek otomasi pembuatan konten multimedia (suara, teks, gambar) lokal yang efisien dan modular.

## Fitur Utama

- **Kokoro TTS (ONNX Runtime)**: Sintesis teks ke suara (Text-to-Speech) berkualitas studio (24kHz) berbasis model Kokoro-82M yang dioptimalkan untuk eksekusi CPU lokal yang ringan dan cepat.
- **Voice Blending**: Kemampuan mencampur beberapa preset suara bawaan dengan bobot persentase tertentu menjadi persona suara baru via kalkulasi vektor NumPy.
- **Proteksi Model Lokal**: Seluruh bobot model (`.onnx`, `.bin`) dan hasil generasi (`outputs/`) otomatis diabaikan oleh Git via `.gitignore`.

## Struktur Direktori

```text
generator/
├── models/
│   └── kokoro/             # Bobot model Kokoro & voice packs (diabaikan Git)
├── outputs/                # Folder penyimpanan file audio hasil sintesis (diabaikan Git)
├── utils/
│   ├── __init__.py
│   └── voice_generator.py  # Wrapper modular Kokoro TTS & Voice Blending
├── changelog.md            # Dokumentasi riwayat perubahan per commit
├── GEMINI.md               # Aturan kerja & self-correcting rules engine
├── main.py                 # CLI / Entrypoint sintesis suara
└── requirements.txt        # Dependensi Python
```

## Memulai

1. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan pengujian sintesis suara standar:
   ```bash
   python main.py --text "Halo dunia!" --voice af_bella
   ```

3. Jalankan pengujian dengan *Voice Blending* kustom:
   ```bash
   python main.py --blend
   ```

