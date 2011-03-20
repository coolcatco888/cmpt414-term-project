__author__="cley"
__date__ ="$Mar 19, 2011 6:52:34 PM$"

from layer import Layer

class Network:
    n = 0               # number of inputs
    layer_sizes = []    # a ist that specifies the size of all the
                        # intermediate layers eg. [40,40]
                        # specifies 2 intermediate layers with 40 neurons
    
    max_time = 1000     # maximum number of time steps
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
                # TODO: construct layers here
                break

            # construct top output layer
            elif i == (number_of_layers - 1):
                break

            # construct middler layer
            else:
                break
        return

    # Use back propagation to learn
    # x - n inputs
    # d - list of desired outputs
    def learn(self, x, d):
        # set desired output for last layer
        layer = self.layers[(len(self.layers) - 1)]
        layer.set_desired_outputs(d)

        # set x as first output
        output = x

        # for each time step t
        for t in range(self.max_time):
            for layer in self.layers:
                # TODO: call learn function for each layer here
                break

    # calculate the final output based on an initial input set
    def calculate(self, inputs):
        # set desired output for last layer
        layer = self.layers[0]
        output = layer.calculate(inputs)

        for layer in self.layers:
            output = layer.calculate(output)

        return output
