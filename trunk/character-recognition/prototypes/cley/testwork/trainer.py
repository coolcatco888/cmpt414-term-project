import trainer
import pickle
from network import Network
from training_data import TrainingData

__author__="cley"
__date__ ="$Mar 28, 2011 11:42:30 AM$"

class Trainer:

    training_data = []
    network = 0
    max_steps = 1000

    def __init__(self, training_data, network):
        self.training_data = training_data
        self.network = network

    def train(self):
        
        return

    def test(self, inputs):
        return self.network.calculate(inputs)

    def get_network(self):
        return self.network

if __name__ == "__main__":
    training_data = TrainingData()
    

    


