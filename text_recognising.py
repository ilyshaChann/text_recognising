from PIL import Image

import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR'

custom_config = r'--oem 3 --psm 6'


image = Image.open("какая-то картинка.jpg")

#print ( pytesseract . image_to_string ( Image . open ( 'index.png' ),  lang = 'rus' ))
#print ( pytesseract . image_to_data ( Image . open ( 'index.png' )))

print(pytesseract.image_to_string(image))

text = pytesseract.image_to_string(image, lang = 'rus', config = custom_config)

with open ("teeexxxt.txt", "w", encoding= 'utf-8') as text_file:
    text_file.write(text)

