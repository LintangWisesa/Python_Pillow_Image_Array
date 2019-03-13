# pip install pillow

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# black/white:'L', rgba:'RGBA', cmyk:'CMYK'
gambar = Image.open('jokowi.jpg').convert('L')
arrayGambar = np.array(gambar)

# plot array
plt.imshow(arrayGambar, cmap='gray')
plt.show()