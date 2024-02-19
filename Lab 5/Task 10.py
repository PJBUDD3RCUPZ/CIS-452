from PIL import Image

island = Image.open(r'C:\Users\crazy\Desktop\Lab2\CIS-452\Island.png')

flip = island.transpose(Image.FLIP_LEFT_RIGHT)

flip.show()