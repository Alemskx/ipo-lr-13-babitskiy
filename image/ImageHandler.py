from PIL import Image

class ImageHandler():

    def __init__(self, img):
        self.img = Image.open(img)
    
    def load(self):
        return self.img
    
    def crop(self):
        self.img = self.img.crop((0, 0, 150, 150)) 

    def turn(self):
        self.img = self.img.rotate(90)

    def save_img(self, image2):
        self.img.save(image2)
    