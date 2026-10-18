
from pathlib import Path
import pandas as pd

# Lokasi file proyek
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "penjualan.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Membaca data
df = pd.read_csv(DATA_FILE)

print("=" * 45)
print("ANALISIS DATA PENJUALAN TOKO")
print("=" * 45)

# 2. Memeriksa kualitas data awal
print("\n--- KUALITAS DATA AWAL ---")
print(f"Jumlah baris awal: {len(df)}")
print("\nJumlah nilai kosong:")
print(df.isnull().sum())

print(f"\nJumlah baris duplikat: {df.duplicated().sum()}")

# 3. Membersihkan data
df["tanggal"] = pd.to_datetime(
    df["tanggal"], errors="coerce"
)
df["produk"] = df["produk"].astype("string").str.strip()
df["produk"] = df["produk"].str.title()

for kolom in ["jumlah", "harga_satuan"]:
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")

# Menghapus baris yang memiliki data penting kosong
df = df.dropna(
    subset=["tanggal", "produk", "jumlah", "harga_satuan"]
)

# Menghapus transaksi duplikat
df = df.drop_duplicates()

# Memastikan jumlah dan harga bernilai positif
df = df[
    (df["jumlah"] > 0) &
    (df["harga_satuan"] > 0)
].copy()

# 4. Menghitung pendapatan setiap transaksi
df["pendapatan"] = df["jumlah"] * df["harga_satuan"]

# 5. Analisis deskriptif
total_transaksi = len(df)
total_unit = int(df["jumlah"].sum())
total_pendapatan = df["pendapatan"].sum()

ringkasan_produk = (
    df.groupby("produk", as_index=False)
    .agg(
        total_terjual=("jumlah", "sum"),
        total_pendapatan=("pendapatan", "sum")
    )
    .sort_values("total_pendapatan", ascending=False)
)

produk_terlaris = (
    df.groupby("produk")["jumlah"].sum().idxmax()
)

produk_pendapatan_tertinggi = (
    ringkasan_produk.iloc[0]["produk"]
)

# 6. Menampilkan hasil analisis
print("\n--- HASIL ANALISIS ---")
print(f"Transaksi valid: {total_transaksi}")
print(f"Total unit terjual: {total_unit}")
print(f"Total pendapatan: Rp{total_pendapatan:,.0f}")
print(f"Produk dengan unit terjual terbanyak: {produk_terlaris}")
print(
    "Pendapatan tertinggi berasal dari: "
    f"{produk_pendapatan_tertinggi}"
)

print("\n--- RINGKASAN PER PRODUK ---")
print(ringkasan_produk.to_string(index=False))

# 7. Membuat insight dan rekomendasi
produk_unit_tertinggi = (
    df.groupby("produk")["jumlah"].sum().idxmax()
)

insight = [
    f"Total pendapatan toko mencapai Rp{total_pendapatan:,.0f}.",
    f"Total produk terjual sebanyak {total_unit} unit.",
    f"{produk_unit_tertinggi} memiliki jumlah unit terjual tertinggi.",
    f"{produk_pendapatan_tertinggi} menghasilkan pendapatan terbesar."
]

rekomendasi = [
    f"Evaluasi stok {produk_unit_tertinggi} agar persediaannya cukup.",
    f"Evaluasi strategi penjualan {produk_pendapatan_tertinggi}.",
    "Periksa data transaksi secara berkala untuk menghindari "
    "data kosong dan duplikat."
]

print("\n--- INSIGHT ---")
for item in insight:
    print(f"- {item}")

print("\n--- REKOMENDASI ---")
for item in rekomendasi:
    print(f"- {item}")

# 8. Menyimpan hasil ke folder output
df.to_csv(
    OUTPUT_DIR / "penjualan_bersih.csv",
    index=False
)

ringkasan_produk.to_csv(
    OUTPUT_DIR / "ringkasan_produk.csv",
    index=False
)

with open(
    OUTPUT_DIR / "laporan_analisis.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("LAPORAN ANALISIS DATA PENJUALAN\n\n")
    file.write("\n".join(insight))
    file.write("\n\nREKOMENDASI\n")
    file.write("\n".join(rekomendasi))

print("\nHasil analisis berhasil disimpan di folder output.")
