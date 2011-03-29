from network import Network
from training_data import TrainingData

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
        net = self.network
        [inputs, desired_outputs] = self.training_data.get_data()
        
        if len(inputs) == len(desired_outputs):
            for t in range(self.max_steps):
                outputs = []
                for i in range(len(inputs)):
                    output = net.learn(inputs[i], desired_outputs[i])
                    outputs.append(output)

                if self.__check_if_system_is_trained(outputs, desired_outputs, 0.1):
                    break
                    
        return

    def __check_if_system_is_trained(self, outputs, desired_outputs, tolerance):
        isTrained = True

        if len(outputs) == len(desired_outputs):
            for i in len(outputs):
                output = outputs[i]
                desired_output = desired_output[i]

                for j in len(output):
                    if output[j] >= desired_output[j] + tolerance & output[j] <= desired_output[j] - tolerance:
                        isTrained = False
        else:
            isTrained = False
            
        return isTrained

    def test(self, inputs):
        return self.network.calculate(inputs)

if __name__ == "__main__":
    training_data = TrainingData()
    training_data.add_dataset([1, 0, 0, 0], [1, 0, 0, 0])
    training_data.add_dataset([1, 1, 0, 0], [0, 1, 0, 0])
    training_data.add_dataset([1, 1, 1, 0], [0, 0, 1, 0])
    training_data.add_dataset([1, 1, 1, 1], [0, 0, 0, 1])

    trainer = Trainer(training_data)

    print "------[Training]-------------"
    trainer.train()

    print "------[Test]-------------"
    print trainer.test([1, 1, 1, 0])


