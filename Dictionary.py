kontak = {"Nama":"Nomor Telepon"}
kontak = {"Angel":"088219718992", "Hertod":"081991914398"}

print("="*50)
print("   Nama          | Nomor Telepon ")
print("="*50)
print("  Angel      | ", kontak["Angel"])
print(" Hertod   | ", kontak["Hertod"])
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Kontak Ari
print("Menampilkan kontak Hadeyal")
print("="*50)
print(" Kastun      | ", kontak["kastun"])
print("-"*50)
print()
print()
print("="*50)

# Menampikan Kontak Dengan Nama Riko
print("Menambahkan kontak dengan Nama Angel")
print("dengan nomor Telepon 081991914398")
kontak["Kamil"]="081991914398"
print("="*50)
print(" Kamil          | ", kontak["Kamil"])
print("-"*50)
print()
print()
print("="*50)

# Mengubah Nomor Dina Dengan Nomor Baru
print("Mengubah Nomor Hertod dengan Nomor 081991914398")
print("="*50)
print(" # Hertod   | ", kontak["Hertod"])
print("="*50)
print()
print()
print("="*50)

# Menampilkan Semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Semua Nomor
print("Menampilkan Semua Nomor dalam Kontak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan Semua Daftar Kontak
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)

# Menghapus salah satu Kontak
print("Hapus Kontak Kastun")
print("="*50)
kontak.pop("Kastun")
print(kontak.items())
print("-"*50)