import numpy as np
from PIL import Image

class ResimMotoru:
    def __init__(self):
        self.orijinal_resim = None
        self.guncel_resim = None
        self.orijinal_resim_array = None
        self.guncel_resim_array = None

    def resim_yukle(self, resim_yolu):
        self.orijinal_resim = Image.open(resim_yolu)
        self.guncel_resim = self.orijinal_resim.copy()
        self.orijinal_resim_array = np.array(self.orijinal_resim)
        self.guncel_resim_array = self.orijinal_resim_array.copy()
        return self.guncel_resim
    
    def glitch_effekti(self):
        r, g, b = self.guncel_resim_array[:,:,0] , self.guncel_resim_array[:,:,1], self.guncel_resim_array[:,:,2]
        r_shift = np.roll(r, 10, axis=1)
        b_shift = np.roll(b, -10, axis=1)
        self.guncel_resim_array = np.dstack((r_shift, g, b_shift))
        self.guncel_resim = Image.fromarray(self.guncel_resim_array)
        return self.guncel_resim