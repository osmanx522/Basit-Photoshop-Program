import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

class ResimMotoru:
    def __init__(self):
        self.ilk_resim = None
        self.orijinal_resim = None
        self.guncel_resim = None

    def resim_yukle(self, resim_yolu):
        self.ilk_resim = Image.open(resim_yolu)
        self.orijinal_resim = self.ilk_resim.copy()
        self.guncel_resim = self.ilk_resim.copy()
        return self.guncel_resim
    
    def resim_bilgiler(self):
        dic = {
            "resolution": self.ilk_resim.size,
            "format": self.ilk_resim.format,
            "mode": self.ilk_resim.mode
        }
        return dic
    
    def resim_kaydet(self, resim_yolu):
        if self.guncel_resim:
            self.guncel_resim.save(resim_yolu)

    def glitch_efekti(self, siddet):
        img_arr = np.array(self.orijinal_resim)
        r, g, b = img_arr[:,:,0] ,img_arr[:,:,1], img_arr[:,:,2]
        r_shift = np.roll(r, siddet, axis=1)
        b_shift = np.roll(b, -siddet, axis=1)
        img_arr_new = np.dstack((r_shift, g, b_shift))
        self.guncel_resim = Image.fromarray(img_arr_new)
        return self.guncel_resim
    
    def blur_efekti(self, siddet):
        self.guncel_resim = self.orijinal_resim.filter(ImageFilter.GaussianBlur(siddet))
        return self.guncel_resim
    
    def grayscale_efekti(self, siddet):
        siddet = 1-(siddet/100)
        self.guncel_resim = ImageEnhance.Color(self.orijinal_resim).enhance(siddet)
        return self.guncel_resim