def remove_Keys(inputDictionary, inputList):
    for item in inputList:
        if item in inputDictionary:
            del dictionary1[item]


dictionary1 = {"key1": "value1", "key2": "value2",
               "key3": "value3", "key4": "value4"}
keys = ["key1", "key3", "key5"]

remove_Keys(dictionary1, keys)
print(dictionary1)
