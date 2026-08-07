import streamlit as st
import pandas as pd
from tracker import (tarckerPemasukkan, tarckerPengeluaran)
from database import (buat_tabel,
                      cek_tabel,
                      ambil_data,
                      filter_tracker_7day,
                      filter_tracker_3day,
                      filter_tracker_10day,
                      filter_tracker_30day,
                      tampilkan_list,
                      tampilkan_total_pemasukkan,
                      tampilkan_total_pengeluaran,
                      seluruh_saldo,
                      tampilkan_tipe,
                      tampilkan_nominal,
                      tampilkan_waktu)
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
                    cek_tabel()
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
                except Exception as e:
                    st.write(e)
            else:
                st.write('masukkan nominal dan jenis')
# TAMPILAN SELURUH SALDO
with st.container(gap='small', border=True):
    st.subheader(f'saldo: {seluruh_saldo()}')
# DASHBOARD SEMUA INPUTAN
with st.container(gap='small', border=True):
    with st.expander('liat semua'):
        st.dataframe(ambil_data())
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
        df = pd.DataFrame({'waktu': tampilkan_waktu('pemasukkan'),
                           'nominal': tampilkan_nominal('pemasukkan')})
        df['waktu'] = pd.to_datetime(df['waktu'])
        df = df.sort_values('waktu', ascending=True)

        # df = df.set_index('waktu')
        st.line_chart(df, x='waktu', y='nominal')


with st.container(gap='small', border=True):
    with st.expander('analisis pengeluaran'):
        df = pd.DataFrame({'waktu': tampilkan_waktu('pengeluaran'),
                           'nominal': tampilkan_nominal('pengeluaran')})
        df['waktu'] = pd.to_datetime(df['waktu'])
        df = df.sort_values('waktu', ascending=True)
        # df = df.set_index('waktu')
        st.line_chart(df, x='waktu', y='nominal')
# BISA CEK ATAU MILIH HARI APA SEBELUMNYA
with st.container(gap='small', border=True):
    with st.expander('sorter day'):
        if st.button('sorted 3 day'):
            st.dataframe(filter_tracker_3day())
        if st.button('sorted 7 day'):
            st.dataframe(filter_tracker_7day())
        if st.button('sorted 10 day'):
            st.dataframe(filter_tracker_10day())
        if st.button('sorted 30 day'):
            st.dataframe(filter_tracker_30day())
        # DOWNLOAD EXCEL SEMUA INPUTAN
with st.container(gap='small', border=True):
    with st.expander('download excel'):
        data_excel = 'open_tracker_data.xlsx'
        tampilkan_list().to_excel(data_excel)

        with open(data_excel, 'rb') as f:
            st.download_button('download excel semua data', data=f, file_name='data_excel.xlsx',
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


# APLIKASI PENCATATAN KEUANGAN DENGAN MUDAH DAN MEMILIKI ANALISIS
