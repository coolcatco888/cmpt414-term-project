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
        errors = []
        s = []
        y = output

        if len(output) == len(self.neurons):
            for i in len(output):
                s.append(y[i] * (1.0 - y[i]) * (d[i] - y[i]))
        errors.append(s)
        return errors

    # errors - error terms for all neurons above this layer
    # layers - reference to the list of layers for the network
    def calculate_error_terms_for_hidden_layer(self, errors, layers_above):
        return

    def calculate(self, inputs):
        output = []
        for neuron in self.neurons:
            output.append(neuron.calculate(inputs))
        return