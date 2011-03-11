from random import random, uniform
import numpy as np
import matplotlib.pyplot as plt

class SingleLayerPerceptron:
    """Initial test of perceptron"""
    
    #NOTE: Organize these, perhaps alphabetically

    numInputs = 0

    threshold = 0

    time = 0

    weights = []

    inputs = []

    output = []
    
    def __init__(self, numInputs):
        self.numInputs = numInputs
        print self.numInputs, "Input Perceptron Initialized"
        self.time = 0
        print "Time initialized to", self.time
        self.setWeights([random() for i in range(numInputs)], self.time)
        print "Weights[", self.time, "] initialized to", self.getWeights(self.time)
        self.setThreshold(random())
        #self.setThreshold(0.0)
        print "Threshold initialized to", self.getThreshold()

    #NOTE: Can never change the number of inputs, only retrieve
    def getNumInputs(self):
        return self.numInputs

    def setWeights(self, weights, time = float('Inf')):
        if len(weights) != self.numInputs:
            print "Incorrect number of weights"
            print "NOTE: Insert error handling here"
            return
        for w in weights:
            if not isinstance(w, float):
                print "All weights must be floating point numbers"
                print "NOTE: Insert error handling here"
                return
        if not isinstance(time, int) and time != float('Inf'):
            print "Time must be an integer"
            print "NOTE: Insert error handling here"
            return
        if time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        if time >= len(self.weights):
            self.weights.append(weights)
        else:
            self.weights[time] = weights
    
    def getWeights(self, time = float('Inf')):
        if not isinstance(time, int) and time != float('Inf'):
            print "Time must be an integer"
            print "NOTE: Insert error handling here"
            return
        if time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        if time >= len(self.weights):
            return self.weights
        return self.weights[time]
    
    def setInputs(self, inputs, time = float('Inf')):
        if len(inputs) != self.numInputs:
            print "Incorrect number of inputs"
            print "NOTE: Insert error handling here"
            return
        for i in inputs:
            if not isinstance(i, float):
                print "All inputs must be floating point numbers"
                print "NOTE: Insert error handling here"
                return
        if not isinstance(time, int) and time != float('Inf'):
            print "Time must be an integer"
            print "NOTE: Insert error handling here"
            return
        if time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        if time >= len(self.inputs):
            self.inputs.append(inputs)
        else:
            self.inputs[time] = inputs

    def getInputs(self, time = float('Inf')):
        if not isinstance(time, int) and time != float('Inf'):
            print "Time must be an integer"
            print "NOTE: Insert error handling here"
            return
        if time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        if time >= len(self.inputs):
            return self.inputs
        return self.inputs[time]

    def setThreshold(self, threshold):
        if not isinstance(threshold, float):
            print "Threshold must be a floating point number"
            print "NOTE: Insert error handling here"
            return 
        self.threshold = threshold

    def getThreshold(self):
        return self.threshold

    def setTime(self, time):
        #NOTE: This function is dangerous for the functioning of the neural network
        #      For "normal" functioning, time only increases one step at a time
        if not isinstance(time, int) or time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        self.time = time

    def incrementTime(self):
        #NOTE: A safer way to increment time
        self.time = self.time + 1

    def getTime(self):
        return self.time

    def calcOutput(self, time = float('Inf')):
        if not isinstance(time, int) and time != float('Inf'):
            print "Time must be an integer"
            print "NOTE: Insert error handling here"
            return
        if time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        #Ensure that we have inputs and weights for this timestep
        if len(self.weights) != len(self.inputs):
            print "This perceptron has non-matching inputs and weights"
            print "NOTE: Insert error handling here"
            return
        #If the time is too large or not used, calc the latest output
        if time > len(self.weights):
            time = self.getTime()
        if len(self.weights) - 1 < time:
            print "This perceptron doesn't currently have weights for time", time
            print "NOTE: Insert error handling here"
            return
        if len(self.inputs) - 1 < time:
            print "This perceptron doesn't currently have inputs for time", time
            print "NOTE: Insert error handling here"
            return
        
        s = 0.0
        thresh = self.getThreshold()
        weights = self.getWeights(time)
        inputs = self.getInputs(time)

        for i in range(self.numInputs):
            s = s + (weights[i] * inputs[i] - thresh)

        #NOTE: Currently using the hard limit non-linearity
        #NOTE: In addition to appending to the output list
        #      Perhaps we should have this return y(self.getTime())
        #print "Summation before non-linearity is", s
        if s < 0.0:
            self.output.append(-1.0)
        else:
            self.output.append(1.0)

    def getOutput(self, time = float('Inf')):
        if not isinstance(time, int) and time != float('Inf'):
            print "Time must be an integer"
            print "NOTE: Insert error handling here"
            return
        if time < 0:
            print "Time must be a positive integer"
            print "NOTE: Insert error handling here"
            return
        if time >= len(self.output):
            return self.output
        return self.output[time]

