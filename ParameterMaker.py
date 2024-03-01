# parameter set creator
# Jace Hultzen

import random

filename = input('Enter a parameter set name: ')
filename = filename + '.txt'

outfile = open(filename, 'w')

layerCount = int(input('Enter the number of layers for this network seed: '))

for layer in range(layerCount):
    line = ''
    layer = str(layer)
    perceptronCount = int(input('Enter the number of perceptrons for layer '+layer+' : '))
    layer = int(layer)
    randomSeed = input('Would you like to use a random seed for this layer? (y/n): ')
    if randomSeed == 'y':
        maxWeightValue = float(input('Enter the maximum absolute weight value for the random parameters: '))
        maxBiasValue = float(input('Enter the maximum absolute bias value for the random parameters: '))
        layerParameters = ''
        parameters = '' # to fill in with our weights and bias to add to layer list
        for perceptron in range(perceptronCount):
            if layer == 0:
                bias = (random.random()-0.5)*2*maxBiasValue
                line = line + str(bias) + ','
                i = 1
                inputSize = 784
                while i <= inputSize:
                    if i != inputSize:
                        line = line + str((random.randint(0,10)/10-0.5)*2*maxWeightValue) + ','
                    else:
                        line = line + str((random.randint(0,10)/10-0.5)*2*maxWeightValue)
                    i += 1
                line = line + 'perceptronSeparator'
                previousLayerOutputItems = inputSize
            else:
                i = 1
                while i <= previousLayerOutputItems:
                    if i != previousLayerOutputItems:
                        line = line + str((random.random()-0.5)*2*maxWeightValue) + ','
                    else:
                        line = line + str((random.random()-0.5)*2*maxWeightValue)
                    i += 1

    else:
        print('Still a work in progress!')
        input('Please press CTRL+C to exit the program')
        weight = int(input('Enter the base value for weight: '))
        bias = int(input('Enter the base value for bias: '))
        for parameter in range(perceptronCount):
            parameter = [weight, bias]
            line.append(parameter)
    line = line[:-19]


    #print(line)
    outfile.write(line+'\n')

outfile.close()