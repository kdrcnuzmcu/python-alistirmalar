class SayiTahminOyunu():
    from random import randint
    from time import sleep

    def Basla(self):
        print("1 ile 100 arasında bir sayi tuttum. Bu sayiyi tahmin edebilecek misin?")
        self.sayi = self.randint(1, 100)
        self.count = 0
        self.tahminler = []
        self.Tahmin()
    def Tahmin(self):
        while self.count < 5:
            try:
                tahmin = int(input("Tahmin et!"))
                if tahmin < 1 or tahmin > 100:
                    print("Lütfen 1 ile 100 arasında bir tamsayi gir.")
                    continue
            except:
                print("Lütfen 1 ile 100 arasında bir tamsayi gir.")
                continue

            if tahmin in self.tahminler:
                self.Monitor("FARKLI BIR SAYI TAHMIN ET!")
                self.sleep(1)
                continue
            else:
                self.tahminler.append(tahmin)
                self.count += 1
                if tahmin == self.sayi:
                    self.Monitor("TEBRIKLER!")
                    self.count = 5
                else:
                    self.Monitor("YENIDEN DENE!")
                self.sleep(1)
        print("""
        --- * --- * --- * --- * --- * ---
        SAYI: {}
        --- * --- * --- * --- * --- * ---
        """.format(self.sayi))
    def Monitor(self, metin):
        print("""
            --- * --- * --- * --- * --- * ---
            {}

            Tahmin Ettiklerin: {}
            --- * --- * --- * --- * --- * ---
            """.format(metin, self.tahminler))

Oyun = SayiTahminOyunu()
Oyun.Basla()