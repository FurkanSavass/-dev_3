class Personel:
    def __init__(self, adı, departmanı, çalışma_yılı, maaşı):
        self.adı = adı
        self.departmanı = departmanı
        self.çalışma_yılı = çalışma_yılı
        self.maaşı = maaşı

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adı:", personel.adı)
            print("Departmanı:", personel.departmanı)
            print("Çalışma Yılı:", personel.çalışma_yılı)
            print("Maaşı:", personel.maaşı)
            

    def maaş_zammı(self, personel, zam_oranı):
        print("Personel Adı:",personel.adı)
        personel.maaşı += personel.maaşı* zam_oranı

    def personel_çıkart(self, personel):
        print("\n",personel.adı,"adlı personel çıkartılıyor...")
        self.personel_listesi.remove(personel)



if __name__ == "__main__":
    firma = Firma()

    personel1 = Personel("Furkan", "Oyun Geliştirici", 5, 75000)
    personel2 = Personel("Hilmi", "WEB Geliştirici", 3, 70000)
    personel3 = Personel("Ömer", "İnsan Kaynakları", 6, 40000)

    firma.personel_ekle(personel1)
    firma.personel_ekle(personel2)
    firma.personel_ekle(personel3)

    print("Firma Çalışanları:")
    firma.personel_listele()

    print("\nMaaş Zammı Uygulanıyor...")
    firma.maaş_zammı(personel1, 0.1)  
    print("Yeni maaşı:", personel1.maaşı)

    
    firma.personel_çıkart(personel2)

    print("\nGüncellenmiş Firma Çalışanları:")
    firma.personel_listele()
