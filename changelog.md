# Changelog

Dokumentasi riwayat perubahan kode per commit ID. Setiap entri mencatat konteks struktural (pemisahan modul, penyesuaian arsitektur) dan ringkasan perubahan kode esensial (apa yang dihapus, diganti, atau ditambahkan beserta alasannya).

Format Entri:
```markdown
## [Commit ID] - <Ringkasan Singkat>
- **Konteks Struktural**: Penjelasan perubahan struktur arsitektur, fungsi, atau modul.
- **Perubahan Kode Penting**:
  - `NamaFile / Fungsi`: Menghapus/mengganti/menambah `<kode>` menjadi `<kode>` agar `<alasan>`.
```

---

<!-- Entri commit mendatang akan dicatat di bawah ini (urutan terbaru di atas) -->

## [Unreleased] - Inisialisasi Repositori Generator & Integrasi Kokoro TTS ONNX
- **Konteks Struktural**: Menyiapkan pondasi awal repositori generator konten AI (suara & multimedia) dengan arsitektur modular (`utils/voice_generator.py`), manajemen model lokal yang diabaikan Git (`.gitignore`), script CLI (`main.py`), dan dokumentasi awal (`README.md`).
- **Perubahan Kode Penting**:
  - `.gitignore`: Menambah aturan pengabaian aset model AI (`models/`), hasil generasi audio/visual (`outputs/`), virtual environment, dan file binary model (`*.onnx`, `*.bin`).
  - `requirements.txt`: Menambah daftar dependensi pustaka Python `kokoro-onnx` dan `soundfile`.
  - `utils/voice_generator.py`: Menambah class `KokoroVoiceGenerator` untuk pembungkusan model TTS, inferensi teks ke audio, daftar preset suara, serta modul *voice blending* via NumPy.
  - `main.py`: Menambah script CLI untuk pengujian sintesis suara standar dan profil campuran (*blended voice*).
  - `README.md`: Menambah dokumentasi panduan proyek, struktur folder, dan cara penggunaan.

