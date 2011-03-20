__author__="cley"
__date__ ="$Mar 19, 2011 6:52:34 PM$"

from layer import Layer

class Network:

    x = [[]]
    d = []
    maxTime = 1000

    layers = []

    def __init__(self, x, d):

        # initialize object
        self.x = x
        self.d = d

        #construct layers
        self.__construct_layers()

    def __construct_layers(self):
        for i in range(3):
            if i == 0:
                # TODO: construct nodes
                break
            elif i == 3:
                break
            else
                break
        return

    # Use back propagation to learn
    def learn(self):
        #for each input set
        for j in range(len(x[0])):
            # for each time step t
            for t in range(this.maxTime):

                break
        return

    # calculate the final output based on an initial input set
    def calculate(self, inputs):
        for j in range(len(x[0])):
            for t in range(this.maxTime):
                break
        return
