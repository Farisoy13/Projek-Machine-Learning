# ==========================================
# MULTILABEL CLASSIFICATION
# Dataset: Yeast
# Sumber:
# https://www.openml.org/search?id=40597&sort=runs&type=data
# ==========================================

import pandas as pd
from sklearn.datasets import fetch_openml

# Mengambil dataset Yeast
dataset = fetch_openml(
    data_id=40597,
    as_frame=True,
    target_column=None
)

# Mengubah dataset menjadi DataFrame
df = dataset.frame.copy()

# Mengidentifikasi kolom label
label_cols = [
    col for col in df.columns
    if str(col).lower().startswith("class")
]

# Menampilkan informasi dataset
print("=== MULTILABEL CLASSIFICATION ===")

print("\nUkuran Dataset:")
print(df.shape)

print("\nLima Data Pertama:")
print(df.head())

print("\nInformasi Dataset:")
df.info()

print("\nJumlah Missing Values:")
print(df.isnull().sum().sum())

print("\nKolom Label:")
print(label_cols)

print("\nJumlah Label:")
print(len(label_cols))

print("\nDistribusi Setiap Label:")

for col in label_cols:
    print(f"\n{col}")
    print(df[col].value_counts())

if len(label_cols) > 1:
    print(
        "\nKesimpulan: Dataset termasuk "
        "Multilabel Classification."
    )