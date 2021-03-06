import simple_operations
import pixelate
import psorting
import random
import unsplash
import resize
import twitterbot
import swirl
import glitch_effects



# Image name
imagename = "image_temp"

# Get an image
unsplash.get_image(imagename)

# Resize image for twitter restrictions and easier computation
resize.resize_image(imagename)



# Operate on the image using some random actions
y = random.randint(1, 12)



if y == 1:
  simple_operations.invert_half(imagename)
  psorting.s_pixels(imagename)
elif y == 2:	
  simple_operations.invert_half(imagename)
  simple_operations. displace_squares(imagename)
elif y == 3:	
  simple_operations.invert_half(imagename)
  simple_operations.square_rotate(imagename)
elif y == 4:
	pixelate.pixelate_image(imagename)
# Removing this one because I think it is generally not a enough of a modification
elif y == 0:
	simple_operations.displace_squares(imagename)
elif y == 6 or y == 7 or y == 8: 
	psorting.s_pixels(imagename)
elif y == 9:
  psorting.s_pixels(imagename)
  swirl.swirl_image(-360, imagename)
elif y == 10:
  swirl.swirl_image(-360, imagename)
elif y == 11:
  psorting.s_pixels(imagename)
  swirl.swirl_image(-360, imagename)
  glitch_effects.make_scan_line(imagename)
else:
  psorting.s_pixels(imagename)
  glitch_effects.make_gif(imagename)

  




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

