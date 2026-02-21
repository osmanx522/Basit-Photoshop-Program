from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO
from resim_islemleri import ResimMotoru

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.motor = ResimMotoru()

        # ANA DÜZEN 
        Hlayout = QHBoxLayout()
        sol_duzen = QVBoxLayout()

        self.resim_alani = QLabel("Burası Resim Alanı")
        sol_duzen.addWidget(self.resim_alani)

        bilgi_etiketi = QLabel("Bİlgiler: (Çözünürlük, Format vb)")
        sol_duzen.addWidget(bilgi_etiketi)
        sag_duzen = QVBoxLayout()

        # BUTON BÖLÜMLERİ 
        izgara = QGridLayout()
        
        btn_ac = QPushButton("Resim Aç")
        btn_ac.clicked.connect(self.yukle)

        btn_kaydet = QPushButton("Resim Kaydet")
        btn_kaydet.clicked.connect(self.kaydet)

        btn_gltich = QPushButton("Glitch Efekti")
        btn_gltich.setCheckable(True)

        btn_bulanik = QPushButton("Blur Efekti")
        btn_bulanik.setCheckable(True)

        izgara.addWidget(btn_ac, 0,0)
        izgara.addWidget(btn_kaydet, 0,1)
        izgara.addWidget(btn_gltich, 1,0)
        izgara.addWidget(btn_bulanik, 1,1)
        sag_duzen.addLayout(izgara)

        self.efekt_grubu = QButtonGroup(self)
        self.efekt_grubu.addButton(btn_gltich, 1)
        self.efekt_grubu.addButton(btn_bulanik, 2)

        # AYAR CUBUGU
        self.ayar_cubugu = QSlider(Qt.Horizontal)
        self.ayar_cubugu.valueChanged.connect(self.efekt_uygula)
        sag_duzen.addWidget(self.ayar_cubugu)

        Hlayout.addLayout(sol_duzen)
        Hlayout.addLayout(sag_duzen)
        self.setLayout(Hlayout)

    def resim_guncelleme(self, resim):
        hafiza = BytesIO()
        resim.save(hafiza, format="BMP")
        pixmap_resim = QPixmap()
        pixmap_resim.loadFromData(hafiza.getvalue())
        # Qt.KeepAspectRatio: Resmin en-boy oranını korur
        # Qt.SmoothTransformation: Küçültürken piksellenmeyi önler
        duzenli_resim = pixmap_resim.scaled(800, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.resim_alani.setPixmap(duzenli_resim) # Resim alanına resmi yerleştirir.

    def efekt_uygula(self):
        if self.motor.orijinal_resim:
            siddet = self.ayar_cubugu.value()
            secili_efekt = self.efekt_grubu.checkedId()
            if secili_efekt == 1:
                self.glitch(siddet)
            elif secili_efekt == 2:
                self.blur(siddet)
    def yukle(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, "Bir Resim Seç", "", "Resimler (*.png *.jpg *.jpeg)")
        if dosya_yolu:
            pil_resmi = self.motor.resim_yukle(dosya_yolu)
            self.resim_guncelleme(pil_resmi)

    def kaydet(self):
        if self.motor.orijinal_resim:
            dosya_yolu, _ = QFileDialog.getSaveFileName(self, "Kaydedilcek Yolu Seçin", "","PNG Formatı (*.png);;JPEG Formatı (*.jpg *.jpeg)")
            if dosya_yolu:
                self.motor.resim_kaydet(dosya_yolu)
    def glitch(self, siddet):
        retro_resim = self.motor.glitch_efekti(siddet)
        self.resim_guncelleme(retro_resim)
    def blur(self, siddet):
        blur_resim = self.motor.blur_efekti(siddet)
        self.resim_guncelleme(blur_resim)