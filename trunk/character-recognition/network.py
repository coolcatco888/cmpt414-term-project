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
        self.n = n
        
        #construct layers
        self.__construct_layers()


    def __construct_layers(self):
        number_of_layers = len(self.layer_sizes)
        for i in range(number_of_layers):
            # construct bottom layer
            if i == 0:
                self.layers.append(Layer(self.layer_sizes[i], self.n))

            # construct hidden and output layers
            else:
                self.layers.append(Layer(self.layer_sizes[i], self.layers[i - 1].get_size()))
        return

    # Use back propagation to learn
    # x - n inputs
    # d - list of desired outputs
    def learn(self, x, d):
        # calculate outputs for each layer
        output = []
        layer_outputs = []

        for i in range(len(self.layers)):
            layer = self.layers[i]

            if i == 0:
                # get outputs of first layer
                output = layer.calculate(x)
            else:
                # get outputs of hidden layers and final layer
                output = layer.calculate(output)

            #save outputs of each layer
            layer_outputs.append(output)
        

        # Step 3 in notes sigma[Sk * Wjk] <- this is the sum of weights * error
        weights_times_error_sum = 0;
        for i in reversed(range(len(self.layers))):
            layer = self.layers[i]
            s = [] # error terms for current layer
            w = [] # a list weights for each node in the current layer

            # if top layer calculate errors based on desired outputs
            if i == len(self.layers) - 1:
                [s, w] = layer.calculate_error_terms_for_top_layer(layer_outputs[i], d)
            else:
                [s, w] = layer.calculate_error_terms_for_hidden_layer(weights_times_error_sum, layer_outputs[i])

            # calculate sigma[Sk * Wjk] in Step 3
            weights_times_error_sum += self.calculate_error_times_weights_for_layer(s, w)

            # determine inputs for current layer
            inputs = []
            if i > 0:
                inputs = layer_outputs[i - 1]
            else:
                inputs = x

            layer.learn(inputs, s);
            break

        return output

    # calculate weights * error for this layer
    # Step 3 in notes sigma[Sk * Wjk] <- this is the sum of weights * error
    def calculate_error_times_weights_for_layer(self, s, weights):
        sum = 0
        if len(s) == len(weights):
            for i in len(s):
                for wj in weights[i]:
                    sum += s[i] * wj
        return sum

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
