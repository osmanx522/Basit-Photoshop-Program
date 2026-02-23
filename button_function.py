from PyQt5.QtWidgets import QFileDialog
class ButonYoneticisi():
    def __init__(self, pencere):
        self.pencere = pencere
        self.motor= self.pencere.motor

    def efekt_uygula(self):
        ''' Bu fonksiyon gui.py de bulunan ayara cubugundan gelen veriyi ve secili efekti
            motora iletir ve uygular.'''
        if self.motor.orijinal_resim:
            siddet = self.pencere.ayar_cubugu.value()
            secili_efekt = self.pencere.efekt_grubu.checkedId()
            if secili_efekt in self.motor.effect_manager:
                resim = self.motor.effect_manager[secili_efekt](siddet)
                self.pencere.resim_guncelleme(resim)

    # DOSYA İSLEMLERİ
    def yukle(self):
        '''Dosyayı yükleme penceresini açar ve motora dosya yolunu iletir.
            Motordan dönene dosyayı ekrana gösterir ve bilgilerini yazdırır.'''
        dosya_yolu, _ = QFileDialog.getOpenFileName(self.pencere, "Bir Resim Seç", "", "Resimler (*.png *.jpg *.jpeg)")
        if dosya_yolu:
            pil_resmi = self.motor.resim_yukle(dosya_yolu)
            bilgiler = self.motor.resim_bilgiler()
            self.pencere.resim_guncelleme(pil_resmi)
            self.pencere.bilgi_etiketi.setText(f"Çözünürlük: {bilgiler['resolution'][0]}x{bilgiler['resolution'][1]} Format: {bilgiler['format']} Mod: {bilgiler['mode']}")

    def kaydet(self):
        '''
        Dosyayı Kaydetmet için kaydetme penceresini oluşturur.
        '''
        if self.motor.orijinal_resim:
            dosya_yolu, _ = QFileDialog.getSaveFileName(self.pencere, "Kaydedilcek Yolu Seçin", "","PNG Formatı (*.png);;JPEG Formatı (*.jpg *.jpeg)")
            if dosya_yolu:
                self.motor.resim_kaydet(dosya_yolu)
    def uygula(self):
        '''
        Uygula butonu için yapılmıştır.
        Yapılan ayarları motordaki orijinal resime eşitler.
        '''
        if self.motor.orijinal_resim:
            self.motor.orijinal_resim = self.motor.guncel_resim.copy()
            self.pencere.ayar_cubugu.setValue(0)

    def sifirla(self):
        '''Yapılan bütün efektleri sıfırlar.'''
        if self.motor.orijinal_resim:
            self.motor.orijinal_resim = self.motor.ilk_resim.copy()
            self.motor.guncel_resim = self.motor.ilk_resim.copy()
            self.pencere.ayar_cubugu.setValue(0)
            self.pencere.resim_guncelleme(self.motor.orijinal_resim)