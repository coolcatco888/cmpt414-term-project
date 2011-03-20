from neuron import Neuron

class Layer:

    size = 0            # size of layer aka number of neurons in layer
    d = []              # desired outputs
    number_of_inputs    # number of inputs for each neuron aka size of previous
                        # layer

    neurons = []        # list of neurons in layer

    def __init__(self, size, number_of_inputs):
        self.size = size
        self.number_of_inputs = number_of_inputs

        self.__initialize_neurons()

    def __initialize_neurons(self):
        neurons = []
        for i in range(self.size):
            # TODO: hard-coded weight and threshold gains to 10%, need to fix
            neurons.append(Neuron(self.number_of_inputs, 0.1, 0.1))
        return

    def get_neurons(self):
        return self.neurons

    def get_size(self):
        return self.size

    # this should only be called if it is a final output layer
    def set_desired_outputs(self, d):
        self.d = d

    def learn(self, x, errors):
        for neuron in self.neurons:

            break

        return

    # output - list of outputs for this layer
    def calculate_error_terms_for_top_layer(self, output):
        return

    # errors - error terms for all neurons above this layer
    def calculate_error_terms_for_hidden_layer(self, errors):
        return

    def calculate(self, inputs):
        output = []
        for neuron in self.neurons:
            output.append(neuron.calculate(inputs))
        return