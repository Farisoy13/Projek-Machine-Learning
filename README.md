Identifikasi Tiga Jenis Klasifikasi Dataset

Repository ini berisi tiga program Python untuk mengidentifikasi jenis klasifikasi dataset menggunakan library Pandas.

1. Binary Classification

Nama Dataset: Breast Cancer Wisconsin (Diagnostic)

Sumber Dataset:
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

Jumlah Output: 1

Kategori:

Benign
Malignant

Binary Classification merupakan metode klasifikasi yang memiliki satu output dengan dua kemungkinan kategori.

2. Multiclass Classification

Nama Dataset: Iris

Sumber Dataset:
https://archive.ics.uci.edu/dataset/53/iris

Jumlah Output: 1

Kategori:

Iris-setosa
Iris-versicolor
Iris-virginica

Multiclass Classification merupakan metode klasifikasi yang memiliki satu output dengan lebih dari dua kategori.

3. Multilabel Classification

Nama Dataset: Yeast

Sumber Dataset:
https://www.openml.org/search?id=40597&sort=runs&type=data

Jumlah Output: 14 label.

Kategori:

Class1
Class2
Class3
Class4
Class5
Class6
Class7
Class8
Class9
Class10
Class11
Class12
Class13
Class14

Multilabel Classification merupakan metode klasifikasi yang memungkinkan satu data memiliki beberapa label sekaligus.

Perbedaan Jenis Klasifikasi
Binary Classification: satu output dengan dua kategori.
Multiclass Classification: satu output dengan lebih dari dua kategori.
Multilabel Classification: memiliki beberapa output atau label yang dapat dimiliki secara bersamaan oleh satu data.
Library yang Digunakan
Pandas
UCI ML Repository
Scikit-learn
Cara Menjalankan

Instal library:

pip install pandas ucimlrepo scikit-learn

Jalankan program:

python 01_binary_classification.py

python 02_multiclass_classification.py

python 03_multilabel_classification.py

## Dokumentasi Git Push dan Pull

Pada repository ini digunakan Git untuk mengelola perubahan file.

Git Pull digunakan untuk mengambil perubahan terbaru dari repository GitHub ke komputer lokal.

Git Push digunakan untuk mengirim perubahan yang telah dilakukan di komputer lokal ke repository GitHub.
## Dokumentasi Git Push dan Pull
Git Pull digunakan untuk mengambil perubahan terbaru dari GitHub ke komputer lokal.
Git Push digunakan untuk mengirim perubahan dari komputer lokal ke GitHub.
