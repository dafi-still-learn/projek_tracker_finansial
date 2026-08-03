
def semua_dashboard(pemasukkan, pengeluaran):
    semua_data = []

    semua_data.append(pemasukkan.list_pemasukkan)
    semua_data.append(pengeluaran.list_pengeluaran)

    return semua_data


def pemasukkan_dashboard(pemasukkan):
    return pemasukkan.list_pemasukkan


def pengeluaran_dashboard(pengeluaran):
    return pengeluaran.list_pengeluaran
