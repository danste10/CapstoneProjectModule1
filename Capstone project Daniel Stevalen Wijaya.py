from datetime import datetime
from tabulate import tabulate

batch_list = {
    "YS001" : { "tanggal": "2025-10-01", "pH": 4.4, "warna": "Putih krem", "aroma": "Segar susu", "status": "Lulus"},
    "YS002" : { "tanggal": "2025-10-02", "pH": 4.9, "warna": "Putih kekuningan", "aroma": "Asam kuat", "status": "Gagal"},
    "YS003" : { "tanggal": "2025-10-03", "pH": 4.6, "warna": "Putih krem", "aroma": "Segar", "status": "Lulus"},
    "YS004" : { "tanggal": "2025-10-04", "pH": 4.2, "warna": "Putih pucat", "aroma": "Kurang segar", "status": "Gagal"},
    "YS005" : { "tanggal": "2025-10-05", "pH": 4.5, "warna": "Putih krem", "aroma": "Segar susu", "status": "Lulus"}
}

def lihat_semua_batch():
    table = []
    for kode, info in batch_list.items():
        table.append([
            kode,
            info["tanggal"],
            info["pH"],
            info["warna"],
            info["aroma"],
            info["status"]
        ])
    headers = ["Kode", "Tanggal", "pH", "Warna", "Aroma", "Status"]
    print("\nDaftar Batch Produksi Yoghurt Stroberi:")
    print(f"{tabulate(table, headers=headers, tablefmt='grid')}\n")   

def lihat_lulus():
    table = []
    for kode, info in batch_list.items():
        if info["status"].lower() == "lulus":
            table.append([kode, info["tanggal"], info["pH"], info["warna"], info["aroma"], info["status"]])
    if table :
        headers = ["Kode", "Tanggal", "pH", "Warna", "Aroma", "Status"]
        print("\nDaftar Batch Lulus QC:")
        print(f"{tabulate(table, headers=headers, tablefmt='grid')}\n")
    else:
        print("\nTidak ada batch yang lulus QC.\n")

def lihat_gagal():
    table = []
    for kode, info in batch_list.items():
        if info["status"].lower() == "gagal":
            table.append([kode, info["tanggal"], info["pH"], info["warna"], info["aroma"], info["status"]])
    if table:
        headers = ["Kode", "Tanggal", "pH", "Warna", "Aroma", "Status"]
        print("\nDaftar Batch Gagal QC:")
        print(f"{tabulate(table, headers=headers, tablefmt='grid')}\n")
    else:
        print("\nTidak ada batch yang gagal QC.\n")

def tambah_batch():
    kode = input("Masukkan kode batch baru: ").upper()
    if kode in batch_list:
        print("Kode batch sudah ada!\n")
        return
    
    tanggal = datetime.today().strftime("%Y-%m-%d")

    while True:
        try:
            ph = float(input("Masukkan pH: "))
            break  
        except ValueError:
            print("pH harus angka! Coba lagi.")

    while True:
        status = input("Masukkan status (Lulus/Gagal): ").capitalize()
        if status in ["Lulus", "Gagal"]:
            break
        print("Status harus 'Lulus' atau 'Gagal'. Coba lagi.")

    warna = input("Masukkan warna: ").capitalize()
    aroma = input("Masukkan aroma: ").capitalize()

    batch_list[kode] = {"tanggal": tanggal, "pH": ph, "warna": warna, "aroma": aroma, "status": status}
    print(f"Batch {kode} berhasil ditambahkan!\n")

def update_qc():
    kode = input("Masukkan kode batch yang ingin diupdate: ").upper()
    if kode not in batch_list:
        print("Batch tidak ditemukan!\n")
        return

    data_lama = batch_list[kode]
    print(f"\nData batch sebelum diupdate:")
    print(f"Tanggal: {data_lama['tanggal']}, pH: {data_lama['pH']}, Warna: {data_lama['warna']}, Aroma: {data_lama['aroma']}, Status: {data_lama['status']}\n")

    tanggal = input(f"Masukkan tanggal baru (YYYY-MM-DD) [Enter = tidak diubah]: ")
    if not tanggal:
        tanggal = data_lama['tanggal']

    ph_input = input(f"Masukkan pH baru [Enter = tidak diubah]: ")
    if not ph_input:
        ph = data_lama['pH']
    else:
        try:
            ph = float(ph_input)
        except ValueError:
            print("Input pH tidak valid. Tetap menggunakan nilai lama.")
            ph = data_lama['pH']

    warna = input(f"Masukkan warna baru [Enter = tidak diubah]: ")
    if not warna:
        warna = data_lama['warna']
    else:
        warna = warna.capitalize()

    aroma = input(f"Masukkan aroma baru [Enter = tidak diubah]: ")
    if not aroma:
        aroma = data_lama['aroma']
    else:
        aroma = aroma.capitalize()

    status = input(f"Masukkan status baru (Lulus/Gagal) [Enter = tidak diubah]: ").capitalize()
    if not status or status not in ["Lulus", "Gagal"]:
        status = data_lama['status']

    batch_list[kode].update({"tanggal": tanggal,"pH": ph,"warna": warna,"aroma": aroma,"status": status})
    print(f"\nBatch {kode} berhasil diupdate!\n")

def hapus_batch():
    kode = input("Masukkan kode batch yang ingin dihapus: ").upper()
    if kode in batch_list:
        del batch_list[kode]
        print(f"Batch {kode} berhasil dihapus!\n")
    else:
        print("Batch tidak ditemukan!\n")
    

while True:
    print("="*40)
    print("QUALITY CONTROL YOGHURT RASA STROBERI")
    print("="*40 )
    print("-----MENU UTAMA-----")
    print("1. Lihat semua batch")
    print("2. Lihat batch lulus")
    print("3. Lihat batch gagal")
    print("4. Tambah batch produksi")
    print("5. Update hasil QC")
    print("6. Hapus data batch")
    print("7. Keluar\n")
    
    pilihan = input("Masukkan pilihan menu (1-7): ")
    
    if pilihan == "1":
        lihat_semua_batch()
    elif pilihan == "2":
        lihat_lulus()
    elif pilihan == "3":
        lihat_gagal()
    elif pilihan == "4":
        tambah_batch()
    elif pilihan == "5":
        update_qc()
    elif pilihan == "6":
        hapus_batch()
    elif pilihan == "7":
        print("Keluar dari program\nTerima kasih")
        break
    else:
        print("Menu belum tersedia / salah input.\n")