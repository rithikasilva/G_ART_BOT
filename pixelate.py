from PIL import Image



def pixelate_image(imgtitle):
    img = Image.open("./working/" + imgtitle + ".png")
    imgPixelate = img.resize((16,16),resample=Image.BILINEAR)
    result = imgPixelate.resize(img.size, Image.NEAREST)
    result.save("./working/" + imgtitle + ".png")


def pixelate_piece(piece):
    piecePixelate = piece.resize((16,16),resample=Image.BILINEAR)
    result = piecePixelate.resize(piecePixelate.size, Image.NEAREST)
    return result
