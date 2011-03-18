from neuron import Neuron

from random import random, uniform, seed
import matplotlib.pyplot as plot
import numpy as np

class StripPer:
    """WARNING: THIS CLASS IS VERY VERY HARDCODED RIGHT NOW, FIX LATER"""
    """Tries to make a very simple perceptron that can detect strips on a plane"""

    #For now, do not put layers into a list, just keep them hard coded and easy
    #NOTE: Find a better way to placehold these until initialization
    #NOTE: A list will probably fix this
    bottomLeft = 0
    bottomRight = 0

    topLeft = 0
    topRight = 0

    def __init__(self):
        #print "Initializing strip perceptron"
        self.bottomLeft = Neuron(2, 0.1, 0.0, 0.0)
        self.bottomRight = Neuron(2, 0.1, 0.0, 0.0)
        self.topLeft = Neuron(2, 0.01, 0.0, 0.0)
        self.topRight = Neuron(2, 0.01, 0.0, 0.0)
        #print "Neurons initialized"
        #print

    def getLeft(self):
        return self.bottomLeft

    def getRight(self):
        return self.bottomRight

    def getTopLeft(self):
        return self.topLeft

    def getTopRight(self):
        return self.topRight

    def neurate(self, inputs):
        #print "Attempting to neurate:", inputs
        if len(inputs) != 2:
            return 0.0

        lResult = self.bottomLeft.neurate(inputs)
        #print "    Left result:", lResult
        rResult = self.bottomRight.neurate(inputs)
        #print "    Right result:", rResult

        lFinal = self.topLeft.neurate([lResult, rResult])
        rFinal = self.topRight.neurate([lResult, rResult])
        #print "Final result:", result
        #print

        return [lFinal, rFinal]

    def learn(self, dOut):
        #NOTE: Will probably have to implement the sigmoid non-linearity
        
        #First, teach top
        #For this seriously hardcoded example, 0 is left, 1 is right
        #print "Learning:"
        #print "    Desired:", dOut
        lOut = self.topLeft.getLastOutput()
        rOut = self.topRight.getLastOutput()
        #print "    Actual:", aOut
        topLeftError = lOut * (1.0 - lOut) * (dOut[0] - lOut)
        topRightError = rOut * (1.0 - rOut) * (dOut[1] - rOut)
        #print "    Setting top error:", topError
        self.topLeft.setErrorTerm(topLeftError)
        self.topRight.setErrorTerm(topRightError)
        #print "    Top learning:"
        self.topLeft.learn()
        self.topRight.learn()

        #Now teach bottoms
        topLeftWeights = self.topLeft.getWeights()
        topRightWeights = self.topRight.getWeights()
        
        lOut = self.bottomLeft.getLastOutput()
        #print "    Left output was:", lOut
        s = (topLeftError * topLeftWeights[0]) + (topRightError * topRightWeights[0])
        lError = lOut * (1.0 - lOut) * s
        #print "    Setting left error:", lError
        self.bottomLeft.setErrorTerm(lError)
        #print "    Left learning:"
        self.bottomLeft.learn()

        rOut = self.bottomRight.getLastOutput()
        #print "    Right output was:", rOut
        s = (topLeftError * topLeftWeights[1]) + (topRightError * topRightWeights[1])
        rError = rOut * (1.0 - rOut) * s
        #print "    Setting right error:", rError
        self.bottomRight.setErrorTerm(rError)
        #print "    Right learning:"
        self.bottomRight.learn()
        #print "Learned:"
        #print

if __name__ == "__main__":
    #Initialize our 'StripPer'
    stripper = StripPer()
    
    setSize = 10000
    dispEvery = 1

    #for i in range(trains):
    lowLimit = -10.0
    highLimit = 10.0
    
    errors = 0.0
    acceptableError = 0.005
    unacceptableError = 1.0
    errorRate = 1.0
   
    plot.ion()
    while errorRate >= acceptableError:
        errors = 0.0
        seed()
        for i in range(setSize):
            #if i % dispEvery == 0:
                #print i, "/", trains
            #print "Train step:", i
    
            x = uniform(lowLimit, highLimit)
            y = uniform(lowLimit, highLimit)
    
            dOut = [0.0, 1.0]
            if x > 0.0 and y > 0.0:
                dOut = [1.0, 0.0]
         
            #print "Inputs:", [x, y]        
            #print "Desired:", dOut
     
            aOut = stripper.neurate([x, y])
            stripper.learn(dOut)
            bOut = [0.0, 0.0]
            if aOut[0] > aOut[1]:
                bOut = [1.0, 0.0]
            else:
                bOut = [0.0, 1.0]
            if dOut != bOut:
                errors = errors + 1.0
            errorRate = errors / setSize
            if i % dispEvery == 0:
                print errorRate, "\t",dOut, "\t", bOut, "\t", aOut, "\t", x, "\t", y

        leftWeights = stripper.getLeft().getWeights()
        leftSlope = -leftWeights[0] / leftWeights[1]
        leftInt = stripper.getLeft().getThreshold() / leftWeights[1]
     
        rightWeights = stripper.getRight().getWeights()
        rightSlope = -rightWeights[0] / rightWeights[1]
        rightInt = stripper.getRight().getThreshold() / rightWeights[1]
    
        xs = np.arange(-10.0, 10.5, 0.5)
        plot.plot(xs, leftSlope * xs + leftInt, '-', c = (0.5, 0.0, 0.0), alpha = 0.1)
        plot.plot(xs, rightSlope * xs + rightInt, '-', c = (0.0, 0.0, 0.5), alpha = 0.1)
        plot.axis([-10, 10, -10, 10])
        plot.draw()

        if errorRate > unacceptableError:
            print "Perceptron is diverging violently, restarting the reactor"
            stripper = StripPer()
    
    #print "Training complete:"
    
    testPoints = 1000

    #print "Test points:", testPoints
    for i in range(testPoints):
        x = uniform(-10.0, 10.0)
        y = uniform(-10.0, 10.0)

        #print "    Testing:", [x, y]

        aOut = stripper.neurate([x, y])
        #print "    Actual:", aOut
        if aOut[0] > aOut[1]:
            colour = (1.0, 0.0, 0.0)
        else:
            colour = (0.0, 0.0, 1.0)
        plot.plot(x, y, 'x', c = colour)
    
    leftWeights = stripper.getLeft().getWeights()
    leftSlope = -leftWeights[0] / leftWeights[1]
    leftInt = stripper.getLeft().getThreshold() / leftWeights[1]
    
    rightWeights = stripper.getRight().getWeights()
    rightSlope = -rightWeights[0] / rightWeights[1]
    rightInt = stripper.getRight().getThreshold() / rightWeights[1]

    xs = np.arange(-10.0, 10.5, 0.5)
    plot.plot(xs, leftSlope * xs + leftInt, 'r-', lw = 3)
    plot.plot(xs, rightSlope * xs + rightInt, 'b-', lw = 3)
   
    plot.ioff()
     
    plot.axis([-10, 10, -10, 10])
    plot.show()
