# prototyping the first neural network here

# here is a prototype of the first layer of the network, using a list of lists to store the weights, biases, and other parameters. Thinking will be below the list

def ReLUActivation(z):
    if z > 0:
        return z
    else:
        return 0

#File structure:
# empty inputData list?
# layerOneParameters
# layerTwoParameters
    
layerOneParameters = [[[1, 6],[6, 10]],[[0.9, 1],[0.4, -1],[0.3, 2],[-1, 0],[1.4, 4]],[[0.1, 4],[0.9, 0],[0.2, -5],[-4, 10],[3, 1]]]
# layerOneParameters = [[[1, 10]],[[0.9, 1],[0.4, -1],[0.3, 2],[-1, 0],[1.4, 4],[0.1, 4],[0.9, 0],[0.2, -5],[-4, 10],[3, 1]]]
# layerOneVarView = [[[1, 10]],[[w1, b1],[w2, b2],[w3, b3],[w4, b4],[w5, b5],[w6, b6],[w7, b7],[w8, b8],[w9, b9],[w10, b10]]
# layerOneParameters would be previously stored in a txt file and imported into the program, each line of the txt file representing one primary layer of the network

x1 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# sample of how input data might work. instead of ones and zeroes it may be a list of pixel values from an image

def layerOutput(inputData):
    # sample for loop to show how we would pull sublayer ranges from the list of layer one parameters
    for ranges in range(len(layerOneParameters[0])):
        layerRange = layerOneParameters[0][ranges]
        print('layerRange =', layerRange)
        subLayerMin = layerRange[0]
        print('subLayerMin =', subLayerMin)
        subLayerMax = layerRange[1]
        print('subLayerMas =', subLayerMax)
        i = 0
        while True:
            try:
                print(i, layerOneParameters[1][i][0], layerOneParameters[1][i][1])
                z = x1[i] * layerOneParameters[1][i][0] + layerOneParameters[1][i][1]
                print(z)
                i = i + 1
            except:
                break
            

layerOutput(x1)

# [0] will contain a list of ranges for the different sublayers, for use in convolutional layers. The list will contain the index ranges of the weights and biases for each sublayer
# Each weight will be stored within its own list, the index [1] of which will be the bias