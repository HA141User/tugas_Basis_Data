# tugas_Basis_Data

# Simulasi B-Tree dan B+ Tree 🌳


---

## 📌 Deskripsi Proyek

Repositori ini berisi simulasi dan analisis perbandingan antara struktur data **B-Tree** dan **B+ Tree**. Simulasi ini bertujuan untuk memahami bagaimana mesin basis data (_database engine_) menyusun indeks untuk pencarian data yang efisien, lengkap dengan penanganan _node_ yang penuh (_split_) saat operasi penyisipan (_insert_).

Proyek ini menyimulasikan penyisipan 20 data berurutan:
`10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200`

---

## 📖 Konsep Dasar: Node dan Level

Sebelum memahami perbedaannya, berikut adalah dua istilah kunci dalam struktur pohon (_tree_):

- **Node (Simpul):** Kotak atau laci penyimpanan data. Dalam simulasi ini, batas maksimal satu _node_ adalah 3 _key_ (Order/Derajat = 4). Jika _node_ penuh (mencapai 4 data), ia akan membelah diri (_split_).
- **Level (Tingkat):** Menunjukkan kedalaman posisi _node_. _Root_ berada di Level 0 (puncak), sedangkan ujung terbawah disebut _Leaf_ (daun).

---

## 🔍 Apa itu B-Tree?

**B-Tree** adalah struktur pohon pencarian seimbang (_self-balancing_) di mana setiap titik persimpangan (_node_) menyimpan indeks (penunjuk jalan) sekaligus data aslinya.

**Karakteristik Utama:**

- **Data Tersebar:** Data atau _pointer record_ tidak hanya berkumpul di bawah, tetapi bisa ditemukan di seluruh level pohon (dari _Root_ hingga _Leaf_).
- **Keunggulan:** Pencarian satu data spesifik bisa sangat cepat jika kebetulan data tersebut tersimpan di level atas (_Root_ atau _Internal Node_).
- **Kelemahan:** Tidak efisien untuk pencarian berurutan (_range query_) karena sistem harus menelusuri cabang naik dan turun secara berulang.

---

## 🚀 Apa itu B+ Tree?

**B+ Tree** adalah perluasan dari B-Tree dan merupakan arsitektur indeks yang paling umum digunakan dalam sistem basis data relasional modern (seperti MySQL dan PostgreSQL).

**Karakteristik Utama:**

- **Pemisahan Tugas:** _Node_ di bagian atas (Level 0, 1, dst.) HANYA berfungsi sebagai indeks atau petunjuk arah.
- **Data Mengumpul di Daun:** Seluruh data asli secara eksklusif dipaksa turun dan disimpan di tingkat paling bawah (_Leaf Node_).
- **Fitur Linked List:** Seluruh _Leaf Node_ saling terhubung menyamping dengan _pointer_ (rantai penghubung).
- **Keunggulan:** Kecepatan pencarian rentang (_range query_) sangat efisien karena sistem hanya perlu turun satu kali ke _Leaf_, lalu berjalan menyamping melintasi _Linked List_ tanpa harus naik-turun pohon lagi.

---

## 📊 Perbandingan Singkat

| Fitur                   | B-Tree                                                 | B+ Tree                                                              |
| :---------------------- | :----------------------------------------------------- | :------------------------------------------------------------------- |
| **Penyimpanan Data**    | Tersebar di semua _node_ (_Root_, _Internal_, _Leaf_). | Eksklusif hanya di tingkat paling bawah (_Leaf_).                    |
| **Duplikasi Key**       | Tidak ada. Setiap nilai hanya muncul satu kali.        | Ada. Nilai indeks di atas diduplikasi lagi di bawah bersama datanya. |
| **Penghubung Daun**     | Tidak saling terhubung.                                | Menggunakan _Linked List_ antar daun.                                |
| **Kinerja Range Query** | Relatif lambat.                                        | Sangat cepat dan stabil.                                             |

---

## 💻 Cara Menjalankan Simulasi

Simulasi ini ditulis menggunakan bahasa pemrograman Python. Terdapat dua file terpisah untuk membandingkan output dari kedua struktur.

**1. Menjalankan Simulasi B-Tree:**

```bash
python b-tree.py
```

Output akan memperlihatkan data yang tersebar di berbagai level tanpa ada hubungan antar daun.

**2. Menjalankan Simulasi B+ Tree:**

```bash
python bplus-tree.py
```

Output akan menunjukkan bahwa level atas hanya berisi indeks (INDEX), semua data tersimpan di level terbawah (LEAF), dan diakhiri dengan visualisasi sambungan Linked List antar daun.
