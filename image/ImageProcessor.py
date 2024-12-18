from PIL import Image, ImageFilter, ImageFont, ImageDraw
from image.ImageHandler import ImageHandler

class ImageProcessor():

    def __init__(self, filter_image):
        self.filter_image = filter_image

    def add_filter(self):
        self.filter_image.img = self.filter_image.img.convert("L")

    def add_text(self, position, text, size, color):
        draw_text = ImageDraw.Draw(self.filter_image.img)
        font = ImageFont.truetype('arial.ttf', size)
        draw_text.text(position, text, font= font, fill = color)