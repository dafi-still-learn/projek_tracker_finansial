Tentu. Dari error yang kamu kirim selama mengembangkan **web tracker keuangan**, ini rangkumannya:

### 1. `ValueError: invalid literal for int() with base 10: ''`

**Penyebab:**

Kamu melakukan:

```python
int(input_pemasukkan)
```

tetapi `input_pemasukkan` ternyata string kosong:

```python
""
```

Jadi Python mencoba:

```python
int("")
```

**Solusi yang kamu temukan:**

```python
if input_pemasukkan:
    ...
```

Sehingga input kosong tidak langsung diproses.

> Catatan: `if input_pemasukkan` hanya menangani input kosong. Kalau user memasukkan `"abc"`, tetap perlu `try/except`.

---

### 2. Data tidak muncul di dashboard

**Penyebab:**

Kamu membuat object tracker **dua kali**.

Di `main.py`:

```python
menjalankan_app_pemasukkan = tarckerPemasukkan()
```

Tetapi di `dashboard.py` kamu membuat lagi:

```python
menjalankan_app_pemasukkan = tarckerPemasukkan()
```

Akibatnya:

```text
main.py
   ↓
Tracker A
   ↓
data masuk ke sini

dashboard.py
   ↓
Tracker B
   ↓
kosong
```

**Solusi:**

Jangan membuat tracker baru di `dashboard.py`.

Dashboard menerima object/data dari `main.py`.

---

### 3. Data hilang setelah Streamlit melakukan rerun

**Penyebab:**

Setiap kali tombol Streamlit ditekan, aplikasi melakukan **rerun**.

Kalau kamu punya:

```python
menjalankan_app_pemasukkan = tarckerPemasukkan()
```

object tersebut dibuat ulang.

Akibatnya data sebelumnya hilang.

**Solusi:**

Gunakan:

```python
st.session_state
```

Contohnya:

```python
if "tracker_pemasukkan" not in st.session_state:
    st.session_state.tracker_pemasukkan = tarckerPemasukkan()
```

Dengan begitu object tetap dipertahankan selama session.

---

### 4. Input tidak kosong setelah submit

**Masalah:**

Setelah memasukkan data, `st.text_input()` masih berisi input sebelumnya.

**Solusi:**

Gunakan:

```python
with st.form("form_pemasukkan", clear_on_submit=True):
```

Sehingga setelah submit:

```text
100000
bonus
   ↓
Kirim
   ↓
data disimpan
   ↓
input kembali kosong
```

---

### 5. `KeyError: 'pemasukkan'`

Ini error terakhir yang kamu kirim.

Kode yang bermasalah:

```python
total = df['pemasukkan'].sum()
```

**Penyebab sebenarnya:**

Ketika belum ada data, kemungkinan:

```python
pemasukkan_dashboard(...)
```

mengembalikan:

```python
[]
```

Kemudian:

```python
df = pd.DataFrame([])
```

menghasilkan DataFrame tanpa kolom:

```text
Columns: []
Index: []
```

Maka:

```python
df['pemasukkan']
```

tidak ditemukan → `KeyError`.

Menariknya, ketika data sudah ada, kamu membuktikan bahwa kolomnya memang:

```python
['pemasukkan', 'jenis', 'waktu', 'jam']
```

Jadi **bukan salah nama kolom**.

**Solusi:**

```python
if not df.empty:
    total = df['pemasukkan'].sum()

    df.loc[len(df)] = {
        'pemasukkan': total,
        'jenis': 'TOTAL'
    }
```

---

### Ringkasan perjalanan error-mu

```text
Input kosong
   ↓
ValueError
   ↓
cek if input_pemasukkan
   ↓
aman


Data tidak muncul
   ↓
object tracker dibuat dua kali
   ↓
dashboard membaca object kosong
   ↓
pisahkan tanggung jawab + gunakan object yang sama


Data hilang setelah klik
   ↓
Streamlit rerun
   ↓
object dibuat ulang
   ↓
gunakan st.session_state


Input tidak kosong
   ↓
gunakan clear_on_submit=True


KeyError 'pemasukkan'
   ↓
DataFrame kosong tidak punya kolom
   ↓
cek df.empty sebelum menghitung total
```

Menurutku ini **bagus banget sebagai catatan debugging project-mu**, karena error-error ini bukan cuma error sintaks. Kamu sudah mulai ketemu konsep penting seperti **state Streamlit, object/class, DataFrame kosong, validasi input, dan pemisahan komponen**.
