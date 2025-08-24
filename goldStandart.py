import tkinter as tk
from tkinter import messagebox
import pandas as pd

df = pd.read_csv("prices.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df["Price"] = df["Price"].astype(str).str.replace(",", "").astype(float)

def hesapla():
    try:
        tarih = entry_tarih.get().strip()
        para = float(entry_para.get().strip())
        tarih_dt = pd.to_datetime(tarih)
        satir = df[df["Date"] == tarih_dt]
        if satir.empty:
            messagebox.showerror("Hata", f"{tarih} için veri bulunamadı.")
            return
        fiyat = float(satir["Price"].values[0])
        gram = para / fiyat
        messagebox.showinfo("Sonuç", f"{tarih} tarihinde {para} TL ≈ {gram:.2f} gram altın ediyordu.")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

root = tk.Tk()
root.title("Altın Hesaplayıcı")

tk.Label(root, text="Tarih (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
entry_tarih = tk.Entry(root)
entry_tarih.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Para (TL):").grid(row=1, column=0, padx=5, pady=5)
entry_para = tk.Entry(root)
entry_para.grid(row=1, column=1, padx=5, pady=5)

btn_hesapla = tk.Button(root, text="Hesapla", command=hesapla)
btn_hesapla.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
