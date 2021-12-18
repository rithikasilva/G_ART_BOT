from imagedisplacement import square_rotate, displace_squares, half_back, invert_half
from pixelate import pixelate_image, pixelate_piece
from psorting import s_pixels


def half_invert_pixel_sort(name):
    invert_half(name)
    s_pixels(name)


def half_invert_square_displace(name):
    invert_half(name)
    displace_squares(name)


def half_invert_rotate_square(name):
    invert_half(name)
    square_rotate(name)


def pixelate(name):
    pixelate_image(name)






