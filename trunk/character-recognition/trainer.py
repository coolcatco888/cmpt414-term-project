from network import Network

__author__="cley"
__date__ ="$Mar 28, 2011 11:42:30 AM$"

class Trainer:

    training_data = []
    network = 0
    max_steps = 10000

    def __init__(self, training_data):
        self.training_data = training_data
        self.network = Network(4,[6, 4])

    def train(self):
        return

    def test(self):
        return

if __name__ == "__main__":
    print "Hello World"
