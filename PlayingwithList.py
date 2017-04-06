exampleList = [4, 5, 6, 7, 8, 9, 9, 9, 10, 1, 1, 2, 67]

# appending the example list
exampleList.append(190)
print(exampleList)

exampleList.insert(6, 120)
print(exampleList)

# removing the first 9 in the example list
exampleList.remove(9)
print(exampleList)

exampleList.remove(exampleList[8])
print(exampleList)