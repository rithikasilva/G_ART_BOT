import numpy as np
from PIL import Image
from typing import Callable


# Written by u/GregTJ on reddit, so credits to them

def sort_pixels(image: Image, value: Callable, condition: Callable, rotation: int = 0) -> Image:
    pixels = np.rot90(np.array(image), rotation)
    values = value(pixels)
    edges = np.apply_along_axis(lambda row: np.convolve(row, [-1, 1], 'same'), 0, condition(values))
    intervals = [np.flatnonzero(row) for row in edges]

    for row, key in enumerate(values):
        order = np.split(key, intervals[row])
        for index, interval in enumerate(order[1:]):
            order[index + 1] = np.argsort(interval) + intervals[row][index]
        order[0] = range(order[0].size)
        order = np.concatenate(order)

        for channel in range(3):
            pixels[row, :, channel] = pixels[row, order.astype('uint32'), channel]

    return Image.fromarray(np.rot90(pixels, -rotation))


# sends to "new" + original image name ".jpg"
def s_pixels(imagename):
    sort_pixels(Image.open("./images/" + imagename + ".jpg"),
                lambda pixels: np.average(pixels, axis=2) / 255,
                lambda lum: (lum > 2 / 6) & (lum < 4 / 6), 1).save("./pixel/pixel" + imagename+ '.jpg')


s_pixels('leaf')
#s_pixels('sky1')
#s_pixels('mountain')
