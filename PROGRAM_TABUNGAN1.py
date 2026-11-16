import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_SALDO = "data_tabungan.json"
FILE_RIWAYAT = "riwayat_tabungan.json"

dompet_default = {
    "OVO": 0,
    "DANA": 0,
    "GoPay": 0,
    "Tunai": 0
}

def baca_json(file, default):
    if os.path.exists(file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            return default.copy()
    return default.copy()

saldo = baca_json(FILE_SALDO, dompet_default)
riwayat = baca_json(FILE_RIWAYAT, [])

def simpan():
    with open(FILE_SALDO, "w") as f:
        json.dump(saldo, f, indent=4)
    with open(FILE_RIWAYAT, "w") as f:
        json.dump(riwayat, f, indent=4)

def rupiah(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")

def perbarui():
    total = sum(saldo.values())
    label_total.config(text=rupiah(total))

    for nama in saldo:
        kartu[nama].config(text=rupiah(saldo[nama]))

    for item in tabel.get_children():
        tabel.delete(item)

    for transaksi in reversed(riwayat):
        tabel.insert("", "end", values=(
            transaksi["jenis"],
            transaksi["dompet"],
            rupiah(transaksi["jumlah"])
        ))
