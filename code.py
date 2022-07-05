from PIL import Image, ImageFont, ImageDraw


my_image = Image.open("nature.jpeg")

title_font = ImageFont.truetype("./K2D-Regular.ttf", 200)


title_text = "The Beauty of Nature"

image_editable = ImageDraw.Draw(my_image)


image_editable.text((15, 15), title_text, (0, 0, 0), font=title_font)

my_image.save("result.jpeg")
