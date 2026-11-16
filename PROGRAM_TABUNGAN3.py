riwayat.pop(len(riwayat) - 1 - indeks)
    simpan()
    perbarui()

    messagebox.showinfo("Berhasil", "Transaksi dihapus!")

# JENDELA UTAMA
root = tk.Tk()
root.title("Program Tabungan")
root.geometry("850x650")
root.configure(bg="#f1f5f9")

judul = tk.Label(
    root, text="PROGRAM TABUNGAN",
    font=("Arial", 22, "bold"),
    bg="#f1f5f9", fg="#172554"
)
judul.pack(pady=15)

tk.Label(
    root, text="Total Seluruh Tabungan",
    font=("Arial", 12), bg="#f1f5f9"
).pack()

label_total = tk.Label(
    root, text="Rp0",
    font=("Arial", 28, "bold"),
    fg="#2563eb", bg="#f1f5f9"
)
label_total.pack(pady=5)

# KARTU DOMPET
frame_kartu = tk.Frame(root, bg="#f1f5f9")
frame_kartu.pack(pady=15)

kartu = {}

for nama in saldo:
    frame = tk.Frame(
        frame_kartu, bg="white",
        padx=20, pady=12,
        highlightbackground="#cbd5e1",
        highlightthickness=1
    )
    frame.pack(side="left", padx=7)

    tk.Label(
        frame, text=nama,
        font=("Arial", 11, "bold"),
        bg="white"
    ).pack()
