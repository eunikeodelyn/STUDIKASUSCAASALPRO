import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# Daftar menu beserta harga
menu_harga = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Bakar": 20000,
    "Ikan Goreng": 18000
}

def pesan_makanan():
    # Dapatkan nilai dari inputan pengguna
    nama_pelanggan = entry_nama.get()
    menu_pilihan = combo_menu.get()
    jumlah_pesanan = spin_jumlah.get()

    # Validasi input
    if not nama_pelanggan or not menu_pilihan or jumlah_pesanan == 0:
        tk.messagebox.showwarning("Peringatan", "Harap isi semua kolom dengan benar!")
        return

    # Harga per satu porsi menu
    harga_per_porsi = menu_harga.get(menu_pilihan, 0)

    # Perhitungan total harga
    total_harga = int(jumlah_pesanan) * harga_per_porsi

    # Tambahkan pesanan ke tabel
    tree.insert("", "end", values=(nama_pelanggan, menu_pilihan, jumlah_pesanan, harga_per_porsi, total_harga))

    # Reset nilai input
    entry_nama.delete(0, tk.END)
    combo_menu.set("")
    spin_jumlah.set(0)

    # Hitung total harga dan perbarui label
    hitung_total()

def hitung_total():
    total = sum(int(tree.item(item, 'values')[-1]) for item in tree.get_children())
    label_total.config(text=f"Total Harga: {total} IDR")


def close():
    response=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()

# Membuat instance Tkinter
root = tk.Tk()
root.title("Program Pemesanan Makanan")

# Label dan Entry untuk Nama Pelanggan
label_nama = tk.Label(root, text="Nama Pelanggan:")
label_nama.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Label dan Combobox untuk Menu Pilihan
label_menu = tk.Label(root, text="Menu Pilihan:")
label_menu.grid(row=1, column=0, padx=10, pady=10, sticky="e")

menu_options = list(menu_harga.keys())
combo_menu = ttk.Combobox(root, values=menu_options)
combo_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Label dan Spinbox untuk Jumlah Pesanan
label_jumlah = tk.Label(root, text="Jumlah Pesanan:")
label_jumlah.grid(row=2, column=0, padx=10, pady=10, sticky="e")

spin_jumlah = tk.Spinbox(root, from_=0, to=10)
spin_jumlah.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Tombol Pesan
button_pesan = tk.Button(root, text="Pesan", command=pesan_makanan)
button_pesan.grid(row=3, column=0, columnspan=2, pady=20)

# Tabel untuk Menampilkan Pesanan
columns = ["Nama Pelanggan", "Menu Pilihan", "Jumlah Pesanan", "Harga per Porsi", "Total Harga"]
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.grid(row=4, column=0, columnspan=2, padx=10)

# Label untuk Menampilkan Total Harga
label_total = tk.Label(root, text="Total Harga: 0 IDR", font=("Helvetica", 12))
label_total.grid(row=5, column=0, columnspan=2, pady=10)

# Tombol Hitung Total
button_hitung_total = tk.Button(root, text="Hitung Total", command=hitung_total)
button_hitung_total.grid(row=6, column=0, columnspan=2, pady=10)

button_keluar = tk.Button(root, text="Exit", command=close)
button_keluar.grid(row=7, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop()
