# 📸 PyImageEditor - Dinamik Fotoğraf Düzenleyici

Bu proje, Python ve PyQt5 kullanılarak geliştirilmiş, anlık geri bildirim veren ve katmanlı efekt uygulama mantığına sahip bir masaüstü fotoğraf düzenleme yazılımıdır. 

## ✨ Öne Çıkan Özellikler

* **Real-Time Önizleme:** Kaydırma çubuğu (slider) ile efekt şiddetini anlık olarak ekranda görün.
* **Katmanlı Efekt Sistemi:** "Uygula" (Apply) mekanizması sayesinde birden fazla efekti (Blur + Glitch vb.) üst üste bindirin.
* **Gelişmiş Geri Dönüş:** "Sıfırla" butonu ile tek tıkla resmin en orijinal haline dönün.
* **Akıllı Hafıza Yönetimi:** Üç kademeli (ilk_resim, orijinal_resim, guncel_resim) mimari ile veri kaybını ve görüntü bozulmasını önler.

## 🛠 Kullanılan Teknolojiler

* **Python 3.x**
* **PyQt5:** Grafiksel kullanıcı arayüzü yönetimi.
* **Pillow (PIL):** Görüntü işleme filtreleri.
* **NumPy:** RGB kanal kaydırma işlemleri (Glitch efekti için).

## 🚀 Kurulum ve Çalıştırma

1. Gerekli kütüphaneleri yükleyin:
   pip install PyQt5 Pillow numpy

2. Projeyi başlatın:
   python gui.py

## 📖 Kullanım Kılavuzu

1. **Resim Aç:** Düzenlemek istediğiniz fotoğrafı seçin.
2. **Efekt Seçin:** Glitch veya Blur butonlarından birine tıklayın.
3. **Ayar Yapın:** Alttaki kaydırma çubuğunu kullanarak şiddeti belirleyin.
4. **Resmi Uygula:** Efekti beğendiyseniz bu butona basarak sabitleyin. Yeni efektler bu mühürlenmiş görüntü üzerine eklenir.
5. **Resmi Sıfırla:** Tüm değişiklikleri iptal edip en başa dönmek için kullanın.
6. **Resmi Kaydet:** Sonucu bilgisayarınıza kaydedin.

---
*Bu proje, modüler yazılım mimarisi ve dinamik veri akışı prensipleriyle geliştirilmiştir.*