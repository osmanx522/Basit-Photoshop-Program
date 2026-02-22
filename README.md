# 🎨 Python Görüntü İşleme Editörü (Mini Photoshop)

Bu proje, Python ve PyQt5 kullanılarak sıfırdan geliştirilmiş, **MVC (Model-View-Controller)** mimarisine sahip modern bir masaüstü fotoğraf düzenleme uygulamasıdır. Kullanıcıların fotoğraflarına gerçek zamanlı filtreler ve renk/ışık ayarlamaları (Image Enhancement) uygulamasına olanak tanır.

## 🚀 Öne Çıkan Özellikler

* **Modern ve Şık Arayüz (Dark Mode):** QSS kullanılarak özel tasarlanmış koyu tema, interaktif butonlar ve özelleştirilmiş kaydırma çubuğu (slider) deneyimi.
* **Gerçek Zamanlı Önizleme:** Seçilen efektin şiddetini alt taraftaki sürgü (slider) ile anlık olarak ayarlayabilme ve ekranda donma olmadan görebilme.
* **Akıllı Bilgi Paneli:** Yüklenen resmin anlık Çözünürlük, Format (JPEG, PNG vb.) ve Renk Modu (RGB) bilgilerini alt panelde gösterme.
* **3 Aşamalı Hafıza Yönetimi:** * **Resmi Sıfırla:** Yapılan tüm işlemleri geri alıp fotoğrafın ilk haline dönme.
  * **Resmi Uygula:** Yapılan efekti kalıcı hale getirip, üzerine yeni efektler ekleyebilme.
* **Temiz Kod (Clean Code):** Arayüz elemanlarının kod tekrarı (Spagetti Kod) yapılmadan, dinamik for döngüleriyle nesne tabanlı olarak oluşturulması.

## 🛠️ İçerdiği Araçlar ve Efektler

**1. Görüntü İyileştirme (Enhancements - PIL):**
* ☀️ **Parlaklık (Brightness):** Resmin ışık değerlerini anlık olarak artırıp azaltma.
* 🌗 **Kontrast (Contrast):** Renkler ve tonlar arası zıtlığı ayarlama.
* 📐 **Keskinleştirme (Sharpness):** Kenar detaylarını ve pikselleri belirginleştirme.
* 🎞️ **Siyah-Beyaz (Grayscale):** Resmin renk doygunluğu (saturation) ile oynayarak dramatik tonlar elde etme.

**2. Artistik Filtreler:**
* 📺 **Glitch Efekti:** NumPy matris (Array) hesaplamaları ve `np.roll` kullanarak RGB kanallarını kaydırma yoluyla dijital bozulma/3D gözlük efekti yaratma.
* 💧 **Blur (Bulanıklık):** Pillow `ImageFilter` motoruyla yumuşak odak (Gaussian Blur) sağlama.

## 📂 Proje Mimarisi (Dosya Yapısı)

Proje karmaşıklığı önlemek için 4 ayrı dosyaya bölünmüştür:
* `main.py` **(Başlatıcı):** Programın ana giriş noktasıdır. Uygulamayı ayağa kaldırır.
* `gui.py` **(View):** Sadece QSS tasarım kodlarının, pencerelerin, buton listelerinin ve görsel unsurların bulunduğu arayüz dosyasıdır.
* `resim_motoru.py` **(Model):** Resimlerin hafızada tutulduğu (ilk_resim, orijinal_resim, guncel_resim), Numpy ve Pillow algoritmalarının piksel piksel işlendiği çekirdek motordur.
* `button_function.py` **(Controller):** Arayüz (GUI) ile Resim Motoru arasındaki köprüdür. Kullanıcının buton tıklamalarını ve sürgü hareketlerini dinleyip motora iletir.

## 💻 Kullanılan Teknolojiler
* **Python 3.x**
* **PyQt5:** Grafiksel Kullanıcı Arayüzü (GUI) tasarımı için.
* **Pillow (PIL):** Temel görüntü işleme ve iyileştirme motoru.
* **NumPy:** Piksel tabanlı gelişmiş matematiksel matris işlemleri için.

## ⚙️ Nasıl Çalıştırılır?

1. Projeyi bilgisayarınıza indirin.
2. Terminal (Komut Satırı) üzerinden gerekli kütüphaneleri yükleyin:
   ```bash
   pip install PyQt5 Pillow numpy
3. Projenin ana başlatıcı dosyasını çalıştırarak uygulamayı açın:
   ```bash
   python main.py