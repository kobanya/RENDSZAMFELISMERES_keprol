import pytesseract
from PIL import Image

# Először beolvassuk a képet a Pillow könyvtár segítségével
image = Image.open('HU_rendszem.png')

# A pytesseract könyvtárat használjuk a szöveg felismerésére
text = pytesseract.image_to_string(image, lang='eng')

# Kiírjuk a felismert szöveget a terminálra
print("Felismert szöveg:")
print(text)
