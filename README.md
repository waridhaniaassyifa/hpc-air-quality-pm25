# **Prediksi Kualitas Udara (PM2.5) Berbasis High Performance Computing (HPC) & Deep Learning**

Proyek ini merupakan implementasi studi kasus pembelajaran berdasarkan materi “Career and Competition in Industrial Era” oleh Widi Primadepa dari City Care Property, Christchurch, Selandia Baru, mengenai pelatihan model Deep Learning (PyTorch) untuk memprediksi tingkat konsentrasi partikulat polusi udara (PM2.5) menggunakan data indikator cuaca lokal. Skrip dirancang agar fleksibel dan dapat dieksekusi baik di lingkungan lokal (pengujian) maupun pada klaster High Performance Computing (HPC) berbasis manajemen pekerjaan SLURM.

**💡 Latar Belakang & Inspirasi**

Polusi udara lokal, khususnya partikulat PM2.5, merupakan salah satu tantangan lingkungan dan kesehatan masyarakat yang krusial. Pengolahan data sensor berskala besar serta pelatihan model kecerdasan buatan (Artificial Intelligence) memerlukan sumber daya komputasi yang besar dan efisien.

Proyek ini terinspirasi dari materi Kuliah Praktisi "Bridging Global Infrastructure to Address Local Challenge with HPC" oleh Worawan Diaz Carballo (Thammasat University, Thailand), yang menekankan pentingnya peran integrator dalam menjembatani teknologi komputasi berkinerja tinggi untuk mengatasi permasalahan nyata di tingkat lokal.

**🔄 Alur Kerja Integrator (Integrator Workflow)**

Sebagai bentuk penerapan konsep integrator, alur kerja proyek ini meliputi:
1. Pengumpulan & Pra-pemrosesan Data Lokal: Mengolah dataset indikator cuaca (suhu, kelembapan,            kecepatan angin) serta konsentrasi PM2.5 menggunakan pandas dan scikit-learn.

2. Fleksibilitas Perangkat Komputasi: Menggunakan PyTorch dengan deteksi perangkat otomatis (cuda untuk    GPU HPC / cpu untuk pengujian lokal).
  
3. Manajemen Pekerjaan Komputasi (SLURM): Menggunakan job script (submit_job.sh) untuk mengirimkan dan     mengantrekan proses pelatihan di klaster HPC.
  
4. Analisis & Evaluasi: Mengevaluasi kinerja model (MSE Loss) serta menyimpan model terlatih               (outputs/pm25_model.pth) untuk dapat dimanfaatkan lebih lanjut.

**📁 Struktur Direktori**

hpc-air-quality-pm25/
├── data/
│   └── air_quality_sample.csv  # Dataset contoh indikator cuaca & PM2.5
├── outputs/                    # Folder penyimpanan model terlatih (dibuat otomatis)
├── train_hpc.py                # Skrip utama pelatihan PyTorch
├── submit_job.sh               # Skrip pekerjaan SLURM untuk eksekusi di HPC
├── .gitignore                  # Berkas pengabaian versi Git
└── README.md                   # Dokumentasi proyek


**🚀 Panduan Instalasi & Eksekusi**

**1.) Eksekusi Lokal (Local Testing & Debugging)**
Langkah-langkah untuk menguji kode di komputer lokal atau VS Code:

  1. Clone Repositori:
     git clone https://github.com/USERNAME/hpc-air-quality-pm25.git
     cd hpc-air-quality-pm25
    
  2. Buat & Aktifkan Virtual Environment (Opsional):
     python -m venv venv
     # Di Windows:
       venv\Scripts\activate
     # Di macOS/Linux:
       source venv/bin/activate
    
  3. Install Dependensi:
     pip install torch pandas scikit-learn
  
  4. Jalankan Skrip Pelatihan:
     python train_hpc.py

**2.) Eksekusi pada Klaster HPC (SLURM Job Scheduler)**
Langkah-langkah untuk menjalankan pelatihan pada klaster HPC:

   1. Akses HPC Server via SSH:
      ssh username@hpc.domain.ac.id
      
   2. Clone Repositori di Environment HPC Anda:
      git clone https://github.com/USERNAME/hpc-air-quality-pm25.git
      cd hpc-air-quality-pm25
      
   3. Kirimkan Pekerjaan ke Antrean SLURM:
      sbatch submit_job.sh
      
   4. Cek Status Antrean Pekerjaan:
      squeue -u username
      
   5. Periksa Log Output / Hasil Eksekusi:
      cat pm25_hpc_*.log
