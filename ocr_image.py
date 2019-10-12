from PIL import Image
from pytesseract import *

print(image_to_string(Image.open('atm_1.png')))
print(image_to_string(Image.open('atm_2.png'), lang='eng'))