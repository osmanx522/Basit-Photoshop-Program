from PyQt5.QtWidgets import QFileDialog

class ButonYoneticisi():
    def __init__(self, pencere):
        self.pencere = pencere
        self.motor = self.pencere.motor

    def efekt_uygula(self):
        """Slider kaydırıldığında anlık (real-time) önizleme yapar."""
        if self.motor.onizleme_resmi:
            siddet = self.pencere.ayar_cubugu.value()
            secili_efekt = self.pencere.efekt_grubu.checkedId()
            
            if secili_efekt in self.motor.effect_manager:
                # Efekti SADECE önizleme resmi üzerinde hesapla (Hızlıdır)
                sonuc = self.motor.effect_manager[secili_efekt](siddet, self.motor.onizleme_resmi)
                self.pencere.resim_guncelleme(sonuc)

    def uygula(self):
        """'Uygula' butonuna basıldığında efekti orijinal yüksek çözünürlüklü resme işler."""
        if self.motor.orijinal_resim:
            siddet = self.pencere.ayar_cubugu.value()
            secili_efekt = self.pencere.efekt_grubu.checkedId()
            
            if secili_efekt in self.motor.effect_manager:
                # 1. Efekti orijinal büyük resme uygula (Kalıcı hale getir)
                self.motor.orijinal_resim = self.motor.effect_manager[secili_efekt](siddet, self.motor.orijinal_resim)
                
                # 2. Yeni halinden yeni bir önizleme katmanı oluştur (Bir sonraki efekt için)
                self.motor.onizleme_resmi = self.motor.orijinal_resim.copy()
                self.motor.onizleme_resmi.thumbnail((800, 600))
                
                # 3. Arayüzü güncelle
                self.pencere.resim_guncelleme(self.motor.onizleme_resmi)
                self.pencere.ayar_cubugu.setValue(50) # Slider'ı nötr noktaya çek

    def yukle(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self.pencere, "Bir Resim Seç", "", "Resimler (*.png *.jpg *.jpeg)")
        if dosya_yolu:
            onizleme = self.motor.resim_yukle(dosya_yolu)
            bilgiler = self.motor.resim_bilgiler()
            self.pencere.resim_guncelleme(onizleme)
            self.pencere.bilgi_etiketi.setText(f"Çözünürlük: {bilgiler['resolution'][0]}x{bilgiler['resolution'][1]} | Format: {bilgiler['format']}")

    def kaydet(self):
        if self.motor.orijinal_resim:
            dosya_yolu, _ = QFileDialog.getSaveFileName(self.pencere, "Kaydedilecek Yolu Seç", "", "PNG (*.png);;JPEG (*.jpg)")
            if dosya_yolu:
                self.motor.resim_kaydet(dosya_yolu)

    def sifirla(self):
        """Her şeyi en baştaki orijinal haline döndürür."""
        if self.motor.ilk_resim:
            self.motor.orijinal_resim = self.motor.ilk_resim.copy()
            self.motor.onizleme_resmi = self.motor.ilk_resim.copy()
            self.motor.onizleme_resmi.thumbnail((800, 600))
            self.pencere.ayar_cubugu.setValue(50)
            self.pencere.resim_guncelleme(self.motor.onizleme_resmi)