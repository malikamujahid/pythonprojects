def flattenList(nestedList):
    if not nestedList:
        return []

    if isinstance(nestedList[0], list):
        return flattenList(nestedList[0]) + flattenList(nestedList[1:])
    else:
        return [nestedList[0]] + flattenList(nestedList[1:])


nestedList = [1, [2, [3, 4], 5], 6, [[7]]]
flattenedList = flattenList(nestedList)
print("Flattened list:", flattenedList)
