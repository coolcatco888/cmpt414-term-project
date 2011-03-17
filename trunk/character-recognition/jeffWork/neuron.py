from random import random, uniform
from math import e

import numpy as np
import matplotlib.pyplot as plot

class Neuron:
    """Test of simplified 'forgetful' neuron"""
    
    #Gains of 0.0 prevent learning for the specified number
    #Determines the size of weight changes when this neuron is told to learn
    wGain = 0.0
    #Derermines the size of threshold changes when this neuron is told to learn
    tGain = 0.0
    
    #Number of inputs this neuron can handle
    numInputs = 0

    #Indicates how certain this neuron must be before it fires
    threshold = 0.0

    #The strength of connection this neuron has to it's inputs
    weights = []

    #Old weights used for the momentum term
    old = []

    #Remembers the last inputs that went through this neuron
    inputs = []

    #Remembers the last output that this neuron spat out
    output = 0.0

    #Remembers the error term for this neuron
    error = 0.0

    #Initializes a neuron with these arguments
    #It is strongly recomended that you set tGain to zero
    def __init__(self, numInputs, wGain, tGain):
        #print "Initializing neuron"
        self.numInputs = numInputs
        #print "    Number of inputs:", self.numInputs
        self.weights = [random() for i in range(numInputs)]
        self.old = self.weights
        #print "    Initial weights are:", self.weights
        self.threshold = random()
        #print "    Initial threshold is:", self.threshold
        self.wGain = wGain
        #print "    Initial weights gain is:", self.wGain
        self.tGain = tGain
        #print "    Initial threshold gain is:", self.tGain
        #print "Neuron initialized"
        #print

    def getNumInputs(self):
        return self.numInputs

    def setWeights(self, weights):
        """Only use this to set weights to some exact numbers"""
        """This function is not used to make this neuron learn"""
        #print "Setting weights to:", weights
        self.weights = weights

    def getWeights(self):
        return self.weights

    def getOldWeights(self):
        return self.old

    def setThreshold(self, threshold):
        #print "Setting threshold to:", threshold
        self.threshold = threshold

    def getThreshold(self):
        return self.threshold

    def setWeightsGain(self, wGain):
        #print "Setting weights gain to:", wGain
        self.wGain = wGain

    def getWeightsGain(self):
        return wGain

    def setThresholdGain(self, tGain):
        #print "Setting threshold gain to:", tGain
        self.tGain = tGain

    def getThresholdGain(self):
        return self.tGain

    def setErrorTerm(self, error):
        self.error = error

    def getErrorTerm(self):
        return self.error

    #NOTE: I don't think I should set inputs, might later
    def getLastInputs(self):
        return self.inputs

    def getLastOutput(self):
        return self.output

    def neurate(self, inputs):
        #print "Neurating output from:", inputs
        self.inputs = inputs
        if len(inputs) != len(self.weights):
            #print "    Incorrect number of inputs"
            #print "Neuration complete (but incorrect)"
            #print
            return 0.0
        
        s = 0.0
        #Test at what length of inputs this cacheing leads to performance gains
        threshold = self.threshold
        weights = self.weights
        #print "    Beginning accumulation"
        for i in range(self.numInputs):
            tmp = weights[i] * inputs[i] - threshold
            s = s + tmp
            #print "        w[", i, "] =", weights[i]
            #print "        i[", i, "] =", inputs[i]
            #print "        t      =", threshold
            #print "        w[", i, "] * i[", i, "] - t =", tmp
            #print "        Running sum =", s
        #print "    Accumulation result =", s

        r = self.sigmoid(s)
        #print "    Sigmoid(", s, ") =", r
        #print "Neuration complete"
        #print
        self.output = r
        return r

    def hardLimit(self, a):
        if a < 0.0:
            return -1.0
        else:
            return 1.0

    def sigmoid(self, a):
        return 1 / (1 + e ** -(a - self.threshold))

    def learn(self):
        #NOTE: This is dangerous, will only work properly after neurate is run and the error term is set
        #NOTE: Perhaps have an automatic way for the error term to be set from this... perhaps using links
        #      and specific types of neurons (ie: hidden and output neurons)
        #print "Learning"
        weights = self.weights
        #print "    Old weights were:", weights
        old = self.old
        momentum = [w - o for w, o in zip(weights, old)]
        self.old = weights
        #print "    Momentum differences:", momentum
        #Test at which number of inputs this cacheing leads to performance gains
        g = self.wGain
        #print "    Weight gain is:", g
        e = self.error
        #print "    Error term is:", e
        inputs = self.inputs
        #print "    Last inputs were:", inputs
        a = 0.0
        #newWeights = [w + g * e * i for w, i in zip(weights, inputs)]
        newWeights = [w + g * e * i + a * m for w, i, m in zip(weights, inputs, momentum)]
        #print "    New weights are:", newWeights
        self.setWeights(newWeights)
        t = self.threshold
        #print "    Old threshold was:", t
        g = self.tGain
        #print "    Threshold gain is:", g
        #NOTE: I think that changing f from random to a constant value will change
        #      (in a good way) the convergance of the thresholds
        #f = random()
        #print "    Gain 'input' is:", f
        #newThreshold = t + g * e * f
        newThreshold = t + g * e
        #print "    New threshold is:", newThreshold
        self.setThreshold(newThreshold)
        #print "Learning complete"
        #print
        

