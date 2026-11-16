def tambah_transaksi():
    jenis = pilihan_jenis.get()
    dompet = pilihan_dompet.get()
    jumlah_teks = input_jumlah.get()

    try:
        jumlah = int(jumlah_teks)
        if jumlah <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Kesalahan", "Masukkan jumlah uang yang benar!")
        return

    if jenis == "Uang Keluar" and saldo[dompet] < jumlah:
        messagebox.showerror("Saldo Kurang", "Saldo dompet tidak mencukupi!")
        return

    if jenis == "Uang Masuk":
        saldo[dompet] += jumlah
    else:
        saldo[dompet] -= jumlah

    riwayat.append({
        "jenis": jenis,
        "dompet": dompet,
        "jumlah": jumlah
    })

    simpan()
    input_jumlah.delete(0, tk.END)
    perbarui()
    messagebox.showinfo("Berhasil", "Transaksi berhasil disimpan!")

def hapus_transaksi():
    pilihan = tabel.selection()
    if not pilihan:
        messagebox.showwarning("Pilih Data", "Pilih transaksi yang ingin dihapus!")
        return

    indeks = tabel.index(pilihan[0])
    transaksi = riwayat[len(riwayat) - 1 - indeks]

    if transaksi["jenis"] == "Uang Masuk":
        saldo[transaksi["dompet"]] -= transaksi["jumlah"]
    else:
        saldo[transaksi["dompet"]] += transaksi["jumlah"]
