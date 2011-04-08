from neuron import Neuron

class Layer:
    """Test of a simple neuron layer"""
    
    def __init__(self, numInputs, size, gain, momentum):
        self.size = size
        self.numInputs = numInputs
        self.neurons = []

        for i in range(size):
            self.neurons.append(Neuron(numInputs, gain, momentum))

    def getNeurons(self):
        return self.neurons

    def getNeuronWeights(self):
        r = []
        for n in self.neurons:
            r.append(n.getWeights())
        return r

    def getSize(self):
        return self.size

    def learn(self, inputs, error):
        if len(inputs) != self.numInputs:
            print "Number of inputs", len(inputs), "does not match layer inputs", self.numInputs
            return
        if len(error) != len(self.neurons):
            print "Number of error factors", len(error), "does not match number of neurons", len(self.neurons)
            return
        for n, e in zip(self.neurons, error):
            n.learn(inputs, e)

    def calculate(self, inputs):
        output = []
        for neuron in self.neurons:
            output.append(neuron.calculate(inputs))
        return output

    def display(self):
        r = []
        for n in self.neurons:
            r.append(n.getWeights())
            r.append(n.getBias())
        return r
