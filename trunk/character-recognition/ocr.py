import ocr
import PythonMagick
import image_utility
from training_data import TrainingData
from network import Network
from trainer import Trainer

#    #Here is an example of how to use Python Magick
#    image = PythonMagick.Image("images/a.png")
#    image_utility.set_color(image, 0, 0, 0, 0, 255)
#    image.scale("100x100")
#    image.display()
#
#    print image.fileName()
#    print image.magick()
#    print image.size().width()
#    print image.size().height()
#    print hex(255)
#    print hex(1)
class OCR:
    training_image_names = []
    training_images = []
    training_data = 0
    trainer = 0
    network = 0

    def __init__(self, training_image_names):
        # training image names are relative location of images
        self.training_image_names = training_image_names
        self.__load_images()
        self.__create_training_data()
        self.__initalize_network_and_trainer()
        
    def __load_images(self):
        for image_name in self.training_image_names:
            # create python magick image
            image = PythonMagick.Image(image_name)

            # scale the image
            image.scale("5x5")
            self.training_images.append(image)
        return

    def __create_training_data(self):
        training_data = TrainingData()
        i = 0
        for image in self.training_images:
            x = self.__serialize_image(image)
            d = [0.0 for j in range(len(self.training_images))]
            d[i] = 1.0
            training_data.add_dataset(x, d)
            i = i + 1

        self.training_data = training_data
        return

    def __initalize_network_and_trainer(self):
        training_data = self.training_data
        network = Network(25, [len(self.training_images)], 0.1, 0.1)
        trainer = Trainer(training_data, network, 0.015, 1500)
        self.trainer = trainer
        self.network = network
        return

    # This converts an image into a 1 dimentional binary string
    def __serialize_image(self, image):

        inputs = []
        for y in range(image.size().height()):
            for x in range(image.size().width()):
                # get the values for all color channels
                [r, g, b] = image_utility.get_color(image, x, y)

                # create normalized gray level pixel value 0.0 to 1.0
                gray_pixel = float(r + g + b) / (3.0 * 256.0)

                # Round value to 1 or floor it
                binary_pixel = gray_pixel
                if binary_pixel > 0.5:
                    binary_pixel = 0.5
                else:
                    binary_pixel = -0.5

                # store in array
                inputs.append(binary_pixel)
                
        return inputs
    
    def train(self):
        self.trainer.train()
        

    def test(self, image_name):
        # Input test image to the network
        print "Testing Image:" + image_name
        image = PythonMagick.Image(image_name)
        input = self.__serialize_image(image)
        output = self.network.calculate(input)

        print "Testing Input: " + str(input)
        print "Testing Output: " + str(output)


        # Find max value out of output (most likely)
        max_value = 0.0
        image_index = 0
        for i in range(len(output)):
            if output[i] > max_value:
                max_value = output[i]
                image_index = i

        binary_output = [0.0 for i in range(len(output))]
        binary_output[image_index] = 1.0

        print "Binary Output: " + str(binary_output) + "\n"
        return self.training_images[image_index]

if __name__ == "__main__":

    training_images = []
    training_images.append("images/a.png")
    training_images.append("images/b.png")
    training_images.append("images/c.png")
    training_images.append("images/d.png")
    training_images.append("images/e.png")

    ocr = OCR(training_images)
    ocr.train()
    image = ocr.test("images/a.png")
    image = ocr.test("images/b.png")
    image = ocr.test("images/c.png")
    image.scale("200x200")
    image.display()

    
