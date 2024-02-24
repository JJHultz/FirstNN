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
