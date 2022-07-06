from PIL import Image, ImageFont, ImageDraw  # Importing the necessary modules
from config import *  # This file Contains the API Keys and other sensitive information


async def create_image(price):
    my_image = Image.open("btc.png")  # Opening File
    title_font = ImageFont.truetype("./Montserrat-ExtraBold.ttf", 220, encoding="unic")
    price = str(price)
    image_editable = ImageDraw.Draw(my_image)  # Creating a draw object
    width, height = my_image.size
    textW, textH = image_editable.textsize(price, font=title_font)
    image_editable.text(
        ((width - textW) / 2, ((height - textH) / 2) - 30),
        price,
        (13, 8, 93),
        font=title_font,
    )
    my_image.save("res.png")  # Saving the image
    return True
