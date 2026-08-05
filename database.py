import sqlite3 as sq
import pandas as pd


def buat_tabel():
    conn = sq.connect('keuangan.db')

    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipe TEXT,
    jenis TEXT,
    nominal INTEGER,
    waktu TEXT)
    """)

    conn.commit()
    conn.close()

# DI MAIN


def cek_tabel():
    conn = sq.connect('keuangan.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(transaksi)")

    print(cursor.fetchall())

# KU SIMPAN DI TRACKER


def tambah_item(tipe, jenis, nominal, waktu):
    conn = sq.connect('keuangan.db')

    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO transaksi(tipe, jenis, nominal, waktu)
    VALUES(?, ?, ?, ?)
    """, (tipe, jenis, nominal, waktu))
    print(tipe)
    print(jenis)
    print(nominal)
    print(waktu)
    conn.commit()
    conn.close()


def tampilkan_list():  # ! AWAL MULA ERROR NYA (DATA TERAMBIL BANYAK KETIKA DIPNGGIL)
    conn = sq.connect('keuangan.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM transaksi
    """)

    data = cursor.fetchall()

    df = pd.DataFrame(
        data, columns=['id', 'tipe', 'jenis', 'nominal', 'waktu'])
    # print(df)
    # for item in data:
    #     print(item)

    conn.close()
    return df


def ambil_data():
    conn = sq.connect('keuangan.db')

    df = pd.read_sql_query("""
    SELECT tipe, jenis, nominal, waktu
    FROM transaksi
    """, conn)

    # print(df)
    conn.close()
    return df


def seluruh_saldo():
    df = ambil_data()
    total_pemasukkan = df.loc[df['tipe'] == 'pemasukkan', 'nominal'].sum()
    total_pengeluaran = df.loc[df['tipe'] == 'pengeluaran', 'nominal'].sum()

    saldo = total_pemasukkan - total_pengeluaran
    print(f'saldo: {saldo}')
    return f"Rp{saldo:,}".replace(",", ".")


def tampilkan_total_pemasukkan():
    df = ambil_data()

    total = df.loc[df['tipe'] == 'pemasukkan', 'nominal'].sum()

    # ! TERJADI PEMANGGILAN 2 KALI DI FUNCTION INI, DAN FUNCTION SEJENISNYA
    return f"Total: Rp{total:,}".replace(",", ".")


def tampilkan_total_pengeluaran():
    df = ambil_data()

    total = df.loc[df['tipe'] == 'pengeluaran', 'nominal'].sum()

    return f"Total: Rp{total:,}".replace(",", ".")


def tampilkan_tipe(tipe):
    df = ambil_data()

    tampilkan = df.loc[df['tipe'] == tipe]

    return tampilkan


def tampilkan_nominal(tipe):
    df = ambil_data()
    total = df.loc[df['tipe'] == tipe, 'nominal']

    return total


def tampilkan_waktu(tipe):
    df = ambil_data()
    waktu = df.loc[df['tipe'] == tipe, 'waktu']

    return waktu
