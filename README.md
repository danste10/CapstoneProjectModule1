# Program Quality Control Yoghurt Stroberi
Program ini adalah program sederhana berbasis **Python** yang dibuat untuk mencatat dan memantau hasil **Quality Control (QC)** setiap batch produksi yoghurt stroberi.  
Tujuan program ini adalah agar proses pengecekan kualitas lebih **cepat, rapi, dan terstruktur**, dengan fitur **CRUD (Create, Read, Update, & Delete)** yang lengkap.

---

## Library yang Digunakan
- **datetime** → Menampilkan tanggal otomatis dalam format `YYYY-MM-DD`
- **tabulate** → Merapikan tampilan tabel di console agar data batch mudah dibaca

---

## Fitur Utama Program
- **Create** — Menambahkan batch baru ke dalam data QC dengan tanggal otomatis  
- **Read** — Menampilkan semua batch, atau filter batch berdasarkan status (Lulus / Gagal)  
- **Update** — Mengubah data hasil QC seperti pH, warna, aroma, dan status  
- **Delete** — Menghapus data batch dari daftar
  
---

## Struktur Data
Program menyimpan data batch produksi yoghurt stroberi menggunakan **dictionary** dengan struktur seperti ini:

```python
batch_list = {
    "YS001": { "tanggal": "2025-10-01", "pH": 4.4, "warna": "Putih krem", "aroma": "Segar susu", "status": "Lulus"},
    "YS002": { "tanggal": "2025-10-02", "pH": 4.9, "warna": "Putih kekuningan", "aroma": "Asam kuat", "status": "Gagal"},
    "YS003": { "tanggal": "2025-10-03", "pH": 4.6, "warna": "Putih krem", "aroma": "Segar", "status": "Lulus"},
    "YS004": { "tanggal": "2025-10-04", "pH": 4.2, "warna": "Putih pucat", "aroma": "Kurang segar", "status": "Gagal"},
    "YS005": { "tanggal": "2025-10-05", "pH": 4.5, "warna": "Putih krem", "aroma": "Segar susu", "status": "Lulus"}
```

========================================
QUALITY CONTROL YOGHURT RASA STROBERI
========================================
-----MENU UTAMA-----
1. Lihat semua batch
2. Lihat batch lulus
3. Lihat batch gagal
4. Tambah batch produksi
5. Update hasil QC
6. Hapus data batch
7. Keluar

Masukkan pilihan menu (1-7):

