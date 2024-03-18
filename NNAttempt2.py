# NN Second Attempt
# Jace Hultzen

def ReLUActivation(z):
    if z > 0:
        return z
    else:
        return 0

def runNetwork(inputData):
    # Initialize temporaryInput with the input data for the first layer
    temporaryInput = inputData
    # Initialize variable to keep track of which layer is being processed
    layerID = 0
    for layer in parametersIn:
        layer = layer.strip('\n').split('perceptronSeparator')
        for perceptron in range(len(layer)):
            layer[perceptron] = layer[perceptron].split(',')
        # Reset temporaryOutput for each layer
        temporaryOutput = []
        for perceptron in layer:
            # Bias is the first element, the rest are weights
            z = float(perceptron[0])  # Initialize z with the bias
            # Iterate over weights and corresponding inputs
            weight_index = 0
            for weight in perceptron[1:]:  #for weight_index, weight in enumerate(perceptron[1:]):
                    try:
                        z += float(weight) * temporaryInput[weight_index]
                        weight_index += 1
                    except:
                        weight_index = 0
            # Apply activation function and store the result
            temporaryOutput.append(ReLUActivation(z))
        # Prepare inputs for the next layer
        print('Layer', layerID, 'output:', temporaryOutput)
        temporaryInput = temporaryOutput
        layerID += 1  # Increment layerID after processing each layer

        # Assuming the last layer's output is what we're interested in:
        if layerID == len(parametersIn):  # Check if it's the last layer
            trueLabel = int(inputData[0])
            # print(temporaryOutput)
            print('Output: ', temporaryOutput.index(max(temporaryOutput)))
            print('True Label: ', trueLabel)
            # Calculate and print loss if needed, using an appropriate loss function
            # Placeholder for loss calculation: (This is a simplification)
            print('Loss: ', abs(temporaryOutput.index(max(temporaryOutput)) - trueLabel))
            print(' ')

parametersIn = open('3l-512-10-10.txt').readlines()
dataIn = open('MNISTtrain.csv')

keepRunning = True
while keepRunning:
    dataIn.seek(0)  # Reset to start of the file for each run
    for line in dataIn:
        dataList = line.strip('\n').split(',')
        for item in range(len(dataList)):
            dataList[item] = float(dataList[item])
        # inputData now contains all the input features plus the label at the start
        inputData = dataList
        runNetwork(inputData)

        exitPrompt = input('Would you like to exit? (y/n): ')
        if exitPrompt.lower() == 'y':
            keepRunning = False
            break
