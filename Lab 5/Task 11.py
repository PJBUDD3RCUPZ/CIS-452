from PIL import Image, ImageFilter

island = Image.open(r'C:\Users\crazy\Desktop\Lab2\CIS-452\Island.png')

blur = island.filter(ImageFilter.BoxBlur(5))

blur.show()