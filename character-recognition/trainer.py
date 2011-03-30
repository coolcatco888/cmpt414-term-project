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
        net = self.network
        [inputs, desired_outputs] = self.training_data.get_data()
        
        if len(inputs) == len(desired_outputs):
            for t in range(self.max_steps):
                outputs = []
                for i in range(len(inputs)):
                    output = net.learn(inputs[i], desired_outputs[i])
                    outputs.append(output[len(output) - 1])

                if self.__check_if_system_is_trained(outputs, desired_outputs, 0.1):
                    break
                    
        return

    def __check_if_system_is_trained(self, outputs, desired_outputs, tolerance):
        isTrained = True

        if len(outputs) == len(desired_outputs):
            for i in range(len(outputs)):
                output = outputs[i]
                desired_output = desired_outputs[i]

                for j in range(len(output)):
                    if ((output[j] >= desired_output[j] + tolerance) or (output[j] <= desired_output[j] - tolerance)):
                        isTrained = False

                    if isTrained == False:
                        break
                        
                if isTrained == False:
                    break
        else:
            isTrained = False
            
        return isTrained

    def test(self, inputs):
        return self.network.calculate(inputs)

    def get_network(self):
        return self.network

if __name__ == "__main__":
    training_data = TrainingData()
    training_data.add_dataset([1, 0], [1, 0])
    training_data.add_dataset([1, 1], [0, 1])

    network = 0
    try:
        #TODO: Make this serialize whole object
        network = pickle.load( open( "network.net" ) )
    except IOError:
        network = Network(2,[4, 2])

    trainer = Trainer(training_data, network)

    print "------[Training]-------------"
    trainer.train()
    pickle.dump( trainer.get_network(), open( "network.net", "wb" ) )

    print "------[Test]-------------"
    print trainer.test([1, 1])


