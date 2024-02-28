# NN Functions Test

def ReLUActivation(z):
    if z > 0:
        return z
    else:
        return 0

def runLayer(inputData):
    for convLayer in range(len(layerOneParameters)):
        inputDataIndex = 0
        for perceptron in range(len(layerOneParameters[convLayer])):
            z = layerOneParameters[convLayer][perceptron][0] * inputData[inputDataIndex] + layerOneParameters[convLayer][perceptron][1]
            #print(z)
            inputDataIndex += 1
            print(ReLUActivation(z))

# layerOneParameters = [[[0.9, 1],[0.4, -1],[0.3, 2],[-1, 0],[1.4, 4]],[[0.1, 4],[0.9, 0],[0.2, -5],[-4, 10],[3, 1]]]
# runLayer(inputData)

parameterset = input('Enter the file name of the parameter set: ')

parametersIn = open(parameterset)



dataset = input('Enter the file name of the dataset: ')

dataIn = open(dataset)

while True: 
    prelimBatchSize = input('Enter the batch size: ')
    
    currentBatchStartLine = 0

    for line in range(currentBatchStartLine, currentBatchStartLine + prelimBatchSize):
        currentBatchStartLine += 1
        dataList = line.split(',')
        trueLabel = dataList[0]
        inputData = dataList[1:]

        #Now we would need to calculate outputs and store them in a list for the next layer to use
        
