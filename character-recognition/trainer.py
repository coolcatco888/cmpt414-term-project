from network import Network
from training_data import TrainingData

from random import uniform
import matplotlib.pyplot as plot


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

        # get a list of input sets and their corresponding desired outputs
        [x, d] = self.training_data.get_data()
        number_of_tests = len(d) * len(d[0])

        # Training Loop
        while error_rate >= self.acceptable_error_rate and diverge_count < self.max_allowable_diverges:
            error_count = 0.0
            # For each training set calculate desired outputs
            for desired_output, input in zip(d, x):
                #Calculate outputs for this training set or class
                y = self.network.calculate(input);

                # Compute binary output for comparison
                binary_y = [0.0 for out in y]
                max_y = 0.0;
                index_of_max_y = 0
                for i in range(len(y)):
                    out = y[i]
                    if out > max_y:
                        max_y = out
                        index_of_max_y = i
                binary_y[index_of_max_y] = 1.0


                # Compute binary desired output for comparison
                binary_desired_output = [1.0 if (out > 0.0) else 0.0 for out in desired_output]

                #Learn
                self.network.learn(input, desired_output)

                # Count number of errors in output
                for y, desired in zip(binary_y, binary_desired_output):
                    if y != desired:
                        error_count = error_count + 1.0

            # Calculate error rate
            previous_error_rate = error_rate
            error_rate = error_count / number_of_tests

            # Determine number of divergences
            is_converging = False
            if error_rate < previous_error_rate:
                is_converging = True
            diverge_count = 0.0 if is_converging else diverge_count + 1.0

            print error_rate, "\t", previous_error_rate, "\t", is_converging

        return

    def test(self, inputs):
        return self.network.calculate(inputs)

    def get_network(self):
        return self.network

if __name__ == "__main__":
    training_data = TrainingData()
    network = Network(2, [2,2, 4], 0.1, 0.1)

    class_A_desired_out = [1.0, 0.0, 0.0, 0.0]
    class_B_desired_out = [0.0, 1.0, 0.0, 0.0]
    class_C_desired_out = [0.0, 0.0, 1.0, 0.0]
    class_D_desired_out = [0.0, 0.0, 0.0, 1.0]

    set_size = 1000
    test_size = 1000

    for i in range(set_size):
        x = uniform(0.0, 10.0)
        y = uniform(0.0, 10.0)
        training_data.add_dataset([x, y], class_A_desired_out)


        x = uniform(-10.0, 0.0)
        y = uniform(0.0, 10.0)
        training_data.add_dataset([x, y], class_B_desired_out)


        x = uniform(0.0, 10.0)
        y = uniform(-10.0, 0.0)
        training_data.add_dataset([x, y], class_C_desired_out)


        x = uniform(-10.0, 0.0)
        y = uniform(-10.0, 0.0)
        training_data.add_dataset([x, y], class_D_desired_out)

    # Train Network
    trainer = Trainer(training_data, network, 0.015, 30)
    trainer.train()

    for i in range(test_size):
        x = uniform(-10.0, 10.0)
        y = uniform(-10.0, 10.0)

        out = network.calculate([x, y])
        m = 0.0
        mi = 0
        for r in range(len(out)):
            if out[r] > m:
                m = out[r]
                mi = r

        c = (0.0, 0.0, 0.0)
        if mi == 0:
            c = (1.0, 0.0, 0.0)
        if mi == 1:
            c = (0.0, 1.0, 0.0)
        if mi == 2:
            c = (0.0, 0.0, 1.0)
        if mi == 3:
            c = (1.0, 0.6, 0.0)

        plot.plot(x, y, 'o', c = c)
    plot.axis([-10.0, 10.0, -10.0, 10.0])
    plot.show()
    

