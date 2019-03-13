# pip install pillow

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# black/white:'L', rgba:'RGBA', cmyk:'CMYK'
gambar = Image.open('lintang.png').convert('L')

# convert 0.png (388px x 388px) to array
arrayGambar = np.array(gambar)
print(arrayGambar)

# show result as image
hasil = Image.fromarray(arrayGambar, 'L')
hasil.show()