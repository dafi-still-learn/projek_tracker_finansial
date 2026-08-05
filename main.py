import streamlit as st
from tracker import (tarckerPemasukkan, tarckerPengeluaran)
from database import (buat_tabel,
                      tampilkan_list,
                      tampilkan_total_pemasukkan,
                      tampilkan_total_pengeluaran,
                      seluruh_saldo,
                      tampilkan_tipe,
                      tampilkan_nominal)

buat_tabel()

menjalankan_app_pemasukkan = tarckerPemasukkan()
menjalankan_app_pengeluaran = tarckerPengeluaran()

# NAMA APLIKASI
st.title("Tracker Finansial")
# INPUT PEMASUKKAN
with st.container(gap='small', border=True):
    with st.form('form pemasukkan', clear_on_submit=True):
        st.subheader('pemasukkan')
        input_pemasukkan = st.text_input('nominal pemasukkan')
        input_jenis_pemasukkan = st.text_input('jenis pemasukkan')

        submit = st.form_submit_button('kirim pemasukkan')
        if submit:
            if input_pemasukkan and input_jenis_pemasukkan:
                try:
                    input_pemasukkan = int(input_pemasukkan)
                    menjalankan_app_pemasukkan.input_pemasukkan(
                        input_pemasukkan, input_jenis_pemasukkan)

                    menjalankan_app_pemasukkan.tampilkan_semua()
                    print(seluruh_saldo())

                except Exception as e:
                    st.write(e)
            else:
                st.write('masukkan nominal dan jenis')
# INPUT PENGELUARAN
with st.container(gap='small', border=True):
    with st.form('form pengeluaran', clear_on_submit=True):
        st.subheader('Pengeluaran')
        input_pengeluaran = st.text_input('nominal pengeluaran')
        input_jenis_pengeluaran = st.text_input('jenis pengeluaran')

        submit = st.form_submit_button('kirim pengeluaran')
        if submit:
            if input_pengeluaran and input_jenis_pengeluaran:
                try:
                    input_pengeluaran = int(input_pengeluaran)
                    menjalankan_app_pengeluaran.input_pengeluaran(
                        input_pengeluaran, input_jenis_pengeluaran)

                    menjalankan_app_pengeluaran.tampilkan_semua()
                    print(seluruh_saldo())

                    tampilkan_list()
                # st.rerun()
                except Exception as e:
                    st.write(e)
            else:
                st.write('masukkan nominal dan jenis')
# TAMPILAN SELURUH SALDO
with st.container(gap='small', border=True):
    st.subheader(seluruh_saldo())
# DASHBOARD SEMUA INPUTAN
with st.container(gap='small', border=True):
    with st.expander('liat semua'):
        st.dataframe(tampilkan_list())
        st.write(f'total: {seluruh_saldo()}')
# DASHBOARD PEMASUKKAN
with st.container(gap='small', border=True):
    with st.expander('liat pemasukkan'):
        st.dataframe(tampilkan_tipe('pemasukkan'))

        st.write(tampilkan_total_pemasukkan())

# DASHBOARD PENGELUARAN
with st.container(gap='small', border=True):
    with st.expander('liat pengeluaran'):
        st.dataframe(tampilkan_tipe('pengeluaran'))
        st.write(tampilkan_total_pengeluaran())

# ANALISIS DIAGRAM ATAU CHART
with st.container(gap='small', border=True):
    with st.expander('analisis pemasukkan'):
        st.line_chart(tampilkan_nominal('pemasukkan'))
        pass
with st.container(gap='small', border=True):
    with st.expander('analisis pengeluaran'):
        st.line_chart(tampilkan_nominal('pengeluaran'))
        pass
    # BISA CEK ATAU MILIH HARI APA SEBELUMNYA
    # DOWNLOAD EXCEL SEMUA INPUTAN
with st.container(gap='small', border=True):
    with st.expander('download excel'):
        pass


# APLIKASI PENCATATAN KEUANGAN DENGAN MUDAH DAN MEMILIKI ANALISIS
