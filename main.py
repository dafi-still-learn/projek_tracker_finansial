import streamlit as st
import pandas as pd
from kondisi_uang import (kondisi_uang, format_rupiah)
from tracker import (tarckerPemasukkan, tarckerPengeluaran)
from dashboard import (
    semua_dashboard, pemasukkan_dashboard, pengeluaran_dashboard)
from database import (buat_tabel, tampilkan_list,
                      tampilkan_total_pemasukkan,
                      tampilkan_total_pengeluaran,
                      ambil_data,
                      seluruh_saldo,
                      tampilkan_tipe,
                      tampilkan_nominal)

if 'tracker_pemasukkan' not in st.session_state:
    st.session_state.tracker_pemasukkan = tarckerPemasukkan()

if 'tracker_pengeluaran' not in st.session_state:
    st.session_state.tracker_pengeluaran = tarckerPengeluaran()


menjalankan_app_pemasukkan = st.session_state.tracker_pemasukkan
menjalankan_app_pengeluaran = st.session_state.tracker_pengeluaran

# NAMA APLIKASI
st.title("Tracker Finansial")
# REAL TIME KONDISI UANG
with st.container(gap='small', border=True):

    st.subheader(seluruh_saldo())
    # realtime_uang = kondisi_uang(
    #     menjalankan_app_pemasukkan.list_pemasukkan, menjalankan_app_pengeluaran.list_pengeluaran)
    # st.subheader(format_rupiah(realtime_uang['saldo']))
# st.subheader(items['pemasukkan'] + items['pengeluaran'])
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

                    tampilkan_list()
                    st.rerun()
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

                    tampilkan_list()
                    st.rerun()
                except Exception as e:
                    st.write(e)
            else:
                st.write('masukkan nominal dan jenis')
# DASHBOARD SEMUA INPUTAN
with st.container(gap='small', border=True):
    with st.expander('liat semua'):
        for items in semua_dashboard(menjalankan_app_pemasukkan,
                                     menjalankan_app_pengeluaran):
            st.dataframe(items)
# DASHBOARD PEMASUKKAN
with st.container(gap='small', border=True):
    with st.expander('liat pemasukkan'):
        st.dataframe(tampilkan_tipe('pemasukkan'))
        tampilkan_total_pemasukkan()

        st.write(tampilkan_total_pemasukkan())
        # st.dataframe(ambil_data())
# DASHBOARD PENGELUARAN
with st.container(gap='small', border=True):
    with st.expander('liat pengeluaran'):
        st.dataframe(tampilkan_tipe('pengeluaran'))
        st.write(tampilkan_total_pengeluaran())
        # df = pd.DataFrame(pengeluaran_dashboard(menjalankan_app_pengeluaran))
        # if not df.empty:
        #     print('tes tidak kosong')
        # else:
        #     print(df.columns.tolist())
        #     # total = df['nominal'].sum()
        #     # df.loc[len(df)] = {
        #     #     'pengeluaran': total,
        #     #     'jenis': "TOTAL"
        #     # }
        # st.dataframe(df)
        # pass
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

buat_tabel()
# APLIKASI PENCATATAN KEUANGAN DENGAN MUDAH DAN MEMILIKI ANALISIS
