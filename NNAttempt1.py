# NN First Attempt

def ReLUActivation(z):
    if z > 0:
        return z
    else:
        return 0

def runLayer(inputData):
    for layer in parametersIn:
        layer = layer.strip().split('perceptronSeparator')
        #print(layer[0])
        #print(type(layer[0]))
        for perceptron in range(len(layer)):
            layer[perceptron] = layer[perceptron].split(',')
        inputDataIndex = 1
        trueLabel = int(inputData[0])
        for perceptron in range(len(layer)):
            z = float(layer[perceptron][0])
            for weight in range(len(layer[perceptron][1:])):
                #print(layer[perceptron][weight], inputData[inputDataIndex])
                try:
                    z += float(layer[perceptron][weight]) * float(inputData[inputDataIndex])
                    if weight % 1000 == 0:
                        print('loading...')
                except:
                    print('Error: ', 'layer:', layer, 'perceptron:', perceptron, 'weight:', weight, 'Input Data Index:', inputDataIndex)
            print(ReLUActivation(z))
            inputDataIndex += 1

# layerOneParameters = [[[0.9, 1],[0.4, -1],[0.3, 2],[-1, 0],[1.4, 4]],[[0.1, 4],[0.9, 0],[0.2, -5],[-4, 10],[3, 1]]]
# runLayer(inputData)

parameterset = 'seed1'+'.txt'

parametersIn = open(parameterset)


dataset = 'MNISTtrain.csv'

dataIn = open(dataset)


keepRunning = True
while keepRunning: 
    batchIndex = 0

    for line in dataIn:
        dataList = line.split(',')
        trueLabel = dataList[0]
        inputData = dataList[1:]

        #Now we would need to calculate outputs and store them in a list for the next layer to use
        runLayer(inputData)
        batchIndex += 1

        exit = input('Would you like to exit? (y/n): ')
        if exit == 'y':
            print(batchIndex)
            keepRunning = False
            break
        else:
            continue
        
