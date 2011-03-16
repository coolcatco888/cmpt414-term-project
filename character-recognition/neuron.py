from random import random, uniform
import numpy as np
import matplotlib.pyplot as plot

class Neuron:
    """Test of simplified 'forgetful' neuron"""
    
    #Determines the size of weight changes when this neuron is told to learn
    gain = 0.0
    
    #Number of inputs this neuron can handle
    numInputs = 0

    #Indicates how certain this neuron must be before it fires
    threshold = 0.0

    #The strength of connection this neuron has to it's inputs
    weights = []

    def __init__(self, numInputs, gain):
        print "Initializing neuron"
        self.numInputs = numInputs
        print "    Number of inputs:", self.numInputs
        self.weights = [random() for i in range(numInputs)]
        print "    Initial weights are:", self.weights
        self.threshold = random()
        print "    Initial threshold is:", self.threshold
        self.gain = gain
        print "    Initial gain is:", self.gain
        print "Neuron initialized"
        print

    def getNumInputs(self):
        return self.numInputs

    def setWeights(self, weights):
        """Only use this to set weights to some exact numbers"""
        """This function is not used to make this neuron learn"""
        #print "Setting weights to:", weights
        self.weights = weights

    def getWeights(self):
        return self.weights

    #Experiment with manipulating thresholds
    def setThreshold(self, threshold):
        print "Setting threshold to:", threshold
        self.threshold = threshold

    def getThreshold(self):
        return self.threshold

    #Experiment with manipulating gains
    def setGain(self, gain):
        print "Setting gain to:", gain
        self.gain = gain

    def getGain(self):
        return gain

    def neurate(self, inputs):
        #print "Neurating output from:", inputs
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

        r = self.hardLimit(s)
        #print "    Hardlimit(", s, ") =", r
        #print "Neuration complete"
        #print
        return r

    def hardLimit(self, i):
        if i < 0.0:
            return -1.0
        else:
            return 1.0

    def learn(self, inputs, dOut, aOut):
        #print "Learning"
        weights = self.getWeights()
        #print "    Old weights were:", weights
        #Test at which number of inputs this cacheing leads to performance gains
        g = self.gain
        #print "    Gain is:", g
        d = dOut - aOut
        #print "    Desired output is:", dOut
        #print "    Actual output is:", aOut
        newWeights = [w + g * d * i for w, i in zip(weights, inputs)]
        #print "    New weights are:", newWeights
        self.setWeights(newWeights)
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

    neuron = Neuron(2, 0.01)
    #An input set takes a lot of memory, a cheaper solution is to run until x steps pass without learning
    #This neuron must learn until it makes success successful decisions in a row
    success = 500
    progress = 0
    total = 0
    fails = 0

    oWeights = []
    nWeights = neuron.getWeights()

    xRange = np.arange(-10.0, 10.5, 0.5)
    failR = 0.0
    failG = 0.0
    failB = 0.0
    failStep = 0.1
    failColour = (failR, failG, failB)
    failFactor = 10.0
    while progress <= success:
        progress = progress + 1
        total = total + 1
        x = uniform(-10.0, 10.0)
        y = uniform(-10.0, 10.0)

        if x > y:
            dOut = -1.0
            plot.plot(x, y, 'bx')
        else:
            dOut = 1.0
            plot.plot(x, y, 'ro')

        #It seems that a list is more appropriate than a tuple...don't know why though
        aOut = neuron.neurate([x, y])
        print "Desire output:", dOut
        print "Actual output:", aOut
        print
        oWeights = nWeights
        neuron.learn([x, y], dOut, aOut)
        nWeights = neuron.getWeights()
        if oWeights != nWeights:
            print "Weights changed:"
            print "    Old weights:", oWeights
            print "    New weights:", nWeights
            failColour = nextFailColour(failColour, failStep)
            slope = -nWeights[0] / nWeights[1]
            intercept = neuron.getThreshold() / nWeights[1]
            tempColour = (failColour[0] / failFactor, failColour[1] / failFactor, failColour[2] / failFactor)
            plot.plot(xRange, slope * xRange + intercept, 'k', c = tempColour)
            print "Resetting progress"
            progress = 0
            fails = 0
        else:
            print "Weights acceptable:"
            print "    Weights:", nWeights
            print "Progress:", progress

    finWeights = neuron.getWeights()
    print "Total steps:", total
    print "Total fails:", fails
    print "Final weights:", finWeights
    slope = -finWeights[0] / finWeights[1]
    intercept = neuron.getThreshold() / finWeights[1]
    failColour = nextFailColour(failColour, failStep)
    plot.plot(xRange, slope * xRange + intercept, 'k', lw = 3, c = failColour)
    plot.axis([-10, 10, -10, 10])
    plot.show()

