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
        self.moment = moment

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
        self.inputs = inputs
        if len(inputs) != len(self.weights):
            return 0.0
        
        s = 0.0
        for i in range(self.numInputs):
            s = s + self.weights[i] * inputs[i]

        return self.sigmoid(s - self.threshold)

    def learn(self, inputs, error):
        self.setWeights([w + self.wGain * error * i for w, i in zip(self.weights, inputs)])
        self.setThreshold(self.threshold - self.tGain * error)

    def sigmoid(self, x):
        return 1 / (1 + (e ** -a))
