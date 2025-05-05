import tkinter as tk
from tkinter import ttk
from pyswip import Prolog
from tkinter import messagebox

prolog = Prolog()
prolog.consult("pakar_deteksi_gui.pl")

jenis_kulit = []
ciri = {}
index_jenis_kulit = 0
index_ciri = -1
current_jenis_kulit = ""
current_ciri = ""

def mulai_deteksi():
    global jenis_kulit, ciri, index_jenis_kulit, index_ciri
    
    prolog.retractall("ciri_pos(_)")  
    prolog.retractall("ciri_neg(_)") 
    
    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)
    
    jenis_kulit.clear()
    ciri.clear()
    
    jenis_kulit = [p["X"].decode() for p in list(prolog.query("jenis_kulit(X)"))]
    
    for p in jenis_kulit:
        ciri[p] = [g["X"] for g in list(prolog.query(f"ciri(X,\"{p}\")"))]
    
    index_jenis_kulit = 0
    index_ciri = -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_jenis_kulit=False):
    global current_jenis_kulit, current_ciri, index_jenis_kulit, index_ciri

    if ganti_jenis_kulit:
        index_jenis_kulit += 1
        index_ciri = -1

    if index_jenis_kulit >= len(jenis_kulit):
        hasil_deteksi()
        return
    
    current_jenis_kulit = jenis_kulit[index_jenis_kulit]
    index_ciri += 1

    if index_ciri >= len(ciri[current_jenis_kulit]):
        pertanyaan_selanjutnya(ganti_jenis_kulit=True)
        return

    current_ciri = ciri[current_jenis_kulit][index_ciri]

    if list(prolog.query(f"ciri_pos({current_ciri})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"ciri_neg({current_ciri})")):
        pertanyaan_selanjutnya()
        return

    pertanyaan = list(prolog.query(f"pertanyaan({current_ciri},Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"ciri_pos({current_ciri})")
    else:
        prolog.assertz(f"ciri_neg({current_ciri})")
    
    pertanyaan_selanjutnya()

def hasil_deteksi():
    hasil = list(prolog.query("terdeteksi(Jenis)"))
    if hasil:
        jenis = hasil[0]["Jenis"].decode()
        messagebox.showinfo("Hasil Deteksi", f"Jenis kulit Anda adalah: {jenis}")
    else:
        messagebox.showinfo("Hasil Deteksi", "Jenis kulit wajah tidak terdeteksi.")
    
    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

root = tk.Tk()
root.title("Sistem Pakar Diagnosis Jenis Kulit")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Deteksi Jenis Kulit Wajah",
          font=("Arial", 16)).grid(column=0, row=0, columnspan=3)

ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Deteksi", command=mulai_deteksi)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
