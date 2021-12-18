from PIL import Image
import PIL

# Resizes images to the rescritions of the twitter API for media upload
def resize_image():
    fixed_width = 1280
    fixed_height = 1024
    image = Image.open("./working/image_temp.png")
    height = image.size[1]
    width = image.size[0]

    if height > width:
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int((float(image.size[0]) * float(height_percent)))
        image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
        image.save("./working/image_temp.png")

    else:
        width_percent = (fixed_width / float(image.size[0]))
        height_size = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((fixed_width, height_size), PIL.Image.NEAREST)
        image.save("./working/image_temp.png")