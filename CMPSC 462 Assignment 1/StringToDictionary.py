def word_Frequencies(inputString):
    outputDictionary = {}
    for item in inputString.split():
        if item in outputDictionary:
            continue
        outputDictionary[item] = inputString.count(item)
    return outputDictionary


string1 = "yes more yes about more about yes yes yes"

dictionary1 = word_Frequencies(string1)
print(dictionary1)
