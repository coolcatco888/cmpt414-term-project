__author__="cley"
__date__ ="$Mar 19, 2011 6:52:34 PM$"

from layer import Layer

class Network:
    n = 0               # number of inputs
    layer_sizes = []    # a list that specifies the size of all the
                        # intermediate layers eg. [40,40]
                        # specifies 1 hidden layer
                        # and 1 output layer, both with 40 neurons each
    
    layers = []         # holds all of the layers

    def __init__(self, n, layer_sizes):
        self.layer_sizes = layer_sizes
        
        #construct layers
        self.__construct_layers()

    def __construct_layers(self):
        number_of_layers = len(self.layer_sizes)
        for i in range(number_of_layers):
            # construct bottom layer
            if i == 0:
                self.layers.append(Layer(100, n))

            # construct hidden and output layers
            else:
                self.layers.append(Layer(self.layer_sizes[i - 1], self.layers(i - 1).get_size()))
        return

    # Use back propagation to learn
    # x - n inputs
    # d - list of desired outputs
    def learn(self, x, d):
        # calculate outputs for each layer
        output = []
        layer_outputs = []

        for i in range(len(self.layers)):
            layer = layers[i]
            output = 0

            if i == 0:
                # get outputs of first layer
                output = layer.calculate(x)
            else:
                # get outputs of hidden layers and final layer
                output = layer.calculate(output)

            #save outputs of each layer
            layer_outputs.append(output)
        
        layers_above_current_layer = []

        # this list holds all the errors for all layers above layer i
        errors = []
        for i in reversed(len(self.layers)):
            layer = self.layers[i]

            # if top layer calculate errors based on desired outputs
            if i == len(self.layers) - 1:
                errors = layer.calculate_error_terms_for_top_layer(layer_outputs[i], d)
            else:
                # TODO: refactor to pass in weights
                errors = layer.calculate_error_terms_for_hidden_layer(errors, layers_above_current_layer)

            layer.learn(x, errors);
            layers_above_current_layer.append(layer)
            break

    # calculate the final output based on an initial input set
    def calculate(self, inputs):
        for i in range(len(self.layers)):
            layer = layers[i]
            output = 0

            if i == 0:
                # get outputs of first layer
                output = layer.calculate(inputs)
            else:
                # get outputs of hidden layers and final layer
                output = layer.calculate(output)

        return output
