    # Basit Konsol Tabanlı Hesap Makinesi

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Hata: Sıfıra bölme yapılamaz!"
    return x / y

print("Yapılacak işlemi seçiniz.")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    # Kullanıcıdan seçim yapmasını iste
    secim = input("Seçiminizi girin (1/2/3/4): ")

    # Seçimin geçerli olup olmadığını kontrol et
    if secim in ('1', '2', '3', '4'):
        try:
            sayi1 = float(input("İlk sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Geçersiz giriş. Lütfen sayı girin.")
            continue

        if secim == '1':
            print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))

        elif secim == '2':
            print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))

        elif secim == '3':
            print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))

        elif secim == '4':
            sonuc = bolme(sayi1, sayi2)
            print(sayi1, "/", sayi2, "=", sonuc)
        
        # Kullanıcıya devam etmek isteyip istemediğini sor
        devam = input("Başka bir işlem yapmak ister misiniz? (evet/hayır): ")
        if devam.lower() != "evet":
            break

    else:
        print("Geçersiz Seçim")