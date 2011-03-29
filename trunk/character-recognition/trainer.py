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
        [inputs, desired_outputs] = self.training_data.get_data()
        
        if len(inputs) == len(desired_outputs):
            for t in range(self.max_steps):
                outputs = []
                for i in len(inputs):
                    outputs.append(self.network.learn(inputs[i], desired_outputs[i]))

                if self.__check_if_system_trained(outputs, desired_outputs, 0.1):
                    break
                    
        return

    def __check_if_system_trained(self, outputs, desired_outputs, tolerance):
        isTrained = true

        if len(outputs) == len(desired_outputs):
            for i in len(outputs):
                output = outputs[i]
                desired_output = desired_output[i]

                for j in len(output):
                    if output[j] >= desired_output[j] + tolerance & output[j] <= desired_output[j] - tolerance:
                        isTrained = false
        else:
            isTrained = false
            
        return isTrained

    def test(self, inputs):
        return self.network.calculate(inputs)

if __name__ == "__main__":
    print "Hello World"
