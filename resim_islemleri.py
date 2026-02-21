import numpy as np
from PIL import Image, ImageFilter

class ResimMotoru:
    def __init__(self):
        self.orijinal_resim = None
        self.guncel_resim = None

    def resim_yukle(self, resim_yolu):
        self.orijinal_resim = Image.open(resim_yolu)
        self.guncel_resim = self.orijinal_resim.copy()

        return self.guncel_resim
    
    def resim_kaydet(self, resim_yolu):
        self.guncel_resim.save(resim_yolu)

    def glitch_efekti(self, siddet):
        img_arr = np.array(self.guncel_resim)
        r, g, b = img_arr[:,:,0] ,img_arr[:,:,1], img_arr[:,:,2]
        r_shift = np.roll(r, siddet, axis=1)
        b_shift = np.roll(b, -siddet, axis=1)
        img_arr_new = np.dstack((r_shift, g, b_shift))
        self.guncel_resim = Image.fromarray(img_arr_new)
        return self.guncel_resim
    
    def blur_efekti(self, siddet):
        blur_resim = self.guncel_resim.filter(ImageFilter.GaussianBlur(siddet))
        return blur_resim