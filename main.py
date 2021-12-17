from imagedisplacement import square_rotate, displace_squares, half_back, invert_half
from pixelate import pixelate_image, pixelate_piece
from pixelsort import s_pixels
from compositefunctions import half_invert_pixel_sort, half_invert_square_displace, half_invert_rotate_square, pixelate
import random
from unsplash import get_image
from resize import resize_image
from twitterbot import tweet_image
import time
import datetime


# get current time
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute

# Run at 2:00pm at every day
if (hour == 14) and (minute == 0):

    # Get an image
    get_image()

    # Operate on the image
    y = random.randint(1,6)
    if y == 1:
        half_invert_pixel_sort("image_temp")
    elif y == 2:
        half_invert_square_displace("image_temp")
    elif y== 3:
        half_invert_rotate_square("image_temp")
    elif y == 4:
        pixelate("image_temp")
    elif y == 5:
        displace_squares("image_temp")
    else:
        s_pixels("image_temp")


    # Resize image for twitter restrictions
    resize_image()

    # Gets the Current Number
    f = open("number.txt", "r")
    number = int(f.read())
    f.close()

    # Tweet the image
    tweet_image(number)


    # Increments number
    number = number + 1
    f = open("number.txt", "w")
    f.write(str(number))
    f.close()

    # wait 60 seconds so that we don't have two runs
    time.sleep(60)


