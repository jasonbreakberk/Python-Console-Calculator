import tkinter as tk

# GLOBAL DEĞİŞKEN: Ekrandaki mevcut ifadeyi tutar
mevcut_ifade = ""

# =======================================================
# 1. FONKSİYONLAR
# =======================================================

def buton_bas(deger):
    """Butona basıldığında değeri ekrana ekler."""
    global mevcut_ifade
    mevcut_ifade = mevcut_ifade + str(deger)
    # Ekranı temizle ve yeni ifadeyi yaz
    gosterge_alani.delete(0, tk.END)
    gosterge_alani.insert(0, mevcut_ifade)

def temizle():
    """Ekranı ve global ifadeyi temizler."""
    global mevcut_ifade
    mevcut_ifade = ""
    gosterge_alani.delete(0, tk.END)

def hesapla():
    """Mevcut ifadeyi değerlendirir ve sonucu ekranda gösterir."""
    global mevcut_ifade
    try:
        # Python'ın 'eval' fonksiyonu ile matematiksel ifadeyi hesapla
        sonuc = str(eval(mevcut_ifade))
        
        # Sonucu ekrana yaz ve yeni ifadeyi sonuç yap
        gosterge_alani.delete(0, tk.END)
        gosterge_alani.insert(0, sonuc)
        mevcut_ifade = sonuc
        
    except Exception:
        # Hata durumunda (örn. sıfıra bölme)
        temizle()
        gosterge_alani.insert(0, "Hata")
        mevcut_ifade = ""


# =======================================================
# 2. ARABİRİM (GUI) OLUŞTURMA
# =======================================================

# Ana Pencere (Root)
pencere = tk.Tk()
pencere.title("Hesap Makinesi")

# !!! BURAYI DÜZELTTİK: Pencere boyutunu küçülttük
pencere.geometry("300x320") 
pencere.resizable(False, False) 

# Görüntüleme Alanı (Ekran)
gosterge_alani = tk.Entry(pencere, width=16, font=('Arial', 20), bd=5, relief=tk.GROOVE, justify='right')
# Ekranı pencereye yerleştirme
gosterge_alani.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# =======================================================
# 3. BUTONLARI TANIMLAMA VE YERLEŞTİRME
# =======================================================

# Butonların Metinleri ve Grid Yerleşimleri
butonlar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# !!! BURAYI DÜZELTTİK: Butonların temel boyutlarını küçülttük
sutun_genisligi = 3
satir_yuksekligi = 1

# Butonları oluşturma ve yerleştirme döngüsü
for (text, row, col) in butonlar:
    action = None
    if text == 'C':
        action = temizle
    elif text == '=':
        action = hesapla
    else:
        # Rakamlar ve işlemler için buton_bas fonksiyonunu kullan
        action = lambda t=text: buton_bas(t)
    
    btn = tk.Button(
        pencere, 
        text=text, 
        font=('Arial', 14),
        command=action, # Butona tıklandığında çalışacak fonksiyon
        height=satir_yuksekligi, 
        width=sutun_genisligi, 
    )
    
    # Özel durum: Eşittir (=) butonu 4 sütun kaplasın
    if text == '=':
        btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=5, pady=5)
    else:
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Pencerenin ana döngüsü
pencere.mainloop()