Tentu. Dari proses debugging **Tracker Keuangan** kamu tadi, sebenarnya kamu menemukan beberapa error yang cukup penting. Ini bagus untuk dicatat karena konsepnya akan kepakai terus saat belajar Python/OOP.

## 📝 Rangkuman error kamu

### 1. Data hanya muncul 1 item

Awalnya kamu membuat object seperti ini di dalam loop:

```python
menjalankanapp = tarckerPemasukkan(
    input_pemasukkan,
    input_jenis_pemasukkan
)
```

Setiap kali tambah pemasukan, kamu **membuat object baru**.

Akibatnya:

```text
Tambah 100000
→ Object A
→ list = [100000]

Tambah 50000
→ Object B
→ list = [50000]
```

Data sebelumnya tidak berada di object yang baru.

### Solusi

Buat object **sekali saja**:

```python
menjalankan_app_pemasukkan = tarckerPemasukkan()
```

di luar `while`.

Kemudian data dimasukkan melalui method:

```python
menjalankan_app_pemasukkan.input_pemasukkan(
    nominal,
    jenis
)
```

---

## 2. `list_pemasukkan = []` tidak menghapus data

Kamu sempat mencoba:

```python
def hapus(self):
    self.list_pemasukkan = []
```

Masalahnya bisa muncul kalau kamu membuat assignment lokal/objek baru dan bukan memodifikasi list yang sedang digunakan.

Untuk mengosongkan list yang sudah ada, kamu menggunakan:

```python
self.list_pemasukkan.clear()
```

Ini yang akhirnya kamu gunakan:

```python
def hapus(self):
    self.list_pemasukkan.clear()
```

✅ Ini benar.

---

## 3. Data menjadi duplikat

Ini error yang paling menarik.

Di `formatter.py` awalnya kamu punya:

```python
items_pemasukkan = []
```

kemudian:

```python
def formatListPemasukkan(data_pemasukkan, jenis_pemasukkan):
    items_pemasukkan.append({...})
    return items_pemasukkan
```

Masalahnya adalah `items_pemasukkan` **terus menyimpan data lama**.

Misalnya:

```text
Input 1
→ [A]

Input 2
→ [A, B]

Input 3
→ [A, B, C]
```

Kemudian di class kamu melakukan:

```python
self.list_pemasukkan.extend(dataList)
```

Maka:

```text
Input 1 → [A]
Input 2 → [A, A, B]
Input 3 → [A, A, B, A, B, C]
```

Makanya di output kamu muncul:

```text
1000000 gaji
20000 bonus

1000000 gaji  ← duplikat
20000 bonus   ← duplikat
20000 dapet
```

---

## 4. Salah penggunaan `extend()` dan `append()`

Ini salah satu pelajaran penting.

Awalnya:

```python
self.list_pemasukkan.extend(dataList)
```

Kemudian formatter diubah agar hanya mengembalikan **satu dictionary**:

```python
return item
```

Misalnya:

```python
{
    "pemasukkan": 1000000,
    "jenis": "gaji",
    "waktu": "...",
    "jam": "..."
}
```

Karena `item` adalah **dictionary**, gunakan:

```python
self.list_pemasukkan.append(dataList)
```

Bukan:

```python
self.list_pemasukkan.extend(dataList)
```

### Ingat gampangnya:

**`append()`**

```python
list.append(item)
```

Memasukkan **satu item**.

```python
[
    {...},
    {...}
]
```

**`extend()`**

```python
list.extend(list_lain)
```

Menggabungkan **isi iterable**.

```python
list1 = [1, 2]
list2 = [3, 4]

list1.extend(list2)

# [1, 2, 3, 4]
```

---

## 5. Error `TypeError: string indices must be integers`

Kamu mendapatkan:

```text
TypeError: string indices must be integers, not 'str'
```

pada:

```python
items['pemasukkan']
```

Penyebabnya adalah `items` ternyata **string**, bukan dictionary.

Hal ini bisa terjadi karena kamu menggunakan:

```python
self.list_pemasukkan.extend(dataList)
```

ketika `dataList` adalah dictionary.

Dictionary ketika di-iterasi akan menghasilkan key:

```python
{
    "pemasukkan": 100000,
    "jenis": "gaji"
}
```

Kalau di-`extend()`:

```python
list.extend(dictionary)
```

yang masuk bisa menjadi:

```python
["pemasukkan", "jenis", "waktu", "jam"]
```

Kemudian kamu melakukan:

```python
items['pemasukkan']
```

Padahal:

```python
items == "pemasukkan"
```

String tidak bisa diakses dengan key `"pemasukkan"`.

Makanya error:

```text
string indices must be integers
```

---

# 6. Nested list yang membuat loop menjadi rumit

Sebelumnya struktur data kamu kemungkinan seperti:

```python
[
    [
        {"pemasukkan": 100000},
        {"pemasukkan": 20000}
    ]
]
```

Makanya kamu harus melakukan:

```python
for items in self.list_pemasukkan:
    for item in items:
```

Setelah diperbaiki, struktur yang lebih sederhana adalah:

```python
[
    {"pemasukkan": 100000, ...},
    {"pemasukkan": 20000, ...},
    {"pemasukkan": 50000, ...}
]
```

Jadi cukup:

```python
for item in self.list_pemasukkan:
```

Ini jauh lebih mudah.

---

# 7. Kesalahan desain `formatter.py`

Awalnya `formatter.py` bukan cuma **memformat data**, tetapi juga menyimpan data:

```python
items_pemasukkan = []

def formatListPemasukkan(...):
    items_pemasukkan.append(...)
    return items_pemasukkan
```

Ini yang menyebabkan state/data tersebar.

Sekarang desain yang lebih bagus:

### `formatter.py`

Tugasnya hanya membuat dictionary:

```python
def formatListPemasukkan(data_pemasukkan, jenis_pemasukkan):
    waktu = datetime.now()

    return {
        "pemasukkan": int(data_pemasukkan),
        "jenis": jenis_pemasukkan,
        "waktu": format_tanggal(waktu),
        "jam": format_jam(waktu)
    }
```

### `TrackerPemasukkan`

Tugasnya menyimpan:

```python
self.list_pemasukkan = []
```

dan:

```python
self.list_pemasukkan.append(dataList)
```

Jadi tanggung jawabnya jelas.

---

# 🧠 Cheat sheet dari error kamu

| Masalah                           | Penyebab                                 | Solusi                         |
| --------------------------------- | ---------------------------------------- | ------------------------------ |
| Data cuma 1                       | Object dibuat ulang                      | Buat object sekali             |
| Data tidak terhapus               | List/object yang digunakan berbeda       | `clear()` pada list yang benar |
| Data duplikat                     | Formatter mengembalikan data lama + baru | Formatter return satu item     |
| `string indices must be integers` | Dictionary di-`extend()`                 | Gunakan `append()`             |
| Loop terlalu banyak               | Nested list                              | Simpan list berisi dictionary  |
| Data formatter ikut tersimpan     | Formatter punya global list              | Formatter hanya membuat data   |

### Struktur yang sekarang kamu tuju:

```text
Input
 ↓
formatListPemasukkan()
 ↓
1 dictionary
 ↓
append()
 ↓
self.list_pemasukkan
 ↓
┌───────────────┐
│ data 1        │
│ data 2        │
│ data 3        │
└───────────────┘
 ↓
tampilkan_semua()
```

Dan menurutku ini **jauh lebih berharga daripada sekadar memperbaiki error**. Kamu tadi secara langsung belajar **scope, object/state, list, dictionary, `append` vs `extend`, nested list, dan separation of concerns** dalam satu project. 🔥
