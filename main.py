from PIL import Image, ImageFilter, ImageFont, ImageDraw
from image.ImageHandler import ImageHandler
from image.ImageProcessor import ImageProcessor
def main():

    image = ImageHandler('image_2.jpg')
    image.crop()
    image.turn()
    
    rezultimg  = ImageProcessor(image)
    rezultimg.add_filter()
    rezultimg.add_text((10,10), "Вариант 2", size = 20, color = 'black')

    rezultimg = image
    image.save_img('image2.jpg')

main()