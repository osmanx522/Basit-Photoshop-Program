from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO
from resim_islemleri import ResimMotoru
class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.motor = ResimMotoru()
        Hlayout = QHBoxLayout()
        sol_duzen = QVBoxLayout()

        self.resim_alani = QLabel("Burası Resim Alanı")
        sol_duzen.addWidget(self.resim_alani)

        bilgi_etiketi = QLabel("Bİlgiler: (Çözünürlük, Format vb)")
        sol_duzen.addWidget(bilgi_etiketi)
        sag_duzen = QVBoxLayout()

        izgara = QGridLayout()
        btn_ac = QPushButton("Resim Aç")
        btn_ac.clicked.connect(self.resim_yukle)
        btn_kaydet = QPushButton("Resim Kaydet")
        btn_retro = QPushButton("Retro")
        btn_bulanik = QPushButton("Bulanik")
        izgara.addWidget(btn_ac, 0,0)
        izgara.addWidget(btn_kaydet, 0,1)
        izgara.addWidget(btn_retro, 1,0)
        izgara.addWidget(btn_bulanik, 1,1)
        sag_duzen.addLayout(izgara)

        ayar_cubugu = QSlider(Qt.Horizontal)
        sag_duzen.addWidget(ayar_cubugu)

        Hlayout.addLayout(sol_duzen)
        Hlayout.addLayout(sag_duzen)
        self.setLayout(Hlayout)

    def resim_yukle(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, "Bir Resim Seç", "", "Resimler (*.png *.jpg *.jpeg)")
        if dosya_yolu:
            pil_resmi = self.motor.resim_yukle(dosya_yolu)

            hafiza = BytesIO()
            pil_resmi.save(hafiza, format="PNG")
            
            pixmap_resim = QPixmap()
            pixmap_resim.loadFromData(hafiza.getvalue())

            # Qt.KeepAspectRatio: Resmin en-boy oranını korur
            # Qt.SmoothTransformation: Küçültürken piksellenmeyi önler
            duzenli_resim = pixmap_resim.scaled(800, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.resim_alani.setPixmap(duzenli_resim) # Resim alanına resmi yerleştirir.