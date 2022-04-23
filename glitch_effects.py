from PIL import Image
from glitch_this import ImageGlitcher


#glitch_image(self, src_img, glitch_amount, glitch_change=0.0, cycle=False, color_offset=False, scan_lines=False, gif=False, frames=23, step=1)

def make_gif(imgname):
    glitcher = ImageGlitcher()
    img = Image.open("./working/" + imgname + ".png")
    glitch_img = glitcher.glitch_image(img, 2, color_offset=True, scan_line=True, gif=True)
    glitch_img[0].save("./working/" + imgname + ".png",
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=100,
                   loop=0)

def make_scan_line_gif(imgname):
    glitcher = ImageGlitcher()
    img = Image.open("./working/" + imgname + ".png")
    glitch_img = glitcher.glitch_image(img, 2, color_offset=True, scan_lines=True, gif=True)
    glitch_img[0].save("./working/" + imgname + ".png",
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=10,
                   loop=0)
