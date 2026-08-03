
def kondisi_uang(uang_pemasukkan, uang_pengeluaran):
    total_pemasukkan = sum(item['nominal'] for item in uang_pemasukkan)

    total_pengeluaran = sum(item['nominal'] for item in uang_pengeluaran)

    total = total_pemasukkan - total_pengeluaran

    return {
        'pemasukkan': total_pemasukkan,
        'pengeluaran': total_pengeluaran,
        'saldo': total
    }


def format_rupiah(angka):
    return f"Rp{angka:,}".replace(",", ".")
