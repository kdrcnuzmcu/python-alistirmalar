# Bu fonksiyon gireceginiz kelimeyi veya cumleyi tersine cevirir.

def TersCevirici(metin):
    return metin[::-1]

metin = str(input("Metin giriniz:"))

print(TersCevirici(metin))