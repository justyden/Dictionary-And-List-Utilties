def combine(inputDictionary1, inputDictionary2):
    outputDictionary = inputDictionary1
    for item in inputDictionary2:
        if item in inputDictionary1:
            outputDictionary[item] += inputDictionary2[item]
            continue
        outputDictionary[item] = inputDictionary2[item]
    return outputDictionary


dictionary1 = {'x': 100, 'y': 200, 'm': 100}
dictionary2 = {'x': 200, 'n': 100, 'y': 200}
dictionary3 = combine(dictionary1, dictionary2)
print(dictionary3)
