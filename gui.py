from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO
from resim_islemleri import ResimMotoru
from button_function import ButonYoneticisi
class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.motor = ResimMotoru()
        self.buton_yonetici = ButonYoneticisi(self)
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
        btn_ac.clicked.connect(self.buton_yonetici.yukle)

        btn_kaydet = QPushButton("Resim Kaydet")
        btn_kaydet.clicked.connect(self.buton_yonetici.kaydet)

        btn_uygula = QPushButton("Resmi Uygula")
        btn_uygula.clicked.connect(self.buton_yonetici.uygula)

        btn_sifirla = QPushButton("Resmi Sıfırla")
        btn_sifirla.clicked.connect(self.buton_yonetici.sifirla)

        btn_gltich = QPushButton("Glitch Efekti")
        btn_gltich.setCheckable(True)

        btn_bulanik = QPushButton("Blur Efekti")
        btn_bulanik.setCheckable(True)

        izgara.addWidget(btn_ac, 0,0)
        izgara.addWidget(btn_kaydet, 0,1)
        izgara.addWidget(btn_sifirla, 0,2)
        izgara.addWidget(btn_uygula, 0,3)
        izgara.addWidget(btn_gltich, 1,0)
        izgara.addWidget(btn_bulanik, 1,1)
        sag_duzen.addLayout(izgara)

        self.efekt_grubu = QButtonGroup(self)
        self.efekt_grubu.addButton(btn_gltich, 1)
        self.efekt_grubu.addButton(btn_bulanik, 2)

        # AYAR CUBUGU
        self.ayar_cubugu = QSlider(Qt.Horizontal)
        self.ayar_cubugu.valueChanged.connect(self.buton_yonetici.efekt_uygula)
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
    