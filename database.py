import sqlite3 as sq
import pandas as pd


def buat_tabel():
    conn = sq.connect('keuangan_baru.db')

    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jenis TEXT,
    tipe TEXT,
    nominal INTEGER,
    waktu TEXT)
    """)

    conn.commit()
    conn.close()


def tambah_item(jenis, tipe, nominal, waktu):
    conn = sq.connect('keuangan_baru.db')

    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO transaksi(jenis, tipe, nominal, waktu)
    VALUES(?, ?, ?, ?)
    """, (jenis, tipe, nominal, waktu))
    conn.commit()
    conn.close()


def tampilkan_list():
    conn = sq.connect('keuangan_baru.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM transaksi
    """)

    data = cursor.fetchall()

    df = pd.DataFrame(
        data, columns=['id', 'tipe', 'jenis', 'nominal', 'waktu'])
    print(df)
    # for item in data:
    #     print(item)

    conn.commit()
    conn.close()


def ambil_data():
    conn = sq.connect('keuangan_baru.db')

    df = pd.read_sql_query("""
    SELECT tipe, jenis, nominal, waktu
    FROM transaksi
    """, conn)

    conn.close()
    return df


def seluruh_saldo():
    df = ambil_data()
    total_pemasukkan = df.loc[df['jenis'] == 'pemasukkan', 'nominal'].sum()
    total_pengeluaran = df.loc[df['jenis'] == 'pengeluaran', 'nominal'].sum()

    saldo = total_pemasukkan - total_pengeluaran

    return f"Rp{saldo:,}".replace(",", ".")


def tampilkan_total_pemasukkan():
    df = ambil_data()

    # print(df['jenis'].unique())
    total = df.loc[df['jenis'] == 'pemasukkan', 'nominal'].sum()

    return f"Total: Rp{total:,}".replace(",", ".")


def tampilkan_total_pengeluaran():
    df = ambil_data()

    total = df.loc[df['jenis'] == 'pengeluaran', 'nominal'].sum()

    return f"Total: Rp{total:,}".replace(",", ".")


def tampilkan_tipe(tipe):
    df = ambil_data()

    tampilkan = df.loc[df['jenis'] == tipe]

    return tampilkan


def tampilkan_nominal(tipe):
    df = ambil_data()
    total = df.loc[df['jenis'] == tipe, 'nominal']

    return total