if __name__ == "__main__":
    #Attempting to make a perceptron to divide the x, y plane along y = x
    #print "--------"
    #print "STEP ONE"
    #print "--------"
    #Initialize our important values
    percep = SingleLayerPerceptron(2)
    steps = 1000
    desiredOut = []
    for step in range(steps):
        #print "--------"
        #print "STEP TWO"
        #print "--------"
        
        #Present one set of inputs with desired output
        #Halfplane above y = x is output 1
        #Halfplane below y = x is output -1
        #So yeah, if x > y, output -1, otherwise 1
        #Input list is a vector [x, y]
        x = uniform(-10.0, 10.0)
        y = uniform(-10.0, 10.0)
        newInput = [x, y]

        if x > y:
            desiredOut.append(-1.0)
        else:
            desiredOut.append(1.0)

        percep.setInputs(newInput)
        time = percep.getTime()
        print "Inputs(", time, ") =", percep.getInputs(time)
        print "Desire(", time, ") =", desiredOut[time]

        #print "----------"
        #print "STEP THREE"
        #print "----------"

        percep.calcOutput()
        print "Output(", time, ") =", percep.getOutput(time)

        #print "---------"
        #print "STEP FOUR"
        #print "---------"
        #NOTE: Fiddle with the gain fraction

        gainFraction = 0.001

        percep.incrementTime()
        time = percep.getTime()
        print "Current time =", time

        oldWeights = percep.getWeights(time - 1)
        oldInputs = percep.getInputs(time - 1)

        outDiff = desiredOut[time - 1] - percep.getOutput(time - 1)

        newWeights = [(oldWeights[i] + gainFraction * outDiff * oldInputs[i]) for i in range(percep.getNumInputs())]
        percep.setWeights(newWeights)
        
        changed = False
        if oldWeights != newWeights:
            print "Old weights were", oldWeights
            print "New weights are ", newWeights
            changed = True
        else:
            print "Network proper"
        
        #NOTE: DANGEROUS; Breaks when the perceptron has numInputs != 2
        slope = -newWeights[0] / newWeights[1]
        intercept = percep.getThreshold() / newWeights[1]
        print "Boundary(", time, ") = y =", slope, "* x +", intercept
        xs = np.arange(-10.0, 10.5, 0.5)
        if changed:
            colour = 1.0 - (float(step) / float(steps))
            colour = (colour, colour, colour)
            plt.plot(xs, slope * xs + intercept, 'k', c = colour)
        if desiredOut[time - 1] == 1.0:
            plt.plot(oldInputs[0], oldInputs[1], 'ro')
        else:
            plt.plot(oldInputs[0], oldInputs[1], 'bx')
    finTime = percep.getTime()
    finWeights = percep.getWeights(finTime)
    print "Weights(", finTime, ") =", finWeights
    slope = -finWeights[0] / finWeights[1]
    intercept = percep.getThreshold() / finWeights[1]
    xs = np.arange(-10.0, 10.5, 0.5)
    plt.plot(xs, slope * xs + intercept, 'k', lw = 3, c = (1.0, 0.0, 0.0))
    plt.axis([-10, 10, -10, 10])
    plt.show()
