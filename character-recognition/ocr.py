import ocr
import PythonMagick
import image_utility

#    #Here is an example of how to use Python Magick
#    image = PythonMagick.Image("images/a.png")
#    image.scale("100x100")
#    image.pixelColor( 0, 0, "red" );
#    image.display()
#    print image.fileName()
#    print image.magick()
#    print image.size().width()
#    print image.size().height()
class OCR:
    training_image_names = []
    training_images = []

    def __init__(self, training_image_names):
        self.training_image_names = training_image_names
        self.__load_images()
        self.__serialize_images()
        
    def __load_images(self):
        for image_name in self.training_image_names:
            img = PythonMagick.Image(image_name)
            self.training_images.append(img)
        return

    def __serialize_images(self):
        return
    
    def train(self):
        return

    def test(self):
        return

if __name__ == "__main__":

    training_images = []
    training_images.append("images/a.png")
    training_images.append("images/b.png")
    training_images.append("images/c.png")
    training_images.append("images/d.png")
    training_images.append("images/e.png")

    ocr = OCR(training_images)
    ocr.train()


    #Here is an example of how to use Python Magick
    image = PythonMagick.Image("images/a.png")
    image_utility.set_color(image, 0, 0, 0, 0, 255)
    image.scale("100x100")
    image.display()

    print image.fileName()
    print image.magick()
    print image.size().width()
    print image.size().height()
    print hex(255)
    print hex(1)