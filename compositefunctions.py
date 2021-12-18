from imagedisplacement import square_rotate, displace_squares, half_back, invert_half
from pixelate import pixelate_image, pixelate_piece
from psorting import s_pixels


# Inverts half the image, then runs a pixel sort on the image
def half_invert_pixel_sort(name):
    invert_half(name)
    s_pixels(name)


# Inverts half the image, then displaces some random squares
def half_invert_square_displace(name):
    invert_half(name)
    displace_squares(name)

# Inverts half the image, then rotates some random squares
def half_invert_rotate_square(name):
    invert_half(name)
    square_rotate(name)


# Pixelates the whole image
def pixelate(name):
    pixelate_image(name)






