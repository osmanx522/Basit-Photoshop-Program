import numpy as np
from PIL import Image

class ResimMotoru:
    def __init__(self):
        self.orijinal_resim = None
        self.guncel_resim = None
    
    def resim_yukle(self, resim_yolu):
        self.orijinal_resim = Image.open(resim_yolu)
        self.guncel_resim = self.orijinal_resim.copy()

        return self.guncel_resim