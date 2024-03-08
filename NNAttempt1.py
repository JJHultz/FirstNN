# NN First Attempt

def ReLUActivation(z):
    if z > 0:
        return z
    else:
        return 0

def runNetwork(inputData):
    #print(inputData)
    temporaryInput = inputData[1:]
    #print(temporaryInput)
    temporaryOutput = []
    layerID = 0
    for layer in parametersIn:
        layer = layer.strip('\n').split('perceptronSeparator')
        #print(layer[0])
        #print(type(layer[0]))
        for perceptron in range(len(layer)):
            layer[perceptron] = layer[perceptron].split(',')
        trueLabel = int(inputData[0])
        for perceptron in range(len(layer)):
            if temporaryOutput != []:
                temporaryInput = temporaryOutput
                temporaryOutput = []
            z = float(layer[perceptron][0])
            inputDataIndex = 0
            for weight in range(len(layer[perceptron][1:])):
                #print(layer[perceptron][weight], inputData[inputDataIndex])
                try:
                    #print(type(float(layer[perceptron][weight]))) 
                    #print(type(temporaryInput[inputDataIndex]))
                    #print(temporaryInput)
                    z += float(layer[perceptron][weight]) * temporaryInput[inputDataIndex]
                    #print('z complete')
                    #if weight % 1000 == 0:
                    #    print('loading...')
                except:
                    print('Error: ', 'layer:', layer, 'perceptron:', perceptron, 'weight:', weight, 'Input Data Index:', inputDataIndex)
                    print(layer[perceptron][weight], temporaryInput[inputDataIndex])
            temporaryOutput.append(ReLUActivation(z))
            inputDataIndex += 1

        if layerID == 1:
            print('Output: ', temporaryOutput.index(max(temporaryOutput)))
            print('True Label: ', trueLabel)
            print('Loss: ', (temporaryOutput.index(max(temporaryOutput)) - trueLabel))
            print(' ')
        else:
            layerID += 1
    #print(temporaryOutput)

# layerOneParameters = [[[0.9, 1],[0.4, -1],[0.3, 2],[-1, 0],[1.4, 4]],[[0.1, 4],[0.9, 0],[0.2, -5],[-4, 10],[3, 1]]]
# runLayer(inputData)

parameterset = 'testseed3'+'.txt'

parametersIn = open(parameterset)

dataset = 'MNISTtrain.csv'

dataIn = open(dataset)


keepRunning = True
while keepRunning: 
    batchIndex = 0

    for line in dataIn:
        line = line.strip('\n')
        dataList = line.split(',')
        for item in range(len(dataList)):
            dataList[item] = float(dataList[item])
        trueLabel = dataList[0]
        inputData = dataList[1:]

        #Now we would need to calculate outputs and store them in a list for the next layer to use
        runNetwork(inputData)
        batchIndex += 1

        exit = input('Would you like to exit? (y/n): ')
        if exit == 'y':
            print(batchIndex)
            keepRunning = False
            break
        
