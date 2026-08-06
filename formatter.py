from datetime import datetime

hari = {
    0: "Senin",
    1: "Selasa",
    2: "Rabu",
    3: "Kamis",
    4: "Jumat",
    5: "Sabtu",
    6: "Minggu",
}

bulan = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember"
}


# items_pemasukkan = []
# items_pengeluaran = []


def format_tanggal(date):
    return f"{hari[date.weekday()]} {date.day} {bulan[date.month]} {date.year}"


def format_jam(date):
    return date.strftime("%H:%M")


def formatListPemasukkan(data_pemasukkan, jenis_pemasukkan):
    waktu = datetime.now()
    tipe = 'pemasukkan'
    items = {
        'nominal': data_pemasukkan,
        'tipe': tipe,
        'jenis': jenis_pemasukkan,
        'waktu_database': waktu,
        'waktu': format_tanggal(waktu),
        'jam': format_jam(waktu)
    }

    return items


def formatListPengeluaran(data_pengeluaran, jenis_pengeluaran):
    waktu = datetime.now()
    tipe = 'pengeluaran'
    items = {
        'nominal': data_pengeluaran,
        'tipe': tipe,
        'jenis': jenis_pengeluaran,
        'waktu_database': waktu,
        'waktu': format_tanggal(waktu),
        'jam': format_jam(waktu)
    }

    return items
