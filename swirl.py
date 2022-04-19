from wand.image import Image


def swirl_image(deg, imgtitle):
    with Image(filename = "./working/" + imgtitle + ".png") as img:
        img.swirl(degree = deg)
        img.save(filename = "./working/" + imgtitle + ".png")


