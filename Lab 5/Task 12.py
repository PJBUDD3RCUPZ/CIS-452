from PIL import Image, ImageFilter
from PIL.ImageFilter import (CONTOUR)

Lenna = Image.open(r'C:\Users\crazy\Desktop\Lab2\CIS-452\Lenna.png')

contour = Lenna.filter(CONTOUR)

contour.show()