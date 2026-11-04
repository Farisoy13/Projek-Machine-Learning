# ==========================================
# BINARY CLASSIFICATION
# Dataset: Breast Cancer Wisconsin
# Sumber:
# https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
# ==========================================

import pandas as pd
from ucimlrepo import fetch_ucirepo

# Mengambil dataset
dataset = fetch_ucirepo(id=17)

# Memisahkan fitur dan target
X = dataset.data.features
y = dataset.data.targets

# Menggabungkan dataset
df = pd.concat([X, y], axis=1)

target = y.columns[0]

# Menampilkan informasi dataset
print("=== BINARY CLASSIFICATION ===")

print("\nUkuran Dataset:")
print(df.shape)

print("\nLima Data Pertama:")
print(df.head())

print("\nInformasi Dataset:")
df.info()

print("\nJumlah Missing Values:")
print(df.isnull().sum().sum())

print("\nDistribusi Label:")
print(df[target].value_counts())

print("\nJumlah Kategori:")
print(df[target].nunique())

print("\nNama Kategori:")
print(df[target].unique())

if df[target].nunique() == 2:
    print("\nKesimpulan: Dataset termasuk Binary Classification.")