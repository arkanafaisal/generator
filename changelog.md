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

## [Unreleased] - Restrukturisasi Modul ke Folder Voice dan Penghapusan README.md
- **Konteks Struktural**: Memindahkan seluruh komponen generator suara ke dalam subfolder `voice/` (`voice/utils/`, `voice/models/`, `voice/outputs/`, `voice/main.py`, `voice/requirements.txt`) untuk memisahkan domain audio dengan modul gambar di masa mendatang. Menghapus `README.md` dan menambahkan aturan learned rule 7 untuk meniadakan overhead pemeliharaan README.
- **Perubahan Kode Penting**:
  - `README.md`: Menghapus file `README.md` agar dokumentasi terpusat di `changelog.md` tanpa redundansi.
  - `GEMINI.md`: Menambahkan Rule 7 `[PROCESS]` yang melarang pembuatan/pemeliharaan `README.md` tanpa permintaan eksplisit.
  - `voice/main.py`: Memindahkan `main.py` ke `voice/main.py` dan menyesuaikan resolusi path modul serta folder output otomatis.
  - `voice/requirements.txt`: Memindahkan `requirements.txt` ke direktori `voice/`.
  - `voice/utils/`: Memindahkan direktori `utils/` ke `voice/utils/` untuk menjaga struktur modular.

## [1b7b1c9] - Inisialisasi Repositori Generator & Integrasi Kokoro TTS ONNX
- **Konteks Struktural**: Menyiapkan pondasi awal repositori generator konten AI (suara & multimedia) dengan arsitektur modular (`utils/voice_generator.py`), manajemen model lokal yang diabaikan Git (`.gitignore`), script CLI (`main.py`), dan dokumentasi awal (`README.md`).
- **Perubahan Kode Penting**:
  - `.gitignore`: Menambah aturan pengabaian aset model AI (`models/`), hasil generasi audio/visual (`outputs/`), virtual environment, dan file binary model (`*.onnx`, `*.bin`).
  - `requirements.txt`: Menambah daftar dependensi pustaka Python `kokoro-onnx` dan `soundfile`.
  - `utils/voice_generator.py`: Menambah class `KokoroVoiceGenerator` untuk pembungkusan model TTS, inferensi teks ke audio, daftar preset suara, serta modul *voice blending* via NumPy.
  - `main.py`: Menambah script CLI untuk pengujian sintesis suara standar dan profil campuran (*blended voice*).
  - `README.md`: Menambah dokumentasi panduan proyek, struktur folder, dan cara penggunaan.