if __name__ == "__main__":
    def nextFailColour((r, g, b), step):
        r = r + step
        if r > 1.0:
            r = 0.0
            g = g + step
        if g > 1.0:
            g = 0.0
            b = b + step
        if b > 1.0:
            b = 0.0
        return (r, g, b)

    neuron = Neuron(2, 0.1, 0.0)
    #A sigmoid neuron will always be wrong by some small margine, can only train with a number of steps
    trainSteps = 10000
    #Will display a line once every this many steps
    lineEvery = 100

    oWeights = []
    nWeights = neuron.getWeights()

    xRange = np.arange(-10.0, 10.5, 0.5)
    failR = 0.0
    failG = 0.0
    failB = 0.0
    failStep = 0.1
    failColour = (failR, failG, failB)
    failFactor = 10.0
    for i in range(trainSteps):
        x = uniform(-10.0, 10.0)
        y = uniform(-10.0, 10.0)

        if x > y:
            dOut = 0.0
            plot.plot(x, y, 'bx')
        else:
            dOut = 1.0
            plot.plot(x, y, 'ro')

        #It seems that a list is more appropriate than a tuple...don't know why though
        aOut = neuron.neurate([x, y])
        #print "Desire output:", dOut
        #print "Actual output:", aOut
        #print
        oWeights = nWeights
        error = aOut * (1 - aOut) * (dOut - aOut)
        #print "Setting error:", error
        neuron.setErrorTerm(error)
        neuron.learn()
        nWeights = neuron.getWeights()
        #print "    Old weights:", oWeights
        #print "    New weights:", nWeights
        if i % lineEvery == 0:
            #Every lineEvery steps, draw the new line
            failColour = nextFailColour(failColour, failStep)
            slope = -nWeights[0] / nWeights[1]
            intercept = neuron.getThreshold() / nWeights[1]
            plot.plot(xRange, slope * xRange + intercept, 'k', c = failColour, alpha = 0.333)

    finWeights = neuron.getWeights()
    finThresh = neuron.getThreshold()
    #print "Final weights:", finWeights
    #print "Final threshold:", finThresh
    slope = -finWeights[0] / finWeights[1]
    intercept = neuron.getThreshold() / finWeights[1]
    #print "Final decision boundary:"
    #print "    Intercept:", intercept
    #print "    Slope:", slope
    failColour = nextFailColour(failColour, failStep)
    plot.plot(xRange, slope * xRange + intercept, 'k', lw = 3, c = failColour)
    plot.axis([-10, 10, -10, 10])
    plot.show()

