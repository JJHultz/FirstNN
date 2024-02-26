# parameter set creator
# Jace Hultzen

import random

filename = input('Enter a parameter set name: ')
filename = filename + '.txt'

outfile = open(filename, 'w')

layerCount = int(input('Enter the number of layers for this network seed: '))

for layer in range(layerCount):
    line = []
    layer = str(layer)
    parameterCount = int(input('Enter the number of parameters for layer '+layer+' : '))
    layer = int(layer)
    randomSeed = input('Would you like to use a random seed for this layer? (y/n): ')
    if randomSeed == 'y':
        maxWeightValue = int(input('Enter the maximum absolute weight value for the random parameters: '))
        maxBiasValue = int(input('Enter the maximum absolute bias value for the random parameters: '))
        for parameter in range(parameterCount):
            weight = (random.random()-0.5)*2*maxWeightValue
            bias = (random.random()-0.5)*2*maxBiasValue
            parameter = [weight, bias]
            line.append(parameter)

    else:
        weight = int(input('Enter the base value for weight: '))
        bias = int(input('Enter the base value for bias: '))
        for parameter in range(parameterCount):
            parameter = [weight, bias]
            line.append(parameter)


    outfile.write(line)

outfile.close()