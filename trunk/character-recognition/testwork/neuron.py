from random import random
from math import e

class Neuron:
    """Test of simplified 'forgetful' neuron"""
    
    #Number of inputs this neuron can handle
    numInputs = 0

    #Indicates how certain this neuron must be before it fires
    threshold = 0.0

    #The strength of connection this neuron has to it's inputs
    weights = []

    #The gain factors for weights and the threshold
    wGain = 0.0
    tGain = 0.0
    
    #Initializes a neuron with these arguments
    #It is strongly recomended that you set tGain to zero
    def __init__(self, numInputs, wGain, tGain):
        self.numInputs = numInputs
        self.weights = [random() for i in range(numInputs)]
        self.threshold = random()
        self.wGain = wGain
        self.tGain = tGain

    def getNumInputs(self):
        return self.numInputs

    def getWeights(self):
        return self.weights

    def getThreshold(self):
        return self.threshold

    def getWeightsGain(self):
        return wGain

    def getThresholdGain(self):
        return self.tGain

    def calculate(self, inputs):
        print "Neuron", self, "calculating", inputs
        self.inputs = inputs
        if len(inputs) != len(self.weights):
            return 0.0
        
        s = 0.0
        for i in range(self.numInputs):
            s = s + self.weights[i] * inputs[i]
            print "    Running sum", s
        
        print "    Subtracting threshold", self.threshold
        r = self.sigmoid(s - self.threshold)
        print "    Sigmoid result", r
        return r

    def learn(self, inputs, error):
        print "Neuron", self, "learning for inputs", inputs, "with error", error
        print "    Old weights were", self.weights
        self.weights = [w + self.wGain * error * i for w, i in zip(self.weights, inputs)]
        print "    New weights are", self.weights
        print "    Old threshold was", self.threshold
        self.threshold = self.threshold - self.tGain * error
        print "    New threshold is", self.threshold

    def sigmoid(self, x):
        return 1 / (1 + (e ** -x))
