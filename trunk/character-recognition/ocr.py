import PythonMagick


class ocr:
    training_image_names = []
    training_images = []

    def __init__(self, training_images):
        self.training_image_names = training_image_names
        self.__process_images_for_network()

        
    def __process_images_for_network(self):
        for image_name in self.training_image_names:
            img = PythonMagick.Image(image_name)
            self.training_images.append(img)
        return
    
    def train(self):
        return

    def test(self):
        return

if __name__ == "__main__":

    training_images = []
    training_images.append("images/a.png")

    image = PythonMagick.Image("images/a.png")
    image.scale("100x100")
    image.display()
    print image.fileName()
    print image.magick()
    print image.size().width()
    print image.size().height()


