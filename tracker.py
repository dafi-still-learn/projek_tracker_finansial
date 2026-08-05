from formatter import (formatListPemasukkan, formatListPengeluaran)
from database import tambah_item


class tarckerPemasukkan:
    def __init__(self):
        self.list_pemasukkan = []

    def input_pemasukkan(self, pemasukkan, jenis):
        data_list = formatListPemasukkan(pemasukkan, jenis)
        self.list_pemasukkan.append(data_list)
        self.pemasukkan = pemasukkan
        self.pemasukkan_jenis = jenis

    def tampilkan(self):
        items = {}

        items['nominal'] = self.pemasukkan
        items['jenis'] = self.pemasukkan_jenis

        print(f"pemasukkan: {items['nominal']}")
        print(f"jenis pemasukkan: {items['jenis']}")

    def tampilkan_semua(self):
        for items in self.list_pemasukkan:
            tambah_item(
                items['tipe'], items['jenis'], items['nominal'], items['waktu'] + ", " + items['jam'])

    def hapus(self):
        self.list_pemasukkan.clear()
        print("list sudah kosong")


class tarckerPengeluaran:
    def __init__(self):
        self.list_pengeluaran = []

    def input_pengeluaran(self, pengeluaran, jenis):
        data_list = formatListPengeluaran(
            pengeluaran, jenis)
        self.list_pengeluaran.append(data_list)

        self.pengeluaran = pengeluaran
        self.jenis_pengeluaran = jenis

    def tampilkan(self):
        items = {}

        items['nominal'] = self.pengeluaran
        items['jenis'] = self.jenis_pengeluaran

        print(f"pengeluaran: {items['pengeluaran']}")
        print(f"jenis pengeluaran: {items['jenis']}")

    def tampilkan_semua(self):
        for items in self.list_pengeluaran:
            tambah_item(
                "pengeluaran", items['jenis'], items['nominal'], items['waktu'] + ", " + items['jam'])

    def hapus(self):
        self.list_pengeluaran.clear()
        print("list sudah kosong")
