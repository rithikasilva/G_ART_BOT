import numpy as np
import matplotlib.pylab as plt
from PIL import Image, ImageDraw, ImageOps
import random



def square_rotate(imgtitle):
    img = Image.open("./working/" + imgtitle + ".png")
    back_im = img.copy()
    width, height = img.size

    square_dimension = int(min(height,width) / 4)

    ransquarenumber = random.randint(1, 7)

    for x in range(ransquarenumber):
        cordx = random.randint(square_dimension,width)
        cordy = random.randint(square_dimension,height)
        rotaterand = random.randint(0,4)
        img_crop = img.crop((cordx - square_dimension, cordy - square_dimension, cordx, cordy))
        img_crop = img_crop.rotate(rotaterand * 90)
        back_im.paste(img_crop, (cordx - square_dimension, cordy - square_dimension, cordx, cordy))

    back_im.save("./working/"+ imgtitle + ".png")



def displace_squares(imgtitle):
    img = Image.open("./working/" + imgtitle + ".png")
    back_im = img.copy()
    width, height = img.size

    square_dimension = int(min(height, width) / 4)

    ransquarenumber = random.randint(1, 4)

    for x in range(ransquarenumber):

        # Get a random square and rotation
        cordx1 = random.randint(square_dimension,width)
        cordy1 = random.randint(square_dimension,height)

        #
        cordx2 = random.randint(square_dimension, width)
        cordy2 = random.randint(square_dimension, height)


        img_crop1 = img.crop((cordx1 - square_dimension, cordy1 - square_dimension, cordx1, cordy1))
        img_crop2 = img.crop((cordx2 - square_dimension, cordy2 - square_dimension, cordx2, cordy2))

        back_im.paste(img_crop2, (cordx1 - square_dimension, cordy1 - square_dimension, cordx1, cordy1))
        back_im.paste(img_crop1, (cordx2 - square_dimension, cordy2 - square_dimension, cordx2, cordy2))

    back_im.save("./working/" + imgtitle + ".png")



def half_back(imgtitle):
    img = Image.open("./working/" + imgtitle + ".png")
    back_im = img.copy()
    width, height = img.size

    # creating new Image object
    img = Image.new("RGB", (int(width/2), height))

    draw = ImageDraw.Draw(back_im)
    draw.rectangle([(int(width/2), 0), (width, height)], fill="#000000", outline="black")

    back_im.save("./working/" + imgtitle + ".png")



def invert_half(imgtitle):
    img = Image.open("./working/" + imgtitle + ".png")
    back_im = img.copy()
    width, height = img.size

    img_crop = img.crop((int(width/2), 0, width, height))

    img_crop = ImageOps.invert(img_crop)
    back_im.paste(img_crop, (int(width/2), 0, width, height))
    back_im.save("./working/" + imgtitle + ".png")


