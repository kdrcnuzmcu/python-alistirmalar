class OBS:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, aldigiDersler):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.aldigiDersler = aldigiDersler
        self.dersler = {}
        self.notlar = {}
        for ders in self.aldigiDersler:
            self.dersler.update({ders: {"Vize" : True,
                                        "Final" : True,
                                        "Laboratuvar" : False,
                                        "Sinav" : False}})
            self.notlar.update({ders: 0})
    def NotHesapla(self, ders):
        ortalama = 0
        for i, j in self.dersler.items():
            if i == ders:
                for x, y in j.items():
                    if y == True:
                        notu = float(input("{} notunu giriniz: ".format(x)))
                        agirlik = float(input("{} agirligi giriniz: ".format(x)))
                        ortalama += (notu * agirlik)
                self.NotSistemi(ortalama)
                self.notlar[ders] = ortalama
    def NotSistemi(self, ortalama):
        if ortalama >= 90:
            print("AA -", ortalama)
        elif ortalama < 90 and ortalama >= 80:
            print("BA -", ortalama)
        elif ortalama < 80 and ortalama >= 70:
            print("BB -", ortalama)
        elif ortalama < 70 and ortalama >= 60:
            print("CB -", ortalama)
        elif ortalama < 60 and ortalama >= 50:
            print("CC -", ortalama)
        elif ortalama < 50 and ortalama >= 40:
            print("DC -", ortalama)
        elif ortalama < 40 and ortalama >= 30:
            print("DD -", ortalama)
        elif ortalama < 30 and ortalama >= 20:
            print("FD -", ortalama)
        else:
            print("FF -", ortalama)

yeniOgrenci = OBS("Kadir Can", "UZUMCU", ["Matematik", "Ingilizce", "Fizik"])
yeniOgrenci.dersler["Ingilizce"]["Sinav"] = True
yeniOgrenci.dersler["Fizik"]["Laboratuvar"] = True
yeniOgrenci.NotHesapla("Matematik")
yeniOgrenci.NotHesapla("Fizik")

yeniOgrenci.notlar

