from PIL import Image, ImageFont, ImageDraw  # Importing the necessary modules
from config import *  # This file Contains the API Keys and other sensitive information


my_image = Image.open("btc.png")
# applying Text in the Middle of the Image
title_font = ImageFont.truetype("./Montserrat-ExtraBold.ttf", 220, encoding="unic")


title_text = "$69,6969"

image_editable = ImageDraw.Draw(my_image)

width, height = my_image.size


width, height = my_image.size

textW, textH = image_editable.textsize(title_text, font=title_font)
image_editable.text(
    ((width - textW) / 2, ((height - textH) / 2) - 30),
    title_text,
    (13, 8, 93),
    font=title_font,
)


my_image.save("result.png")
