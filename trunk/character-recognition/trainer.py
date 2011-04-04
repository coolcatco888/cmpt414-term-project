import trainer
import pickle
from network import Network
from training_data import TrainingData

__author__="cley"
__date__ ="$Mar 28, 2011 11:42:30 AM$"

class Trainer:

    training_data = []
    network = 0
    acceptable_error_rate = 0.015
    max_allowable_diverges = 3

    def __init__(self, training_data, network, acceptable_error_rate, max_allowable_diverges):
        self.training_data = training_data
        self.network = network
        self.acceptable_error_rate = acceptable_error_rate
        self.max_allowable_diverges = max_allowable_diverges

    def train(self):

        error_rate = 1.0
        diverge_count = 0
        actual_outputs = []
        binary_outputs = []
        binary_desired_outputs = []

        # get a list of input sets and their corresponding desired outputs
        [x, d] = self.training_data.get_data()
        number_of_tests = len(d) * len(d[0])

        # Training Loop
        while error_rate >= self.acceptable_error_rate and diverge_count < self.max_allowable_diverges:
            
            # For each training set calculate desired outputs
            for input, desired_output in zip(x, d):
                #Calculate outputs for this training set or class
                y = self.network.calculate(input);
                actual_outputs.append(y)

                # Compute binary output for comparison
                binary_y = [1.0 if not(out == 0.0) else 0.0 for out in y]
                binary_outputs.append(binary_y)

                # Compute binary desired output for comparison
                binary_desired_output = [1.0 if not(out == 0.0) else 0.0 for out in desired_output]
                binary_desired_outputs.append(binary_desired_output)

                #Learn
                self.network.learn(input, desired_output)

            # Count number of errors in output
            error_count = 0
            for y, d in zip(binary_outputs, binary_desired_outputs):
                if y != d:
                    error_count = error_count + 1.0

            # Calculate error rate
            previous_error_rate = error_rate
            error_rate = error_count / number_of_tests

            
            # Determine number of divergences
            is_converging = False
            if error_rate < previous_error_rate:
                is_converging = True
            diverge_count = 0.0 if is_converging else diverge_count + 1.0

        return

    def test(self):
        return self.network.calculate(inputs)

    def get_network(self):
        return self.network

if __name__ == "__main__":
    training_data = TrainingData()
    

