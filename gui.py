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

        # Dosya İşlem Olan Butonlar
        # Yapı: (Buton Metni, Obje Adı, Bağlanacak Fonksiyon, Sütun Numarası)
        aksiyon_butonlari = [
            ("Resim Aç", "btn_ac", self.buton_yonetici.yukle, 0),
            ("Resim Kaydet", "btn_kaydet", self.buton_yonetici.kaydet, 1),
            ("Resmi Sıfırla", "btn_sifirla", self.buton_yonetici.sifirla, 2),
            ("Resmi Uygula", "btn_uygula", self.buton_yonetici.uygula, 3)
        ]

        for metin, obje_adi, fonksiyon, sutun in aksiyon_butonlari:
            btn = QPushButton(metin)
            btn.setObjectName(obje_adi)
            btn.clicked.connect(fonksiyon)
            izgara.addWidget(btn, 0, sutun) # 0. Satıra sırayla diziyoruz


        # EFEKT BUTONLARI
        # Yapı: (Buton Metni, Grup ID'si, Sütun Numarası)
        self.efekt_grubu = QButtonGroup(self)
        
        efekt_butonlari = [
            ("Glitch Efekti", 1, 0),
            ("Blur Efekti", 2, 1),
            ("Siyah-Beyaz", 3, 2),
            ("Parlaklık", 4, 3),
            ("Kontrast", 5, 4),
            ("Keskinleştirme", 6, 5),
        ]

        for metin, grup_id, sutun in efekt_butonlari:
            btn = QPushButton(metin)
            btn.setCheckable(True)
            self.efekt_grubu.addButton(btn, grup_id)
            izgara.addWidget(btn, 1, sutun) # 1. Satıra sırayla diziyoruz

        sag_duzen.addLayout(izgara)
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
        '''Resmi ekranda anlık olarak güncellemeyi sağlayan fonksiyon,
            Ram'e yüklenen sanal bmp dosyasından sağlar.'''
        hafiza = BytesIO()
        resim.save(hafiza, format="BMP")
        pixmap_resim = QPixmap()
        pixmap_resim.loadFromData(hafiza.getvalue())
        # Qt.KeepAspectRatio: Resmin en-boy oranını korur
        # Qt.SmoothTransformation: Küçültürken piksellenmeyi önler
        duzenli_resim = pixmap_resim.scaled(800, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.resim_alani.setPixmap(duzenli_resim) # Resim alanına resmi yerleştirir.
    