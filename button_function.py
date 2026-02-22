from PyQt5.QtWidgets import QFileDialog
class ButonYoneticisi():
    def __init__(self, pencere):
        self.pencere = pencere
        self.motor= self.pencere.motor
    def efekt_uygula(self):
        if self.motor.orijinal_resim:
            siddet = self.pencere.ayar_cubugu.value()
            secili_efekt = self.pencere.efekt_grubu.checkedId()
            if secili_efekt == 1:
                self.glitch(siddet)
            elif secili_efekt == 2:
                self.blur(siddet)
            elif secili_efekt == 3:
                self.grayscale(siddet)
    
    # DOSYA İSLEMLERİ
    def yukle(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self.pencere, "Bir Resim Seç", "", "Resimler (*.png *.jpg *.jpeg)")
        if dosya_yolu:
            pil_resmi = self.motor.resim_yukle(dosya_yolu)
            bilgiler = self.motor.resim_bilgiler()
            self.pencere.resim_guncelleme(pil_resmi)
            self.pencere.bilgi_etiketi.setText(f"Çözünürlük: {bilgiler['resolution'][0]}x{bilgiler['resolution'][1]} Format: {bilgiler['format']} Mod: {bilgiler['mode']}")

    def kaydet(self):
        if self.motor.orijinal_resim:
            dosya_yolu, _ = QFileDialog.getSaveFileName(self.pencere, "Kaydedilcek Yolu Seçin", "","PNG Formatı (*.png);;JPEG Formatı (*.jpg *.jpeg)")
            if dosya_yolu:
                self.motor.resim_kaydet(dosya_yolu)
    def uygula(self):
        if self.motor.orijinal_resim:
            self.motor.orijinal_resim = self.motor.guncel_resim.copy()
            self.pencere.ayar_cubugu.setValue(0)

    def sifirla(self):
        if self.motor.orijinal_resim:
            self.motor.orijinal_resim = self.motor.ilk_resim.copy()
            self.motor.guncel_resim = self.motor.ilk_resim.copy()
            self.pencere.ayar_cubugu.setValue(0)
            self.pencere.resim_guncelleme(self.motor.orijinal_resim)

    # EFEKTLER 
    def glitch(self, siddet):
        retro_resim = self.motor.glitch_efekti(siddet)
        self.pencere.resim_guncelleme(retro_resim)

    def blur(self, siddet):
        blur_resim = self.motor.blur_efekti(siddet)
        self.pencere.resim_guncelleme(blur_resim)
    
    def grayscale(self, siddet):
        grayscale_resim = self.motor.grayscale_efekti(siddet)
        self.pencere.resim_guncelleme(grayscale_resim)