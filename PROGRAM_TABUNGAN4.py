kartu[nama] = tk.Label(
        frame, text="Rp0",
        font=("Arial", 12, "bold"),
        bg="white", fg="#2563eb"
    )
    kartu[nama].pack(pady=5)

# FORM TRANSAKSI
form = tk.LabelFrame(
    root, text="Catat Transaksi",
    font=("Arial", 12, "bold"),
    bg="#f1f5f9", padx=15, pady=12
)
form.pack(fill="x", padx=30, pady=10)

pilihan_jenis = tk.StringVar(value="Uang Masuk")
pilihan_dompet = tk.StringVar(value="DANA")

tk.Label(form, text="Jenis:", bg="#f1f5f9").grid(row=0, column=0, padx=5)
ttk.Combobox(
    form, textvariable=pilihan_jenis,
    values=["Uang Masuk", "Uang Keluar"],
    state="readonly", width=15
).grid(row=0, column=1, padx=5)

tk.Label(form, text="Dompet:", bg="#f1f5f9").grid(row=0, column=2, padx=5)
ttk.Combobox(
    form, textvariable=pilihan_dompet,
    values=list(saldo.keys()),
    state="readonly", width=12
).grid(row=0, column=3, padx=5)

tk.Label(form, text="Jumlah Rp:", bg="#f1f5f9").grid(row=0, column=4, padx=5)
input_jumlah = tk.Entry(form, width=13)
input_jumlah.grid(row=0, column=5, padx=5)

tk.Button(
    form, text="Simpan Transaksi",
    command=tambah_transaksi,
    bg="#2563eb", fg="white",
    padx=10
).grid(row=1, column=1, columnspan=3, pady=12)

# TABEL RIWAYAT
tk.Label(
    root, text="Riwayat Transaksi",
    font=("Arial", 14, "bold"),
    bg="#f1f5f9"
).pack(pady=8)

tabel = ttk.Treeview(
    root,
    columns=("jenis", "dompet", "jumlah"),
    show="headings", height=9
)

tabel.heading("jenis", text="Jenis Transaksi")
tabel.heading("dompet", text="Dompet")
tabel.heading("jumlah", text="Jumlah")

tabel.column("jenis", width=200, anchor="center")
tabel.column("dompet", width=200, anchor="center")
tabel.column("jumlah", width=200, anchor="center")
tabel.pack(padx=30, fill="x")

tk.Button(
    root, text="Hapus Transaksi Terpilih",
    command=hapus_transaksi,
    bg="#dc2626", fg="white",
    padx=10
).pack(pady=12)

perbarui()
root.mainloop()
