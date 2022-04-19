import imagedisplacement
import pixelate
import psorting
import random
import unsplash
import resize
import twitterbot
import swirl


# Image name
imagename = "image_temp"

# Get an image
unsplash.get_image(imagename)

# Resize image for twitter restrictions and easier computation
resize.resize_image(imagename)



# Operate on the image using some random actions
y = random.randint(1, 9)


if y == 1:
        imagedisplacement.invert_half(imagename)
        psorting.s_pixels(imagename)
elif y == 2:	
        imagedisplacement.invert_half(imagename)
        imagedisplacement. displace_squares(imagename)
elif y == 3:	
        imagedisplacement.invert_half(imagename)
        imagedisplacement.square_rotate(imagename)
elif y == 4:
	pixelate.pixelate_image(imagename)
elif y == 5:
	imagedisplacement.displace_squares(imagename)
elif y == 6 or y == 7 or y == 8: 
	psorting.s_pixels(imagename)
else:
        swirl.swirl_image(-360, imagename)



# Gets the Current Number
f = open("number.txt", "r")
number = int(f.read())
f.close()

print(str(number))

# Tweet the image
twitterbot.tweet_image(number)

# Increments number
number = number + 1
f = open("number.txt", "w")
f.write(str(number))
f.close()

# Print done just for fun
print("done")

