import tkinter as tk
from tkinter import filedialog, messagebox


def not_kaydet():
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Metin Dosyası", "*.txt")])
    if dosya_yolu:
        try:
            with open(dosya_yolu, "w", encoding="utf-8") as dosya:
                dosya.write(text_area.get("1.0", tk.END))
            messagebox.showinfo("Başarılı", "Not başarıyla kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilemedi: {e}")

def not_ac():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyası", "*.txt")])
    if dosya_yolu:
        try:
            with open(dosya_yolu, "r", encoding="utf-8") as dosya:
                icerik = dosya.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, icerik)
            kelime_say()  # açıldığında da say
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya açılamadı: {e}")

def kelime_say(event=None):
    metin = text_area.get("1.0", tk.END).strip()
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)
    karakter_sayisi = len(metin)
    durum_label.config(text=f"Kelime: {kelime_sayisi} | Karakter: {karakter_sayisi}")

pencere = tk.Tk()
pencere.title("Not Defteri (Kelime Sayarlı)")
pencere.geometry("600x450")


menu_bar = tk.Menu(pencere)
pencere.config(menu=menu_bar)


dosya_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dosya", menu=dosya_menu)
dosya_menu.add_command(label="Aç", command=not_ac)
dosya_menu.add_command(label="Kaydet", command=not_kaydet)
dosya_menu.add_separator()
dosya_menu.add_command(label="Çıkış", command=pencere.quit)


text_area = tk.Text(pencere, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

durum_label = tk.Label(pencere, text="Word: 0 | Char: 0", anchor="w")
durum_label.pack(fill="x")


text_area.bind("<KeyRelease>", kelime_say)

pencere.mainloop()
