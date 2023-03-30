dictionary1 = {'a': 10, 'b': 20, 'c': 30, 'd': 20}

dictionary1.update({'a': 500})
print(dictionary1)


def checkDuplicate(inputDictionary):
    tempDictionary = {}
    outputDictionary = {}

    for keys, values in inputDictionary.items():
        if values not in tempDictionary:
            tempDictionary[values] = keys

    for keys, values in tempDictionary.items():
        outputDictionary[values] = keys

    return outputDictionary


dictionary2 = checkDuplicate(dictionary1)
print(dictionary2)
