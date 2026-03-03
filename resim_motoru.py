import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

class ResimMotoru:
    def __init__(self):
        self.ilk_resim = None        # Dosyadan ilk açılan ham hali (Geri dönüş için)
        self.orijinal_resim = None   # Efektlerin kalıcı olarak bindiği yüksek çözünürlüklü hali
        self.onizleme_resmi = None   # Sadece ekranda hızlı görmek için kullanılan küçük resim
        
        # Efekt Manager: Fonksiyonları merkezi bir yerden yönetir
        self.effect_manager = {
            1: self.glitch_efekti,
            2: self.blur_efekti,
            3: lambda s, res: self.enhancements_apply(ImageEnhance.Color, s, res),
            4: lambda s, res: self.enhancements_apply(ImageEnhance.Brightness, s, res),
            5: lambda s, res: self.enhancements_apply(ImageEnhance.Contrast, s, res),
            6: lambda s, res: self.enhancements_apply(ImageEnhance.Sharpness, s, res),
        }

    def resim_yukle(self, resim_yolu):
        self.ilk_resim = Image.open(resim_yolu)
        self.orijinal_resim = self.ilk_resim.copy()
        
        # Önizleme için küçük bir kopya oluştur (Performans için kritik)
        self.onizleme_resmi = self.ilk_resim.copy()
        self.onizleme_resmi.thumbnail((800, 600))
        return self.onizleme_resmi

    def resim_bilgiler(self):
        if not self.ilk_resim: return {}
        return {
            "resolution": self.ilk_resim.size,
            "format": self.ilk_resim.format,
            "mode": self.ilk_resim.mode
        }

    def resim_kaydet(self, resim_yolu):
        if self.orijinal_resim:
            self.orijinal_resim.save(resim_yolu)

    # EFEKT FONKSİYONLARI
    def glitch_efekti(self, siddet, kaynak_resim):
        img_arr = np.array(kaynak_resim)
        if len(img_arr.shape) < 3: return kaynak_resim # RGB değilse işlem yapma
        
        r, g, b = img_arr[:,:,0], img_arr[:,:,1], img_arr[:,:,2]
        r_shift = np.roll(r, siddet, axis=1)
        b_shift = np.roll(b, -siddet, axis=1)
        
        img_arr_new = np.dstack((r_shift, g, b_shift))
        return Image.fromarray(img_arr_new)

    def blur_efekti(self, siddet, kaynak_resim):
        # GaussianBlur 0-100 arası çok fazladır, değeri normalize ediyoruz
        return kaynak_resim.filter(ImageFilter.GaussianBlur(siddet / 10))

    def enhancements_apply(self, enh_tool, siddet, kaynak_resim):
        # Orta nokta 50 (Değişim yok = 1.0). 0-100 arası 0.0 ile 2.0 arası çarpan verir.
        faktor = siddet / 50 
        return enh_tool(kaynak_resim).enhance(faktor)