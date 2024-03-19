#NNAttempt3.py
# Jace Hultzen

# This time we are going to try to use dictionaries instead of lists for easier updating

import numpy as np

def ReLUActivation(z):
    return np.maximum(0, z)

def initialize_network(input_size, hidden_layer_perceptrons, output_size):
    np.random.seed(42)  # For reproducible results
    network_params = {}
    
    # Initialize parameters for each layer
    layer_sizes = [input_size] + hidden_layer_perceptrons + [output_size]
    for i in range(1, len(layer_sizes)):
        network_params[f'layer{i}'] = {
            'weights': np.random.randn(layer_sizes[i-1], layer_sizes[i]) * 0.1,
            'biases': np.random.randn(layer_sizes[i]) * 0.1
        }
    
    return network_params

def forward_pass(input_data, network_params):
    activation = input_data
    activations = [input_data]  # List to store all activations, layer by layer
    zs = []  # List to store all z vectors, layer by layer

    for i in range(1, len(network_params) + 1):
        layer = f'layer{i}'
        z = np.dot(activation, network_params[layer]['weights']) + network_params[layer]['biases']
        activation = ReLUActivation(z)
        
        zs.append(z)
        activations.append(activation)
    
    return activations[-1], activations, zs  # Return output of last layer

def runNetwork(inputData, network_params):
    # Extract the label and reshape the inputData for the network
    trueLabel = int(inputData[0])  # Extract the true label
    inputData = np.array(inputData[1:]).reshape(1, -1)  # Convert the rest to a numpy array and ensure correct shape

    output, activations, zs = forward_pass(inputData, network_params)
    
    # Assuming the last layer's output is what we're interested in
    predictedLabel = np.argmax(output)
    print('Output: ', predictedLabel)
    print('True Label: ', trueLabel)
    print('Loss: ', abs(predictedLabel - trueLabel))
    print(' ')


# Example initialization
input_size = 784  # For MNIST
hidden_layer_perceptrons = [512]  # One hidden layer with 512 neurons
output_size = 10  # 10 classes for MNIST digits

network_parameters = initialize_network(input_size, hidden_layer_perceptrons, output_size)

# The rest of the data loading and running logic remains the same,
# except inputData needs to be adjusted to work with numpy arrays
# and exclude the label from inputData when calling runNetwork.

dataIn = open('MNISTtrain.csv')

# Main Loop
keepRunning = True
while keepRunning:
    dataIn.seek(0)  # Reset to start of the file for each run
    for line in dataIn:
        dataList = line.strip('\n').split(',')
        dataList = [float(item) for item in dataList]  # Convert each item to float
        runNetwork(dataList, network_parameters)  # Now passing network_parameters as well

        exitPrompt = input('Would you like to exit? (y/n): ')
        if exitPrompt.lower() == 'y':
            keepRunning = False
            break
