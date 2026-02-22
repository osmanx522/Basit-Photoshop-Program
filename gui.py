from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO
from resim_motoru import ResimMotoru
from button_function import ButonYoneticisi
class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.motor = ResimMotoru()
        self.buton_yonetici = ButonYoneticisi(self)
        
        # ANA DÜZEN 
        Hlayout = QHBoxLayout()
        Hlayout.setContentsMargins(20,20,20,20)
        Hlayout.setSpacing(20)

        sol_duzen = QVBoxLayout()
        sag_duzen = QVBoxLayout()
        
        self.resim_alani = QLabel("Burası Resim Alanı")
        sol_duzen.addWidget(self.resim_alani)
        
        self.bilgi_etiketi = QLabel("Bilgiler: (Çözünürlük, format vb)")
        sol_duzen.addWidget(self.bilgi_etiketi)

        # BUTON BÖLÜMLERİ
        izgara = QGridLayout()
        izgara.setSpacing(15)
    
        btn_ac = QPushButton("Resim Aç")
        btn_ac.setObjectName("btn_ac")
        btn_ac.clicked.connect(self.buton_yonetici.yukle)

        btn_kaydet = QPushButton("Resim Kaydet")
        btn_kaydet.setObjectName("btn_kaydet")
        btn_kaydet.clicked.connect(self.buton_yonetici.kaydet)

        btn_uygula = QPushButton("Resmi Uygula")
        btn_uygula.setObjectName("btn_uygula")
        btn_uygula.clicked.connect(self.buton_yonetici.uygula)

        btn_sifirla = QPushButton("Resmi Sıfırla")
        btn_sifirla.setObjectName("btn_sifirla")
        btn_sifirla.clicked.connect(self.buton_yonetici.sifirla)

        btn_gltich = QPushButton("Glitch Efekti")
        btn_gltich.setCheckable(True)

        btn_bulanik = QPushButton("Blur Efekti")
        btn_bulanik.setCheckable(True)

        btn_grayscale = QPushButton("Siyah-Beyaz")
        btn_grayscale.setCheckable(True)

        izgara.addWidget(btn_ac, 0,0)
        izgara.addWidget(btn_kaydet, 0,1)
        izgara.addWidget(btn_sifirla, 0,2)
        izgara.addWidget(btn_uygula, 0,3)
        izgara.addWidget(btn_gltich, 1,0)
        izgara.addWidget(btn_bulanik, 1,1)
        izgara.addWidget(btn_grayscale, 1,2)
        sag_duzen.addLayout(izgara)

        self.efekt_grubu = QButtonGroup(self)
        self.efekt_grubu.addButton(btn_gltich, 1)
        self.efekt_grubu.addButton(btn_bulanik, 2)
        self.efekt_grubu.addButton(btn_grayscale, 3)

        # AYAR CUBUGU
        self.ayar_cubugu = QSlider(Qt.Horizontal)
        self.ayar_cubugu.valueChanged.connect(self.buton_yonetici.efekt_uygula)
        sag_duzen.addWidget(self.ayar_cubugu)

        Hlayout.addLayout(sol_duzen)
        Hlayout.addLayout(sag_duzen)
        self.setLayout(Hlayout)

        # TEMA VE STİL KODLARI (QSS)
        stil_kodu = """
        /* Ana Pencere ve Genel Ayarlar */
        QWidget {
            background-color: #2b2b2b; /* Koyu Gri Arka Plan */
            color: #ffffff;            /* Beyaz Yazı */
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 14px;
        }

        /* Resim Alanı (Çerçeveli ve Şık) */
        QLabel {
            background-color: #1e1e1e;
            border: 2px dashed #555555;
            border-radius: 10px;
            padding: 10px;
        }

        /* Genel Buton Tasarımı */
        QPushButton {
            background-color: #3c3f41;
            border: 1px solid #555555;
            border-radius: 6px;
            padding: 10px 15px;
            font-weight: bold;
        }
        
        /* Farenin Butonun Üstüne Gelmesi (Hover) */
        QPushButton:hover {
            background-color: #4b4f52;
            border: 1px solid #777777;
        }

        /* Tıklanabilir (Glitch/Blur) Butonların Seçili Hali */
        QPushButton:checked {
            background-color: #007acc; /* Hoş bir mavi */
            border: 1px solid #0098ff;
        }

        /* ÖZEL RENKLİ BUTONLAR */
        #btn_uygula {
            background-color: #2ecc71; /* Zümrüt Yeşili */
            color: #111111;
        }
        #btn_uygula:hover { background-color: #27ae60; }

        #btn_sifirla {
            background-color: #e74c3c; /* Canlı Kırmızı */
        }
        #btn_sifirla:hover { background-color: #c0392b; }

        #btn_kaydet {
            background-color: #2980b9; /* Belirgin Mavi */
        }
        #btn_kaydet:hover { background-color: #1f618d; }

        /* Ayar Çubuğu (Slider) Tasarımı */
        QSlider::groove:horizontal {
            border: 1px solid #444;
            height: 8px;
            background: #1e1e1e;
            border-radius: 4px;
        }
        QSlider::handle:horizontal {
            background: #007acc;
            border: 1px solid #007acc;
            width: 18px;
            margin: -6px 0; /* Çubuğun ortasında durması için */
            border-radius: 9px;
        }
        QSlider::handle:horizontal:hover {
            background: #0098ff;
        }
        """
        self.setStyleSheet(stil_kodu)

    def resim_guncelleme(self, resim):
        hafiza = BytesIO()
        resim.save(hafiza, format="BMP")
        pixmap_resim = QPixmap()
        pixmap_resim.loadFromData(hafiza.getvalue())
        # Qt.KeepAspectRatio: Resmin en-boy oranını korur
        # Qt.SmoothTransformation: Küçültürken piksellenmeyi önler
        duzenli_resim = pixmap_resim.scaled(800, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.resim_alani.setPixmap(duzenli_resim) # Resim alanına resmi yerleştirir.
    