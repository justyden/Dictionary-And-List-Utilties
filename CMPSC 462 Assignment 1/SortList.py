def is_Sorted(inputList):
    checkSort = True
    for i in range(len(inputList)):
        if i + 1 == len(inputList):
            break
        if inputList[i] > inputList[i + 1]:
            checkSort = False
            break
    return checkSort


list1 = [1, 2, 2]
list2 = ['b', 'a']

print(is_Sorted(list1))
print(is_Sorted(list2))
