from PIL import Image

island = Image.open(r'C:\Users\crazy\Desktop\Lab2\CIS-452\Island.png')

flip = island.rotate(30)

flip.show()