import ocr
import PythonMagick
import image_utility
from training_data import TrainingData
from network import Network
from trainer import Trainer
import pickle

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

    training_images = []
    training_data = 0
    trainer = 0
    network = 0

    def __init__(self):
        self.training_images = []
        self.training_data = 0
        self.trainer = 0
        self.network = 0

        

    def load_training_images(self, training_image_names):
        self.__load_images(training_image_names)
        self.training_data = self.__create_training_data()
        
    def __load_images(self, training_image_names):
        training_images = []
        for image_name in training_image_names:
            # create python magick image
            image = PythonMagick.Image(image_name)

            # scale the image
            image = image_utility.resize(image, 5, 5)
            training_images.append(image)

        self.training_images = training_images

    def __create_training_data(self):
        training_data = TrainingData()
        i = 0
        for image in self.training_images:
            x = self.__serialize_image(image)
            d = [0.0 for j in range(len(self.training_images))]
            d[i] = 1.0
            training_data.add_dataset(x, d)
            i = i + 1

        return training_data
        

    def initialize_network(self):
        network = Network(25, [len(self.training_images)], 0.1, 0.1)
        self.network = network

    def initalize_trainer(self):
        training_data = self.training_data
        network = self.network
        trainer = Trainer(training_data, network, 0.0005, 1500)
        self.trainer = trainer

    def initalize_network_and_trainer(self):
        self.initialize_network()
        self.initalize_trainer()
        
        

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
                    binary_pixel = 1.0
                else:
                    binary_pixel = 0.0

                # store in array
                inputs.append(binary_pixel)
                
        return inputs

    def get_network(self):
        return self.network

    def set_network(self, network):
        self.network = network
    
    def train(self):
        self.trainer.train()

    def test(self, image_name):
        # Input test image to the network
        print "Testing Image: " + image_name
        image = PythonMagick.Image(image_name)
        image = image_utility.resize(image, 5, 5)
        print "Size: " + str(image.size().width()) + "x" + str(image.size().height())
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

    ocr = OCR()
    ocr.load_training_images(training_images)
    ocr.initalize_network_and_trainer()
    ocr.train()

    network = ocr.get_network()
    filehandler = open("network.txt", 'w')
    pickle.dump(network, filehandler)
    filehandler = open("network.txt", 'r')
    network = pickle.load(filehandler)
    ocr.set_network(network)

    image = ocr.test("images/a.png")
    image = ocr.test("images/b.png")
    image = ocr.test("images/c.png")
    image.scale("200x200")
    image.display()

    