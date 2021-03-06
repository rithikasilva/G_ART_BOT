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







loop = True
while (loop):
  y = input("Select an option:")
  y = int(y)
  
  if y == 1:
    loop = False
  elif y == 2:
    simple_operations.invert_half(imagename)
    psorting.s_pixels(imagename)
  elif y == 3:	
    simple_operations.invert_half(imagename)
    simple_operations. displace_squares(imagename)
  elif y == 4:	
    simple_operations.invert_half(imagename)
    simple_operations.square_rotate(imagename)
  elif y == 5:
  	pixelate.pixelate_image(imagename)
  elif y == 6:
  	simple_operations.displace_squares(imagename)
  elif y == 7 or y == 8 or y == 9: 
  	psorting.s_pixels(imagename)
  elif y == 10:
    psorting.s_pixels(imagename)
    swirl.swirl_image(-360, imagename)
  elif y == 11:
    swirl.swirl_image(-360, imagename) 
  elif y == 12:
   simple_operations.square_rotate(imagename)
  elif y == 13:
   simple_operations.crop_square(imagename)
  elif y == 14:
    glitch_effects.make_scan_line_gif(imagename)
  else:
   simple_operations.invert_colour(imagename)
  





# Feedback for completion
print("done")

