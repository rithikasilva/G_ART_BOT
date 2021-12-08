import numpy as np
import matplotlib.pylab as plt
from PIL import Image
import random



#img_crop = img.crop((0,0,nwidth,nheight))
#img_crop = img_crop.rotate(90)

#back_im.paste(img_crop)

def square_rotate(imgtitle):
    img = Image.open("./images/" + imgtitle + ".jpg")
    back_im = img.copy()
    width, height = img.size

    square_dimension = int(min(height,width) / 4)

    ransquarenumber = random.randint(0, 7)

    for x in range(ransquarenumber):
        cordx = random.randint(square_dimension,width)
        cordy = random.randint(square_dimension,height)
        rotaterand = random.randint(0,4)
        img_crop = img.crop((cordx - square_dimension, cordy - square_dimension, cordx, cordy))
        img_crop = img_crop.rotate(rotaterand * 90)
        back_im.paste(img_crop, (cordx - square_dimension, cordy - square_dimension, cordx, cordy))

    back_im.save("./square/square"+ imgtitle + ".jpg")






